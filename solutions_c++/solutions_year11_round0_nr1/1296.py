#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int dp[1100];

int abs(int a) {
    if (a < 0) return -a;
    return a;
}

int main() {
    int t, n, clk = 0;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    while (t--) {
        int i, j;
        char id[3];
        scanf("%d", &n);
        
        int pre_a = 0, pre_b = 0;
        int pre_ax = 1, pre_bx = 1;
        memset(dp, 0, sizeof(dp));
        for (i = 1; i <= n; ++i) {
            scanf("%s%d", id, &j);
            if (id[0] == 'O') {
                dp[i] = max(dp[i-1], dp[pre_b] + abs(pre_bx - j)) + 1;
                pre_b = i;
                pre_bx = j;
            } else {
                dp[i] = max(dp[i-1], dp[pre_a] + abs(pre_ax - j)) + 1;
                pre_a = i;
                pre_ax = j;
            }
        }
        printf("Case #%d: %d\n", ++clk, dp[n]);
    }
    //system("pause");
    return 0;
}
