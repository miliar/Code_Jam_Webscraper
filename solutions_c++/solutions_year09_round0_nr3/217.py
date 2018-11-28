#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#ifndef ONLINE_JUDGE
int poj();
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	poj();
	return 0;
}
#define main poj
#endif

#define clr(x) memset(x, 0, sizeof(x))
#define MAXINT 200000000
#define EPS 0.00000001
#define MAXN 300

int n;
int dp[600][30];
char table[300] = "welcome to code jam";

int main()
{
	int i, j, k, t, result;
	char buf[1000];
	
	scanf("%d\n", &n);
	for (k = 1; k <= n; k++)
	{
		fgets(buf, 900, stdin);
		if (buf[strlen(buf) - 1] == '\n') buf[strlen(buf) - 1] = '\0';
		//printf("%s\n", buf);
		clr(dp);
		for (i = 0; i < strlen(buf); i++)
		{
			if (buf[i] == 'w')
				dp[i][0] = 1;
			for (j = 0; j < i; j++)
			{
				for (t = 1; t < 19; t++)
				{
					if (table[t - 1] == buf[j] && table[t] == buf[i] && dp[j][t - 1])
					{
						dp[i][t] += dp[j][t - 1];
						dp[i][t] %= 10000;
					}
				}
			}
		}
		result = 0;
		for (i = 0; i < strlen(buf); i++)
		{
			if (buf[i] == 'm')
			{
				result += dp[i][18];
				result %= 10000;
			}
		}
		printf("Case #%d: %04d\n", k, result);
	}
	
	return 0;
}
