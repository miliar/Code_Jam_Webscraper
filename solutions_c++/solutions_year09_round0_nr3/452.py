#include <cstdio>
#include <cstring>

char *str = "welcome to code jam";
char ss[512];

int dp[512][20];

void run(int t)
{
	gets(ss);
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for (int i = 0; ss[i]; ++i) {
		dp[i + 1][0] = dp[i][0];
		for (int j = 0; j < 19; ++j) {
			dp[i + 1][j + 1] += dp[i][j + 1];
			if (ss[i] == str[j]) {
				dp[i + 1][j + 1] += dp[i][j];
			}
			dp[i + 1][j + 1] %= 10000;
		}
	}
	int l = strlen(ss);
	printf("Case #%d: %04d\n", t, dp[l][19]);
}

int main()
{
	int t;
	scanf("%d", &t);
	gets(ss);
	for (int i = 1; i <= t; ++i) {
		run(i);
	}
	return 0;
}