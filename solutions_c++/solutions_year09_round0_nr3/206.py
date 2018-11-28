#include <cstdio>
#include <cstring>
char t[] = "?welcome to code jam";
char s[1000];
int dp[1000][1000];
int N, T, S;
int main()
{
	scanf("%d\n", &N);
	for (int n = 1; n <= N; n++)
	{
		gets(s+1);
		S = strlen(s+1);
		T = strlen(t+1);
		memset(dp, 0, sizeof dp);
		for (int i = 0; i <= S; i++)
			dp[i][0] = 1;
		for (int i = 1; i <= S; i++)
			for (int j = 1; j <= T; j++)
			{
				dp[i][j] = dp[i-1][j];
				if (s[i] == t[j])
					dp[i][j] = (dp[i][j]+dp[i-1][j-1]) % 10000;
			}
		printf("Case #%d: %04d\n", n, dp[S][T]);
	}
}
