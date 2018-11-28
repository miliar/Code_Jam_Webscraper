#include <stdio.h>
#include <string.h>

#include <algorithm>

int dp[101][256];
int a[100];
bool used[256];
int D, I, M, N;

int main() {
    int caseSize;
    scanf("%d", &caseSize);
    for (int T = 1; T <= caseSize; T++) {
        scanf("%d%d%d%d", &D, &I, &M, &N);
        for (int i = 0; i <= N; i++) {
            if (i != 0) {
                memset(dp[i], -1, sizeof(dp[i]));
            } else {
                memset(dp[i], 0, sizeof(dp[i]));
            }
        }
        for (int i = 0; i < N; i++) {
            scanf("%d", &a[i]);
        }
        for (int i = 0; i < N; i++) {
            memset(used, false, sizeof(used));
            for (int j = 0; j < 256; j++) {
                int pos = -1;
                for (int k = 0; k < 256; k++) {
                    if (!used[k] && (pos == -1 || dp[i][k] < dp[i][pos])) {
                        pos = k;
                    }
                }
                if (pos == -1) {
                    break;
                }
//                printf("%d %d %d\n", i, pos, dp[i][pos]);
                used[pos] = true;
                //delete
                if (dp[i + 1][pos] == -1 || dp[i][pos] + D < dp[i + 1][pos]) {
                    dp[i + 1][pos] = dp[i][pos] + D;
                }
                int Min = std::max(0, pos - M), Max = std::min(255, pos + M);
                //insert
                for (int k = Min; k <= Max; k++) {
                    if (dp[i][k] == -1 || dp[i][pos] + I < dp[i][k]) {
                        dp[i][k] = dp[i][pos] + I;
                    }
                }
                //change
                for (int k = Min; k <= Max; k++) {
                    int cost = std::abs(a[i] - k);
                    if (dp[i + 1][k] == -1 || dp[i][pos] + cost < dp[i + 1][k]) {
                        dp[i + 1][k] = dp[i][pos] + cost;
                    }
                }
            }
        }
        int result = -1;
        for (int i = 0; i < 256; i++) {
            if (result == -1 || dp[N][i] < result) {
                result = dp[N][i];
            }
        }
        printf("Case #%d: %d\n", T, result);
    }
    return 0;
}
