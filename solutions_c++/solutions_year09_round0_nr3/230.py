#include <stdio.h>
#include <string.h>

int dp[509][20];
char s[509];
char* wel = "welcome to code jam";

int main() {
	freopen("F:\\C-large.in", "r", stdin);
	freopen("F:\\C-large.out", "w", stdout);
	int T, cas = 0;
	int i, j;
	scanf("%d", &T);
	gets(s);
	while (T--) {
		gets(s);
		memset(dp, 0, sizeof(dp));
		for (i = 0; s[i]; ++i) {
			if (i == 0) {
				if (s[i] == wel[0])
					++dp[0][0];
				continue;
			}
			for (j = 0; j <= 18; ++j)
				if (s[i] == wel[j]) {
					if (j == 0) {
						dp[i][j] = dp[i - 1][j] + 1;
						continue;
					}
					dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
					if (dp[i][j] >= 10000)
						dp[i][j] %= 10000;
				} else
					dp[i][j] = dp[i - 1][j];
		}
		printf("Case #%d: %04d\n", ++cas, dp[i - 1][18]);
	}
	return 0;
}