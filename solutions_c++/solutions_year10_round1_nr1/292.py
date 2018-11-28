#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100;

char g[N][N];
int off[4][2] = {0, 1, 1, 0, 1, 1, -1, 1};
int n, m;

void rotate_line(int i) {
    if (count(g[i], g[i] + n, '.') == n) return;
    char buffer[N];
    fill_n(buffer, n, '.');
    char *p = buffer + n - 1;
    for (int j = n - 1; j >= 0; --j) {
        if ('.' != g[i][j]) {
            *(p--) = g[i][j];
        }
    }
    copy(buffer, buffer + n, g[i]);
}
void rotate_all() {
    for (int i = 0; i < n; ++i) {
        rotate_line(i);
    }
}
bool check(char color) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < 4; ++k) {
                int l;
                int r = i;
                int c = j;
                for (l = 0; l < m; ++l) {
                    if (r < 0 || r >= n || c < 0 || c >= n) break;
                    if (g[r][c] != color) break;
                    r += off[k][0];
                    c += off[k][1];
                }
                if (l == m) return true;
            }
        }
    }
    return false;
}
void solve() {
    freopen("A-large.in", "r", stdin);
    freopen("a.large.out", "w", stdout);

    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", g[i]);
        }
        rotate_all();
        bool r = check('R');
        bool b = check('B');
        printf("Case #%d: ", tci);
        if (r && b) puts("Both");
        else if (!r && !b) puts("Neither");
        else if (r && !b) puts("Red");
        else puts("Blue");
    }
}
int main() {
    solve();
    return 0;
}

