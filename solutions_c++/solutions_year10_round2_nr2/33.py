#include <stdio.h>
#include <algorithm>

int n, k, b, t;
int x[50], v[50];
int dp[50][51];

int main ()
{
	freopen ("b-large.in", "r", stdin);
	freopen ("b-large.out", "w", stdout);
	int ct, tt;

	tt = 0;
	for (scanf("%d", &ct); ct > 0; ct --)
	{
		scanf ("%d%d%d%d", &n, &k, &b, &t);
		for (int i = 0; i < n; i ++)
			scanf ("%d", x + i);
		for (int i = 0; i < n; i ++)
			scanf ("%d", v + i);
		for (int i = n - 1; i >= 0; i --)
		{
			int reachable = x[i] + t * v[i] >= b;
			for (int j = 0; j <= n; j ++)
			{
				dp[i][j] = 1000000000;
				if (i == n - 1 && j == !reachable)
					dp[i][j] = 0;
				if (j > 0)
				{
					dp[i][j] = std::min(dp[i][j], dp[i][j - 1]);
					if (i + 1 < n)
						dp[i][j] = std::min(dp[i][j], dp[i + 1][j - 1]);
				}
				if (reachable && i + 1 < n)
					dp[i][j] = std::min(dp[i][j], j + dp[i + 1][j]);
			}
		}
		if (dp[0][n - k] >= 1000000000)
			printf ("Case #%d: IMPOSSIBLE\n", ++ tt);
		else
			printf ("Case #%d: %d\n", ++ tt, dp[0][n - k]);
	}

	return 0;
}