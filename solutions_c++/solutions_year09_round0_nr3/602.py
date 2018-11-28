#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
char tmp[] = "welcome to code jam";
int dp[20];
char str[1000];

int main() {
	int i, j, k;
	int N;
	scanf("%d\n", &N);
	for (i = 0; i < N; i++) {
		gets(str);
		memset(dp, 0, sizeof(dp));
		dp[0] = 1;
		for (j = 0; str[j]; j++) {
			/*for (k = 0; k <= 18; k++) {
				printf("%d : %d\n", k, dp[k]);
			}*/
			for (k = 18; k >= 0; k--) {
				if (tmp[k] == str[j]) {
					dp[k + 1] += dp[k];
					dp[k + 1] %= 10000;
				}
			}
		}
		printf("Case #%d: %.4d\n", i + 1, dp[19]);
	}
	return 0;
} 
