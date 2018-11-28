#include <stdio.h>
#include <string.h>

#include <algorithm>

const int MAX_N = 1 << 10;

int need[MAX_N];
int value[MAX_N];

int dp[MAX_N][11];

int P, limit;

void solve(int root) {
    if (root * 2 >= limit) {
        dp[root][need[root]] = 0;
        if (need[root] > 0) {
            dp[root][need[root] - 1] = value[root];
        }
        return;
    }
    int l = root * 2, r = l + 1;
    solve(l);
    solve(r);
    for (int i = 0; i <= need[l]; i++) {
        if (dp[l][i] < 0) {
            continue;
        }
        for (int j = 0; j <= need[r]; j++) {
            if (dp[r][j] < 0) {
                continue;
            }
            int k = std::max(i, j);
            if (dp[root][k] == -1 || dp[l][i] + dp[r][j] < dp[root][k]) {
                dp[root][k] = dp[l][i] + dp[r][j];
            }
            if (k > 0) {
                if (dp[root][k - 1] == -1 || dp[l][i] + dp[r][j] + value[root] < dp[root][k - 1]) {
                    dp[root][k - 1] = dp[l][i] + dp[r][j] + value[root];
                }
            }
        }
    }
    need[root] = std::max(need[l], need[r]);
}

int main() {
    int caseSize;
    scanf("%d", &caseSize);
    for (int T = 1; T <= caseSize; T++) {
        scanf("%d", &P);
        limit = 1 << P;
        memset(need, 0, sizeof(need));
        memset(dp, -1, sizeof(dp));
        for (int i = 0; i < limit; i++) {
            int tmp;
            scanf("%d", &tmp);
            if (P - tmp > need[((1 << P) + i) / 2]) {
                need[((1 << P) + i) / 2] = P - tmp;
            }
        }
        int m = limit;
        for (int i = 0; i < P; i++) {
            m /= 2;
            for (int j = 0; j < m; j++) {
                scanf("%d", &value[m + j]);
            }
        }
        solve(1);
        printf("Case #%d: %d\n", T, dp[1][0]);
    }
    return 0;
}
