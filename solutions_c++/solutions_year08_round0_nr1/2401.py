#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <map>
using namespace std;

int dp[1002][102];
char se[102][102];
int qu[1002];

int main()
{
//	freopen("C:\\A-large.in", "r", stdin);
//	freopen("C:\\test2.out", "w+", stdout);
	int i, j, m, n, k, cas, ca = 0, ans;
	char tmp[102];
	scanf("%d", &cas);
	while(cas--)
	{
		scanf("%d", &n);
		gets(tmp);
		for(i = 1;i <= n; i++) gets(se[i]);
		scanf("%d", &m);
		gets(tmp);
		for(i = 1;i <= m; i++) 
		{
			gets(tmp);
			for(j = 1;j <= n; j++) if(strcmp(se[j], tmp) == 0) break;
			qu[i] = j;
		}
		memset(dp, -1, sizeof(dp));
		for(j = 1;j <= n; j++) dp[0][j] = dp[1][j] = 0; dp[1][qu[1]] = -1;

		for(i = 2;i <= m; i++)
		{
			for(j = 1;j <= n; j++)
			{			
				if(qu[i] != j)
				{
					if(dp[i-1][j] != -1) dp[i][j] = dp[i-1][j];
					for(k = 1;k <= n; k++)
					{
						if(k != j && dp[i-1][k] != -1 && (dp[i-1][k] + 1 < dp[i][j] || dp[i][j] == -1)) dp[i][j] = dp[i-1][k] + 1;
					}
				}
			}
		}
		ans = 100000;
		for(i = 1;i <= n; i++) if(dp[m][i] >= 0 && dp[m][i] < ans) ans = dp[m][i];
		printf("Case #%d: %d\n", ++ca, ans);
	}
	return 0;
}