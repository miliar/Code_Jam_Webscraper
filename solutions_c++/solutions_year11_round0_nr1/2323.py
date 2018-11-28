#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int dp[111][111][111];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T++) {
        int n;
        scanf("%d", &n);
        char c;
        int x;
        memset(dp, 63, sizeof(dp));
        dp[0][1][1] = 0;
        for (int i = 0; i < n; i++) {
            scanf(" %c %d", &c, &x);//anext
            if (c == 'O') {
                for (int j = 1; j <= 100; j++) {//anow
                    for (int k = 1; k <= 100; k++) {//bnow
                        for (int l = 1; l <= 100; l++) {//bnext
                            if (abs(l - k) > abs(x - j) + 1) continue;
                            dp[i + 1][x][l] = min(dp[i + 1][x][l], dp[i][j][k] + abs(x - j) + 1);
                        }
                    }
                }
            } else {
                for (int j = 1; j <= 100; j++) {//bnow
                    for (int k = 1; k <= 100; k++) {//anow
                        for (int l = 1; l <= 100; l++) {//anext
                            if (abs(l - k) > abs(x - j) + 1) continue;
                            dp[i + 1][l][x] = min(dp[i + 1][l][x], dp[i][k][j] + abs(x - j) + 1);
                        }
                    }
                }
            }
        }
        int ans = 0x3F3F3F3F;
        for (int i = 1; i <= 100; i++) {
            for (int j = 1; j <= 100; j++) {
                if (dp[n][i][j] < ans) {
                    ans = dp[n][i][j];
                }
            }
        }
        printf("Case #%d: %d\n", T, ans);
    }
}
