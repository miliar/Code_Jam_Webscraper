#include <cstdio>
#include <algorithm>

using namespace std;

int type[32000];
int change[32000];
int value[32000][2];

const int oo = 100000000;

int main()
{
	int kases, kase = 0;
	for (scanf("%d", &kases); kases; kases--)
	{
		int n, r;
		scanf("%d%d", &n, &r);
		for (int i = 1; i <= (n-1)/2; i++)
			scanf("%d%d", &type[i], &change[i]);
		for (int i = (n-1)/2 + 1; i <= n; i++)
		{
			int x;
			scanf("%d", &x);
			value[i][x] = 0;
			value[i][!x] = oo;
		}
		for (int i = (n-1)/2; i >= 1; i--)
		{
			if (type[i] == 1)
			{
				value[i][1] = min(oo, value[2*i][1] + value[2*i+1][1]);
				value[i][0] = min(oo, min(value[2*i][0], value[2*i+1][0]));
				if (change[i])
				{
					value[i][1] = min(value[i][1], 1 + min(value[2*i][1], value[2*i+1][1]));
					value[i][0] = min(value[i][0], 1 + value[2*i][0] + value[2*i+1][0]);
				}
			}
			else
			{
				value[i][1] = min(oo, min(value[2*i][1], value[2*i+1][1]));
				value[i][0] = min(oo, value[2*i][0] + value[2*i+1][0]);
				if (change[i])
				{
					value[i][1] = min(value[i][1], 1 + value[2*i][1] + value[2*i+1][1]);
					value[i][0] = min(value[i][0], 1 + min(value[2*i][0], value[2*i+1][0]));
				}
			}
		}

		if (value[1][r] == oo)
			printf("Case #%d: IMPOSSIBLE\n", ++kase);
		else
			printf("Case #%d: %d\n", ++kase, value[1][r]);
	}
	return 0;
}
