#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

const int maxn = 128;
const int maxm = 32;
int cases, cas = 1;
int n, m;
int price[maxn][maxm];
bool mat[maxn][maxn];
int match[maxn];

bool find(int u, int m, bool mat[][maxn], bool used[], int match[]) {
    for (int v = 0; v < m; ++v) if (mat[u][v] && !used[v]) {
        used[v] = true;
        if (match[v] < 0 || find(match[v], m, mat, used, match)) {
            match[v] = u;
            return true;
        }
    }
    return false;
}

int hungary(int n, int m, bool mat[][maxn], int match[]) {
    bool used[maxn];
    int ret = 0;
    memset(match, 0xff, sizeof(int) * m);
    for (int i = 0; i < n; ++i) {
        memset(used, false, sizeof(bool) * m);
        if (find(i, m, mat, used, match)) {
            ret++;
        }
    }
    return ret;
}

bool inc(int x, int y) {
    for (int k = 0; k < m; ++k) if (price[x][k] >= price[y][k]) {
        return false;
    }
    return true;
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
            scanf("%d", &price[i][j]);
        }
        memset(mat, false, sizeof(mat));
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) if (inc(i, j)) {
            mat[i][j] = true;
        }
        int ans = n - hungary(n, n, mat, match);
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}

