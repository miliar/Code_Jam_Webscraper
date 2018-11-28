#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>

using namespace std;

const int N = 200;

char g[N][N];
int n;

bool check_one(char l, char r) {
    if (' ' == l || ' ' == r) return true;
    if (0 == l || 0 == r) return true;
    return l == r;
}
bool check(int r) {
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < 2 * n - 1; ++j) {
            if (!check_one(g[i][j], g[2 * r - i][j])) {
                return false;
            }
        }
    }
    return true;
}
void rotate_g() {
    for (int i = 0; i < 2 * n - 1; ++i) {
        for (int j = 0; j < i; ++j) {
            swap(g[i][j], g[j][i]);
        }
    }
}
void flip_row() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 2 * n - 1; ++j) {
            swap(g[i][j], g[2 * n - 2 - i][j]);
        }
    }
}
void flip_col() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 2 * n - 1; ++j) {
            swap(g[j][i], g[j][2 * n - 2 - i]);
        }
    }
}
int best_row() {
    for (int i = n - 1; i >= 0; --i) {
        if (check(i)) return i;
    }
    assert(false);
    return 0;
}
void opt() {
    for (int i = 0; i < 2 * n - 1; ++i) {
        puts(g[i]);
    }
}
int solve_one() {
    int r = best_row();
    //opt();
    flip_row();
    r = max(r, best_row());
    //opt();
    rotate_g();
    //opt();
    int c = best_row();
    flip_row();
    c = max(c, best_row());

    //printf("%d %d\n", r, c);
    
    int x = 2 * n - 1 - r;
    int y = c + x - n;
    int z = 2 * x - 1 - y;
    int ans = z * z - n * n;
    return ans;
}
void solve() {
    freopen("A-large.in", "r", stdin);
    freopen("a.large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        memset(g, ' ', sizeof(g));
        scanf("%d", &n);
        getchar();
        //printf("%d\n", n);
        for (int i = 0; i < 2 * n - 1; ++i) {
            gets(g[i]);
            g[i][strlen(g[i])] = ' ';
            g[i][2 * n - 1] = 0;
        }
        int ans = solve_one();
        printf("Case #%d: %d\n", tci, ans);
    }
}
int main() {
    solve();
    return 0;
}

