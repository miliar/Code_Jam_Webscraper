#include <stdio.h>
#include <string.h>

char line[1000];
char pattern[30] = "welcome to code jam";
const int mod = 10000;
int dp[1000][30];

int main() {
	int tc, l = strlen(pattern);
	gets(line);
	sscanf(line, "%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		gets(line);
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;
		int i;
		for (i=0; line[i]; ++i) {
			for (int j=0; j<=l; ++j) {
				dp[i+1][j] = dp[i][j];
				if (j && pattern[j-1] == line[i])
					dp[i+1][j] = (dp[i+1][j] + dp[i][j-1]) % mod;
			}
		}
		printf("Case #%d: %04d\n", scen, dp[i][l]);
	}
	return 0;
}
