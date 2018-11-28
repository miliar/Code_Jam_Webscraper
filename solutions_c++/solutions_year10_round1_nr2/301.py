#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define N 105
#define M 256
#define LL long long

const int INF = 0x7fffffff;

int a[N];
int f[N][M];

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t, i, j, k, p, pj, dc, dk, np, ret, d, e, m, n, cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d %d %d", &d, &e, &m, &n);
        for (i = 1; i <= n; ++i)
            scanf("%d", &a[i]);
        for (i = 1; i <= n; ++i)
            for (j = 0; j < M; ++j) {
                dc = abs(j - a[i]);
                ret = (i - 1) * d + dc;
                for (k = 1; k < i; ++k) {
                    dk = (i - k - 1) * d;
                    if (0 == m)
                        ret = min(ret, f[k][j] + dc + dk);
                    else {
                        for (p = 0; p < M; ++p) {
                            pj = abs(j - p);
                            if (pj == 0) np = 0;
                            else np = (pj - 1) / m * e;
                            ret = min(ret, f[k][p] + dc + dk + np);
                        }
                    }
                }
                f[i][j] = ret;
            }
        ret = n * d;
        for (i = 1; i < n; ++i)
            for (j = 0; j < M; ++j)
                ret = min(ret, f[i][j] + (n - i) * d);
        for (j = 0; j < M; ++j)
            ret = min(ret, f[n][j]);
        printf("Case #%d: %d\n", ++cas, ret);
    }
    return 0;
}
