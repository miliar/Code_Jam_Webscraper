#include<iostream>
#include<sstream>
using namespace std;

bool v[50000];
bool L[12][81*11];
int b[20];

bool ok(int x, int b)
{
	memset(v, 0, sizeof(v));
	int tmp;
	while (1)
	{
		tmp = 0;
		while (x)
		{
			tmp += (x%b) * (x%b);
			x /= b;
		}
		if (tmp == 1)
			return 1;
		if (v[tmp])
			return 0;
		v[tmp] = 1;
		x = tmp;	
	}
}

void deal(int I)
{
	int s = b[I]; 
	for (int i = 0; i < 81*11; i++)
	{
		if (!ok(i, s))
			L[I][i] = 0;
	}
}	

int main()
{
	int tc, n;
	scanf("%d", &tc);
	getchar();
	for (int T = 1; T <= tc; T++)
	{
		memset(L, 1, sizeof(L));
		n = 0;
		string str, line;
		getline(cin, line);
		istringstream stream(line);
		while(stream>>b[n])
		{
			deal(n);
			++n;
		}
		for (int i = 2; ; i++)
		{
			int fail = 0;
			for (int j = 0; j < n; j++)
			{
				int tmp = 0, x = i;
				while (x)
				{
					tmp += (x%b[j]) * (x%b[j]);
					x /= b[j];
				}
				if (!L[j][tmp])
				{
					fail = 1;
					break;
				}
			}
			if (!fail)
			{
				printf("Case #%d: %d\n", T, i);
				break;
			}
		}
	}
	return 0;
}

/*

5555
2 3 4 5 6 7 8 9 10


*/
