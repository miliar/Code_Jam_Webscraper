#include <iostream>
#include <vector>
using namespace std;
const int MAX = 100005;
const int INF = 1000000;

int n, m, cc;
int op[MAX], v[MAX], c[MAX];
int dp[MAX][2];

int main (void)
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T, Case = 1;
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d %d", &n, &cc);
		m = (n-1)/2;

		int i, j, k;
		for (i = 0; i < m; ++ i)
		{
			scanf("%d", op+i);
			scanf("%d", c+i);
		}
		for (i = 0; i < n; ++ i)
			dp[i][0] = dp[i][1] = INF;
		for (i = m; i < n; ++ i)
		{
			scanf("%d", v+i);
			dp[i][v[i]] = 0;
		}
		
		int l, r, t;
		for (i = m-1; i >= 0; -- i)
		{
			l = (i<<1)+1; r = (i<<1)+2;
			if (c[i])
			{
				if (op[i])
				{
					for (j = 0; j < 2; ++ j)
						for (k = 0; k < 2; ++ k)
							if (dp[l][j] != INF && dp[r][k] != INF)
							{
								t = j & k;
								dp[i][t] = min(dp[i][t], dp[l][j]+dp[r][k]);
								t = j | k;
								dp[i][t] = min(dp[i][t], dp[l][j]+dp[r][k]+1); 
							}
				}
				else
				{
					for (j = 0; j < 2; ++ j)
						for (k = 0; k < 2; ++ k)
							if (dp[l][j] != INF && dp[r][k] != INF)
							{
								t = j | k;
								dp[i][t] = min(dp[i][t], dp[l][j]+dp[r][k]);
								t = j & k;
								dp[i][t] = min(dp[i][t], dp[l][j]+dp[r][k]+1);
							}
				}
			}
			else
			{
				if (op[i])
				{
					for (j = 0; j < 2; ++ j)
						for (k = 0; k < 2; ++ k)
							if (dp[l][j] != INF && dp[r][k] != INF)
							{
								t = j & k;
								dp[i][t] = min(dp[i][t], dp[l][j]+dp[r][k]);
							}
				}
				else
				{
					for (j = 0; j < 2; ++ j)
						for (k = 0; k < 2; ++ k)
							if (dp[l][j] != INF && dp[r][k] != INF)
							{
								t = j | k;
								dp[i][t] = min(dp[i][t], dp[l][j]+dp[r][k]);
							}
				}
			}
		}

		printf("Case #%d: ", Case++);
		int ans = dp[0][cc];
		if (ans == INF)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
	return 0;
}