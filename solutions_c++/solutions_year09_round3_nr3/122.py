#include <stdlib.h>
#include <stdio.h>
//
// 
//

int cut[510], dp[510][510];

int main() {

		freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);

    int n, l, i, j, k, t;
	scanf("%d", &t);
	int C = 1;
    while(t --) {
		scanf("%d %d", &l, &n);
        for(i = 1;i <= n;++ i) 
            scanf("%d", &cut[i]);
        cut[0] = 0, cut[n+1] = l + 1;
        for(i = 0;i <= n - 1;++ i) {
            dp[i][i+2] = cut[i+2] - cut[i] - 2;
            dp[i][i+1] = 0;
            dp[i][i] = 0;
        }
        dp[n][n+1] = 0;
        dp[n+1][n+1] = dp[n][n] = 0;
        for(i = 2;i <= n + 1;++ i) {
            for(j = 0;j <= n + 1 - i;++ j) {
                int value = cut[j+i] - cut[j] - 2;
                dp[j][j+i] = dp[j][j+1] + dp[j+1][i+j] + value;
                for(k = j + 1;k < i + j;++ k) {
                    if(dp[j][k] + dp[k][i+j]  + value < dp[j][j+i])
                        dp[j][j+i] = dp[j][k] + dp[k][i+j] + value;
                }
            }
        }       
        printf("Case #%d: %d\n",C++, dp[0][n+1]);
    }
    return 0;
}

