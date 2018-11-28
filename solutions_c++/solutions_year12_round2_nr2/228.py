#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int inf = int(1e9);

const int dx[] = { 1, 0,-1, 0};
const int dy[] = { 0, 1, 0,-1};

int f[110][110];
int t[110][110];
int d[110][110][4];
bool use[110][110];

int T;
int h, n, m;
int a[110][110];
int b[110][110];

void add(int i1, int j1, int i2, int j2, int q) {
    if (i2 < 0 || i2 >= n) return;
    if (j2 < 0 || j2 >= m) return;
    if (b[i2][j2] - a[i2][j2] < 50) return;
    if (b[i2][j2] - a[i1][j1] < 50) return;
    if (b[i1][j1] - a[i2][j2] < 50) return;
    d[i1][j1][q] = h - (b[i2][j2] - 50);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    forn(tt, T) {
        scanf("%d%d%d", &h, &n, &m);
        forn(i, n)
            forn(j, m) scanf("%d", &b[i][j]);
        forn(i, n)
            forn(j, m) scanf("%d", &a[i][j]);

        forn(i, n)
            forn(j, m) {
                t[i][j] = inf;
                use[i][j] = 0;
                f[i][j] = h - (a[i][j] + 20);
                forn(q, 4) {
                    d[i][j][q] = inf;
                    add(i, j, i + dx[q], j + dy[q], q);
                }
            }

        t[0][0] = 0;
        forn(z, n * m) {
            int ui = 0, uj = 0, mn = inf;
            forn(i, n)
                forn(j, m)
                    if ((!use[i][j]) && mn > t[i][j]) {
                        ui = i, uj = j, mn = t[i][j];
                    }
            if (ui == n - 1 && uj == m - 1) break;
            use[ui][uj] = 1;
            forn(q, 4)
                if (d[ui][uj][q] != inf) {
                    if (max(t[ui][uj], d[ui][uj][q]) <= 0) t[ui + dx[q]][uj + dy[q]] = 0;
                    else {
                        if (max(t[ui][uj], d[ui][uj][q]) <= f[ui][uj])
                            t[ui + dx[q]][uj + dy[q]] = min(t[ui + dx[q]][uj + dy[q]], max(t[ui][uj], d[ui][uj][q]) + 10);
                        else
                            t[ui + dx[q]][uj + dy[q]] = min(t[ui + dx[q]][uj + dy[q]], max(t[ui][uj], d[ui][uj][q]) + 100);
                    }
                }
        }

        printf("Case #%d: ", tt + 1);

        printf("%d.%d\n", t[n - 1][m - 1] / 10, t[n - 1][m - 1] % 10);
    }
    return 0;
}
