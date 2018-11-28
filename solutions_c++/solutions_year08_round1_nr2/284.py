/*
 * Sat Jul 26 09:02:27 KST 2008
 */
#define see(n) cerr << #n << " = " << n << endl
#define seeArray(n, a) cerr << #a << " = ";\
    for (int __i__ = 0; __i__ < n; ++__i__)\
        cerr << a[__i__] << " ";\
    cerr << endl;
#define seeArray2(n, m, a) cerr << #a << " = " << endl;\
    for (int __i__ = 0; __i__ < n; ++__i__) {\
        for (int __j__ = 0; __j__ < m; ++__j__)\
            cerr << a[__i__][__j__] << " ";\
        cerr << endl;\
    }
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <list>
#include <sstream>
#include <cctype>
using namespace std;
const int maxn = 1000 + 10;

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

int cases, cas = 1, n, m;
bool mat1[maxn][maxn];
bool mat2[maxn][maxn];
bool mat[maxn][maxn];
int match[maxn];

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d%d", &n, &m);
        memset(mat1, false, sizeof(mat1));
        memset(mat2, false, sizeof(mat2));
        for (int i = 0; i < m; ++i) {
            int cnt, x, y;
            scanf("%d", &cnt);
            for (int k = 0; k < cnt; ++k) {
                scanf("%d%d", &x, &y);
                if (y == 0) {
                    mat1[x - 1][i] = true;
                } else {
                    mat2[x - 1][i] = true;
                }
            }
        }
        int best = 1000000, bestmask;
        for (int mask = 0; mask < (1 << n); ++mask) {
            int cnt = 0;
            for (int i = 0; i < n; ++i) if ((mask & (1 << i)) != 0) {
                cnt++;
            }
            memset(mat, false, sizeof(mat));
            for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
                int next = m * i + j;
                if ((mask & (1 << i)) == 0) {
                    if (mat1[i][j]) {
                        mat[j][next] = true;
                    }
                } else {
                    if (mat2[i][j]) {
                        mat[j][next] = true;
                    }
                }
            }
            int ret = hungary(m, n * m, mat, match);
            if (ret == m && cnt < best) {
                best = cnt;
                bestmask = mask;
            }
        }
        if (best < 1000000) {
            printf("Case #%d:", cas++);
            for (int i = 0; i < n; ++i) {
                if ((bestmask & (1 << i)) == 0) {
                    printf(" 0");
                } else {
                    printf(" 1");
                }
            }
            printf("\n");
        } else {
            printf("Case #%d: IMPOSSIBLE\n", cas++);
        }
    }
    return 0;
}
