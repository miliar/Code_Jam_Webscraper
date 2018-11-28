#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>

using namespace std;

const int N = 101;

bool g[2][N][N];

bool step() {
    int res = true;
    for (int i = 1; i < N; ++i) {
        for (int j = 1; j < N; ++j) {
            if (g[0][i][j]) {
                if (g[0][i - 1][j] || g[0][i][j - 1]) {
                    g[1][i][j] = true;
                    res = false;
                } else {
                    g[1][i][j] = false;
                }
            } else {
                if (g[0][i - 1][j] && g[0][i][j - 1]) {
                    g[1][i][j] = true;
                    res = false;
                } else {
                    g[1][i][j] = false;
                }
            }
        }
    }
    memcpy(g[0], g[1], sizeof(g[0]));
    return res;
}
int solve_one() {
    int ans = -1;
    for (int i = 1; i < N; ++i) {
        for (int j = 1; j < N; ++j) {
            if (g[0][i][j]) {
                ans = 0;
                break;
            }
        }
    }
    if (ans < 0) return 0;
    do {
        ++ans;
    } while (!step());
    return ans;
}
void fill_g(int x1, int y1, int x2, int y2) {
    for (int i = x1; i <= x2; ++i) {
        for (int j = y1; j <= y2; ++j) {
            g[0][i][j] = true;
        }
    }
}
void opt() {
    for (int i = 1; i < 7; ++i) {
        for (int j = 1; j < 7; ++j) {
            if (g[0][i][j]) {
                putchar('1');
            } else {
                putchar('0');
            }
        }
        putchar('\n');
    }
}
void solve() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("c.small.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        memset(g, 0, sizeof(g));
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            int x1, y1, x2, y2;
            scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
            fill_g(x1, y1, x2, y2);
        }
        //opt();
        int ans = solve_one();
        printf("Case #%d: %d\n", tci, ans);
    }
}
int main() {
    solve();
    return 0;
}

