#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int t, n;
	char s[506];
	char p[20] = "welcome to code jam";
	scanf("%d\n", &t);
	for (int c=1; c<=t; c++) {
		int dp[20] = {0};
		dp[0] = 1;
		gets(s);
		n = strlen(s);
		for (int i=0; i<n; i++) {
			for (int j=0; j<=18; j++) {
				if (s[i] == p[j]) {
					dp[j+1] += dp[j];
					dp[j+1] %= 10000;
				}
			}
		}
		printf("Case #%d: %04d\n", c, dp[19]);
	}
	return 0;
}
