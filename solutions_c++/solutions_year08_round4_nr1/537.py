#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAXN 16384
#define INF 1000000000

using namespace std;

int f[MAXN][2];
int c[MAXN], g[MAXN];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ti = 0; ti < T; ti++) {
        int n, v;
        scanf("%d%d", &n, &v);
        for (int i = 1; i <= n; i++) f[i][0] = f[i][1] = INF;
        int intern = (n - 1) / 2;
        for (int i = 1; i <= intern; i++) {
            int tg, tc;
            scanf("%d%d", &tg, &tc);
            g[i] = tg;
            c[i] = tc;
        }
        for (int i = intern + 1; i <= n; i++) {
            int t;
            scanf("%d", &t);
            f[i][t] = 0;
        }
        for (int i = intern; i >= 1; i--) {
            for (int p = 0; p < 2; p++) {
                for (int q = 0; q < 2; q++) {
                    int cost = f[2 * i][p] + f[2 * i + 1][q];
                    if (g[i] == 0) {
                        f[i][p || q] = min(cost, f[i][p || q]);
                        if (c[i]) {
                            f[i][p && q] = min(cost + 1, f[i][p && q]);
                        }
                    }
                    else {
                        f[i][p && q] = min(cost, f[i][p && q]);
                        if (c[i]) {
                            f[i][p || q] = min(cost + 1, f[i][p || q]);
                        }
                    }
                }
            }
        }
        printf("Case #%d: ", ti + 1);
        if (f[1][v] != INF) printf("%d\n", f[1][v]);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
