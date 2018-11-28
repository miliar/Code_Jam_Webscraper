#include <stdio.h>
#include <string.h>
int dp[511][21];
char gcj[] = "welcome to code jam";
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	char s[511];
	int t, tc = 1;
	int i, j, len;
	scanf("%d\n", &t);
	for ( ; tc <= t; ++tc)
	{
		gets(s);
		len = strlen(s);
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;
		for (i = 1; i <= len; ++i)
		{
			dp[i][0] = 1;
			for (j = 1; j <= 19 && i >= j; ++j)
			{
				if (s[i - 1] == gcj[j - 1])
				{
					dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10000;
				}
				else
				{
					dp[i][j] = dp[i - 1][j];
				}
			}
		}
		printf("Case #%d: %04d\n", tc, dp[len][19]);
	}
	return 0;
}
