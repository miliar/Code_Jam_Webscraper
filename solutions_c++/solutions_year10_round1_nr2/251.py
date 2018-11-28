#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int N = 110;

int a[N];
int f[N + 1][256];
int n, m, del, ins;

int dp() {
    for (int i = 0; i < 256; ++i) {
        f[0][i] = 0;
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < 256; ++j) {
            f[i][j] = 0x7fffffff;
        }
    }
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 256; ++j) {
            if (0x7fffffff == f[i][j]) continue;
            
            f[i + 1][j] = min(f[i + 1][j], f[i][j] + del);
            
            for (int k = 0; k < 256; ++k) {
                if (k != j) {
                    if (m) {
                        int cost = ins * ((abs(k - j) - 1) / m);
                        f[i + 1][k] = min(f[i + 1][k], f[i][j] + cost + abs(k - a[i]));
                    }
                } else {
                    f[i + 1][k] = min(f[i + 1][k], f[i][j] + abs(k - a[i]));
                }
            }
        }
    }
    
    int best = 0x7fffffff;
    for (int i = 0; i < 256; ++i) {
        best = min(best, f[n][i]);
    }
    return best;
}
void solve() {
    freopen("B-large.in", "r", stdin);
    freopen("b.large.out", "w", stdout);
    //freopen("test.in", "r", stdin);
    //freopen("test.out", "w", stdout);

    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        scanf("%d%d%d%d", &del, &ins, &m, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", a + i);
        }
        int ans = dp();
        printf("Case #%d: %d\n", tci, ans);
    }
}
int main() {
    solve();
    return 0;
}

