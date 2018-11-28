#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <utility>
#include <algorithm>
#include <numeric>
#include <functional>

using namespace std;

int t, n, d[10010], l[10010], dp[10010];

void solve() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d%d", &d[i], &l[i]);
    }
    scanf("%d", &d[n]);
    memset(dp, 0, sizeof(dp));
    dp[0] = d[0];
    bool ok = false;
    for (int i = 0; i < n; ++i) {
        if (d[i] == 0)
            continue;
        for (int j = i + 1; j <= n; ++j) {
            if (d[i] + dp[i] < d[j])
                break;
            if (j == n)
                ok = true;
            else
                dp[j] = max(dp[j], min(l[j], d[j] - d[i]));
        }
    }
    printf("Case #%d: %s\n", ++t, ok ? "YES" : "NO");
}

int main() {
    freopen("A.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
