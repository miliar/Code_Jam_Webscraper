#include <cstdio>
#include <cstring>

int dp[501][21];
int N, L;
char text[502], pattern[21] = " welcome to code jam";

int main()
{
	scanf("%d", &N);
	gets(text);
	for(int t = 1;t <= N;++t)
	{
		text[0] = ' ';
		gets(text + 1);
		L = strlen(text);
		memset(dp, 0, sizeof(dp));
		for(int i = 0;i <= L;++i)
			dp[i][0] = 1;
		for(int i = 1;i <= L;++i)
			for(int j = 1;j <= 20;++j)
				if(text[i] == pattern[j])
					dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10000;
				else
					dp[i][j] = dp[i - 1][j];
		printf("Case #%d: %04d\n", t, dp[L][20]);
	}
	return 0;
}
