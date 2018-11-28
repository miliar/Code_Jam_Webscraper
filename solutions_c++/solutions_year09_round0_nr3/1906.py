#include <stdio.h>
#include <string.h>
char s[510];
int dp[19][510];
char str[] = "welcome to code jam";
int main() {
    int ca, i, j, cases = 0;
    scanf("%d\n", &ca);
    while (ca--) {
        gets(s);
        memset(dp, 0, sizeof(dp));
        for (i = 0; i < 19; ++i) {
            for (j = 0; s[j]; ++j) {
                if (s[j] == str[i]) {
                    if (i>0) {
                        dp[i][j] = dp[i-1][j];
                    } else {
                        dp[i][j] = 1;
                    }
                    if (j>0) {
                        dp[i][j] = (dp[i][j] + dp[i][j-1])%10000;
                    }
                } else {
                    dp[i][j] = j>0? dp[i][j-1] : 0;
                }
            }
        }
        printf("Case #%d: %04d\n", ++cases, dp[18][j-1] % 10000);

    }
	return 0;
}