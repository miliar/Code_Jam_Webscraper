# include <iostream>
# include <cstdio>
# include <vector>
# include <set>
# include <queue>
# define MAXN 60
using namespace std;

int n;
char v[MAXN][MAXN], w[MAXN][MAXN];

void rotate()
{
    int i, j, k;
    char c;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            v[j][n - i - 1] = w[i][j];
        }
    }
    for (j = 0; j < n; j++) {
        i = n - 1;
        while(i >= 0) {
            for (k = i; k >= 0; k--) {
                if (v[k][j] != '.') {
                    break;
                }
            }
            if (k >= 0) {
                c = v[k][j];
                v[k][j] = '.';
                v[i][j] = c;
            }
            else {
                break;
            }
            i--;
        }
    }
}

bool valid(int x, int y)
{
    return x >= 0 && x < n && y >= 0 && y < n;
}

int main()
{
    int t, K, i, j, k, q[4][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}}, ii, jj;
    bool a[2];
    int vv[MAXN][MAXN][4];
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        a[0] = a[1] = false;
        scanf("%d%d", &n, &K);
        for (i = 0; i < n; i++) {
            scanf("%s", w[i]);
        }
        rotate();
        memset(vv, 0, sizeof vv);
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                if (v[i][j] != '.') {
                    for (k = 0; k < 4; k++) {
                        vv[i][j][k] = 1;
                        ii = i + q[k][0];
                        jj = j + q[k][1];
                        if (valid(ii, jj) && v[ii][jj] == v[i][j]) {
                            vv[i][j][k] += vv[ii][jj][k];
                        }
                        if (vv[i][j][k] >= K) {
                            a[v[i][j] == 'R'] = true;
                        }
                    }
                }
            }
        }
        printf("Case #%d: %s\n", tt, a[0] && a[1] ? "Both" : a[0] ? "Blue" : a[1] ? "Red" : "Neither");
    }
    return 0;
}
