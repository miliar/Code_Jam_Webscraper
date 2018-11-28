#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

#define MAX 10010

using namespace std;

int d[MAX], l[MAX], dp[MAX];

bool solve(int n, int w) {
    int i, j;

    dp[0] = d[0];
    if (dp[0] + d[0] >= w) return true;
    for (i = 1; i < n; ++i) {
        dp[i] = 0;
        for (j = 0; j < i; ++j) {
            if (d[j] + dp[j] >= d[i]) {
                dp[i] = max(dp[i], min(l[i], d[i] - d[j]));
            }
        }

        if (d[i] + dp[i] >= w) return true;
    }

    return false;
}

int main() {
    int t, ct = 0, n, w, i;

    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; ++i) scanf("%d %d", &d[i], &l[i]);
        scanf("%d", &w);
        printf("Case #%d: %s\n", ++ct, solve(n, w) ? "YES" : "NO");
    }

    return 0;
}
