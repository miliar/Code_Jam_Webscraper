#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>

#define SZ 200

using namespace std;

int store[SZ];

int main()
{
//	freopen("A-small-attempt0.in", "rt", stdin);
//	freopen("A-small.out", "wt", stdout);
	
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int i, j, kase, inp, len;
	char line[100];
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		for(i = 0; i < SZ; i++)
		{
			store[i] = -1;
		}
		scanf("%s", line);
		len = strlen(line);
		store[line[0]] = 1;
		i = 1;
		while(line[i] == line[0] && i < len)
		{
			i++;
		}
		if(i < len)
		{
			store[line[i]] = 0;
			j = 2;
			i++;
			for( ; i < len; i++)
			{
				if(store[line[i]] < 0)
				{
					store[line[i]] = j;
					j++;
				}
			}
		}
		int b = 0;
		for(i = 0; i < SZ; i++)
		{
			if(store[i] != -1)
			{
				b++;
			}
		}
		if(b == 1)
			b++;

		__int64 ret = 0;
		__int64 j = 1;
		for(i = len - 1; i > -1; i--)
		{
			ret = ret + store[line[i]] * j;
			j *= b;
		}
		printf("Case #%d: %I64d\n", kase, ret);
	}

	return 0;
}
