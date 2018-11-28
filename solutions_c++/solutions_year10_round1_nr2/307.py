#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

int dp[105][260];
int data[105];
int n, m, dd, ii;
int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d%d%d", &dd, &ii, &m, &n);
        for (int i = 1; i <= n; ++i)
            scanf("%d", &data[i]);
        memset(dp, 63, sizeof(dp));
        for (int i = 0; i < 256; ++i)
            dp[0][i] = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < 256; ++j) {
                for (int k = 0; k < 256; ++k) {
                    if (abs(j - k) <= m) {
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(j - data[i]));
                    }
                }
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + dd);
                if (m > 0 && abs(data[i] - j) > 0) {
                    int num = abs(data[i] - j) / m + (abs(data[i] - j) % m != 0);
                    num--;
                    dp[i][data[i]] = min(dp[i][data[i]], dp[i - 1][j] + ii * num);
                }
            }
        }
        int ans = 2000000000;
        for (int i = 0; i < 256; ++i)
            ans = min(ans, dp[n][i]);
        printf("Case #%d: %d\n", ca, ans);
    }

    return 0;
}
