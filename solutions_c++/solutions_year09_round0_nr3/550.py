#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

const int len = 19;
char phrase[len + 1] = "welcome to code jam";

char line[1000];
int dp[len + 1], dpnext[len + 1];

int main()
{
	int cas, cases, i, j;
	scanf("%d\n", &cases);
	for (cas = 1; cas <= cases; cas++) {
		fgets(line, 1000, stdin);
		memset(dp, 0, sizeof(dp));
		dp[0] = 1;
		for (i = 0; line[i]; i++) {
			memset(dpnext, 0, sizeof(dpnext));
			dpnext[0] = 1;
			for (j = 0; j < len; j++) {
				if (line[i] == phrase[j]) {
					dpnext[j + 1] = (dp[j + 1] + dp[j]) % 10000;
				} else {
					dpnext[j + 1] = dp[j + 1];
				}
			}
			memcpy(dp, dpnext, sizeof(dpnext));
		}
		printf("Case #%d: %04d\n", cas, dp[len] % 10000);
	}
	return 0;
}
