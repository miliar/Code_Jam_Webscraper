#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int n, c, d;
char combin[36][3];
char opp[28][2];
char list[101];
char output[101];

char junk;

int compress(int out)
{
	if(out < 1)
		return -2;
	for(int i = 0;i < c; i++)
	{
		if((output[out] == combin[i][0] && output[out-1] == combin[i][1]) ||
			 (output[out] == combin[i][1] && output[out-1] == combin[i][0]) )
		{
			output[out-1] = combin[i][2];
			return out-1;
		}
	}

	for(int i = 0; i < d; i++)
	{
		for(int j = 0; j < out; j++)
		{
			if((output[out] == opp[i][0] && output[j] == opp[i][1]) ||
				 (output[out] == opp[i][1] && output[j] == opp[i][0]) )
			{
				return -1;
			}
		}
	}
	return -2;
}

void solve()
{
	//printf("%s\n", list);
	if(n == 0)
		return;

	output[0] = list[0];

	int in = 1;
	int out = 1;
	int newout;
	while(in < n)
	{
		//printf("%d %d\n", in, out);
		output[out] = list[in];
		newout = compress(out);
		while(newout >= -1)
		{
			//printf("newout : %d\n", newout);
			out = newout;
			newout = compress(out);
		}
		out++;
		in++;
	}
	//printf("%d %d\n", in, out);

	printf("[");
	for(int i = 0;i < out; i++)
	{
		if(i!=0)
			printf(", ");
		printf("%c", output[i]);
	}
	printf("]\n");
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		scanf("%d", &c);
		scanf("%c", &junk);

		for(int j = 0; j < c; j++)
		{
			scanf("%s", combin[j]);
			scanf("%c", &junk);
		}

		scanf("%d", &d);
		scanf("%c", &junk);

		for(int j = 0; j < d; j++)
		{
			scanf("%s", opp[j]);
			scanf("%c", &junk);
		}
		scanf("%d %s", &n, list);
		
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
