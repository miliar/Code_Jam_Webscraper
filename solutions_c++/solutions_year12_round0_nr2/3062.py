#include <stdio.h>
#include <string.h>
#include <algorithm>
#define INF 1000000
int abs(int n) { return n < 0 ? -n : n; }
int dp[105][105], sco[105], p;
int dfs(int n, int k)
{
	int i, j, f;
	if (n <= 0) return k == 0 ? 0 : -INF;
	if (~dp[n][k]) return dp[n][k];
	dp[n][k] = 0;
	if (k > 0)
	{
		for (i = 0; i <= 10; i++)
			if (sco[n] - i * 3 >= 2 && sco[n] - i * 3 <= 4)
			{
				if (i + 2 >= p)
					f = 1;
				else
					f = 0;
				dp[n][k] = std::max(dfs(n-1, k-1)+f, dp[n][k]);
			}
	}
	for (i = 0; i <= 10; i++)
	{
		if (sco[n] - i * 3 >= 1 && sco[n] - i * 3 <= 2)
		{
			if (i + 1 >= p)
				f = 1;
			else
				f = 0;
			dp[n][k] = std::max(dfs(n-1, k)+f, dp[n][k]);
		}
		else if (sco[n] - i * 3 == 0)
		{
		    if (i >= p)
                f = 1;
            else
                f = 0;
            dp[n][k] = std::max(dfs(n-1, k)+f, dp[n][k]);
		}
	}
	return dp[n][k];
}

int main()
{
	int t, cnt, n, s, i;

    cnt = 1;
    scanf("%d", &t);
    while (t--)
    {
        scanf("%d %d %d", &n, &s, &p);
        for (i = 1; i <= n; i++)
            scanf("%d", &sco[i]);
        memset(dp, -1, sizeof(dp));
        dp[0][0] = 0;
        printf("Case #%d: %d\n", cnt++, dfs(n, s));
    }
	return 0;
}
