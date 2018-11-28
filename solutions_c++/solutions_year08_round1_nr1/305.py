/*
 * Sat Jul 26 10:00:06 KST 2008
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

const int maxn = 800 + 10;
const long long inf = 100000000000000000LL;

bool find(int u, int m, long long mat[][maxn], bool* used, int* match, int* que, int& p, long long* lx, long long* ly) {
    que[p++] = u;
    for (int v = 0; v < m; ++v) if (!used[v] && lx[u] + ly[v] == mat[u][v]) {
        used[v] = true;
        if (match[v] < 0 || find(match[v], m, mat, used, match, que, p, lx, ly)) {
            match[v] = u;
            return true;
        }
    }
    return false;
}
long long kuhn_munkres(int n, int m, long long mat[][maxn], int match[]) {
    bool used[maxn];
    long long lx[maxn], ly[maxn], ret = 0;
    int que[maxn], p;
    memset(match, 0xff, sizeof(int) * m);
    for (int i = 0; i < n; ++i) {
        lx[i] = mat[i][0];
        for (int j = 1; j < m; ++j) {
            lx[i] = std::max(mat[i][j], lx[i]);
        }
    }
    for (int i = 0; i < m; ++i) {
        ly[i] = 0;
    }
    for (int i = 0; i < n; ++i) {
        memset(used, false, sizeof(bool) * m);
        if (!find(i, m, mat, used, match, que, p = 0, lx, ly)) {
            i--;
            long long delta = inf;
            for (int k = 0; k < p; ++k) for (int j = 0; j < m; ++j) if (!used[j]) {
                delta = std::min(delta, lx[que[k]] + ly[j] - mat[que[k]][j]);
            }
            for (int k = 0; k < p; ++k) {
                lx[que[k]] -= delta;
            }
            for (int k = 0; k < m; ++k) if (used[k]) {
                ly[k] += delta;
            }
        }
    }
    for (int i = 0; i < m; ++i) if (match[i] >= 0) {
        ret += mat[match[i]][i];
    }
    return ret;
}

int cases, cas = 1, n;
long long x[maxn], y[maxn];
long long mat[maxn][maxn];
int match[maxn];

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%lld", &x[i]);
        }
        for (int i = 0; i < n; ++i) {
            scanf("%lld", &y[i]);
        }
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) {
            mat[i][j] = -x[i] * y[j];
        }
        long long ret = kuhn_munkres(n, n, mat, match);
        printf("Case #%d: %lld\n", cas++, -ret);
    }
    return 0;
}
