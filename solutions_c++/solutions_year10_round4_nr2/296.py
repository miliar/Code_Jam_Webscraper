#include<sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn = 2000;
const int maxm = 15;

int g[maxm][maxn], r[maxm][maxn][maxm], b[maxm][maxn][maxm], a[maxn];
int n;

int get(int k, int nb, int nc) {
    if (b[k][nb][nc] == 1) return r[k][nb][nc];
    if (k == 0)	{
        if (a[nb * 2] <= nc && a[nb * 2 + 1] <= nc)
			r[k][nb][nc] = 0;
		else if (a[nb * 2] <= nc + 1 && a[nb * 2 + 1] <= nc + 1)
			r[k][nb][nc] = g[k][nb];
		else
			r[k][nb][nc] = -1;
		return r[k][nb][nc];
	}

	int now = -1;
	rep(i, nc + 2) rep(j, nc + 2) {
        int tmp = 0;
		if (i == nc + 1 || j == nc + 1) tmp += g[k][nb];
		if (get(k - 1, nb * 2, i) >= 0 && get(k - 1, nb * 2 + 1, j) >= 0) {
			tmp += r[k - 1][nb * 2][i] + r[k - 1][nb * 2 + 1][j];
			if (now == -1 || tmp < now) now = tmp;
		}
	}

	r[k][nb][nc] = now;
	b[k][nb][nc] = 1;
	return now;
}

int main() {
    int cas;
    scanf(" %d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        memset(a,0,sizeof(a));
        memset(b, 0, sizeof(b));
        memset(g, 0,sizeof(g));
        memset(r, 0, sizeof(r));
        scanf("%d", &n);
        rep(i, (1 << n)) {
            scanf("%d",&a[i]);
            a[i] = n - a[i];
        }
        rep(i, n) rep(j, (1 << (n - i - 1))) scanf("%d", &g[i][j]);
        int res = get(n - 1, 0, 0);
        printf("Case #%d: %d\n", tt + 1, res);
    }
}

