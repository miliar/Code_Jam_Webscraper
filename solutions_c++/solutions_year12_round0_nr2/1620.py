#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
const int maxn = 105;
int f[maxn], g[maxn], dp[maxn][maxn];

void update(int &u, int v) {
    if(u == -1 || u < v) {
        u = v;
    }
}

int dis(int x, int y, int z) {
    return max(abs(x - y), max(abs(x - z), abs(y - z)));
}


void pre() {
    memset(f, -1, sizeof(f));
    memset(g, -1, sizeof(f));
    for(int i = 0; i <= 10; i++) {
        for(int j = 0; j <= 10; j++) {
            for(int k = 0; k <= 10; k++) {
                int d = dis(i, j, k);
                if(d > 2) continue;
                if(d == 2) {
                    update(f[i + j + k], max(i, max(j, k)));
                }
                else {
                    update(g[i + j + k], max(i, max(j, k)));
                }
            }
        }
    }
}

int ca, n, s, p, v[maxn];

int main() {
    freopen("gcj_B.out", "w", stdout);
    pre();
    scanf("%d", &ca);
    for(int t = 1; t <= ca; t++) {
        memset(dp, -1, sizeof(dp));
        scanf("%d%d%d", &n, &s, &p);
        for(int i = 0; i < n; i++) scanf("%d", v + i);
        dp[0][0] = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j <= s; j++) {
                if(dp[i][j] == -1) continue;
                if(g[v[i]] != -1) update(dp[i + 1][j], dp[i][j] + (g[v[i]] >= p));
                if(j < s && f[v[i]] != -1) {
                    update(dp[i + 1][j + 1], dp[i][j] + (f[v[i]] >= p));
                }
            }
        }
        printf("Case #%d: %d\n", t, dp[n][s]);
    }
    return 0;
}

