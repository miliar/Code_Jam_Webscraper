#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cctype>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ll long long

class tnode {
public:
    ll x, y;

    tnode () {}
    tnode (int nx, int ny): x(nx), y(ny) {}
};

bool operator==(const tnode &a, const tnode &b) {
    return a.x == b.x && a.y == b.y;
}

const int maxn = 1100;

int nx[maxn], ty[maxn], tx[maxn];
int pr[maxn][30];
int n, m, g[maxn][maxn], res;

ll det(tnode &c, tnode &a, tnode &b) {
    return (a.x - c.x) *( b.y - c.y) - (a.y - c.y) * (b.x - c.x);
}

int sgn(ll x) {
    return x < 0 ? -1 : x > 0;
}

bool cross(tnode &a, tnode &b, tnode &c, tnode &d) {
    return sgn(det(a, b, c)) * sgn(det(a, b, d)) < 0 && sgn(det(c, d, a)) * sgn(det(c, d, b)) < 0;
}

bool dfs(int x) {
    if (nx[x]) return 0;
    nx[x] = 1;
    for (int i = 0; i < n; i++) if (g[x][i]) {
        int tmp = ty[i];
        ty[i] = x;
        if (tmp < 0 || dfs(tmp)) {
            return 1;
        }
        ty[i] = tmp;
    }
    return 0;
}

void solve() {
    memset(tx, -1, sizeof(tx));
    memset(ty, -1, sizeof(ty));
    memset(g, 0, sizeof(g));
    tnode u, v, x, y;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            int ok = 0;
            for (int k = 0; !ok && k + 1 < m; k++) {
                u = tnode(k, pr[i][k]);
                v = tnode(k, pr[j][k]);
                if (u == v) ok = 1;
                x = tnode(k + 1, pr[i][k + 1]);
                y = tnode(k + 1, pr[j][k + 1]);
                if (x == y) ok = 1;
                if (cross(u, x, v, y)) ok = 1;
            }
            if (ok) continue;
            //printf("%d %d\n", i, j);
            if (pr[i][0] > pr[j][0])
                g[i][j] = 1;
        }
    res = 0;
    for (int i = 0; i < n; i++) {
        memset(nx, 0, sizeof(nx));
        if (dfs(i)) res++;
    }
}


int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) scanf("%d", &pr[i][j]);
        }
        solve();
        cout << "Case #" << tt + 1 << ": " << n - res << endl;
    }
    return 0;
}
