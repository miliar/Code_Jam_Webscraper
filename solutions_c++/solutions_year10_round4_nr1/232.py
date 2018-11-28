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

const int maxn = 1000;
const int maxm = 1000000;

int opp[maxn], tot[maxn];
int mp[maxn][maxn];
int x[maxm], y[maxm], z[maxm];
int m;
int flg[maxn][maxn];
int n;

bool ok(int len) {
    int tmp = 1;
    foru(i, 1, len * 2 - 1) {
        tot[i] = tmp;
        if (i <= len) {
            opp[i] = len * 2 - i;
            opp[len * 2 - i] = i;
        }

        if (i < len) tmp ++; else tmp--;
    }

    int tim = 0;
    memset(flg, 0, sizeof(flg));
    int nx, ny, mx, my;
//printf("len = %d\n", len);
    for (int i = 1; i <= len * 2 - 1; i++)
        for (int j = 1; j <= tot[i]; j++) {
            int ok = 1;
            ++tim;
            for (int p = 0; p < m; p++) {
               if (x[p] <= 0 && i <= len || x[p] > 0 && i > len) {
                    nx = x[p] + i;
                    ny = y[p] + j;
                } else if (x[p] <= 0 && i > len) {
                    nx = x[p] + i;
                    ny = y[p] + j - (i - len);
                } else if (x[p] > 0 && i <= len) {
                    nx = x[p] + i;
                    ny = y[p] + j + (len - i);
                }

                if (nx < 0 || nx >= len * 2 || ny > tot[nx] || ny <= 0) {
                    ok = 0;
                    continue;
                }

                flg[nx][ny] = tim;
                mp[nx][ny] = z[p];
            }
            for (int p = 0; ok && p < m; p++) {

                if (x[p] <= 0 && i <= len || x[p] > 0 && i > len) {
                    nx = x[p] + i;
                    ny = y[p] + j;
                } else if (x[p] <= 0 && i > len) {
                    nx = x[p] + i;
                    ny = y[p] + j - (i - len);
                } else if (x[p] > 0 && i <= len) {
                    nx = x[p] + i;
                    ny = y[p] + j + (len - i);
                }
                if (nx < 0 || nx >= len * 2 || ny > tot[nx] || ny <= 0) {
                    ok = 0;
                    continue;
                }
                mx = opp[nx];
                my = ny;
                if (flg[mx][my] != tim || mp[nx][ny] == mp[mx][my]) {
                } else ok = 0;

                if (x[p] <= 0 && i <= len || x[p] > 0 && i > len) {
                    nx = x[p] + i;
                    ny = y[p] + j;
                } else if (x[p] <= 0 && i > len) {
                    nx = x[p] + i;
                    ny = y[p] + j - (i - len);
                } else if (x[p] > 0 && i <= len) {
                    nx = x[p] + i;
                    ny = y[p] + j + (len - i);
                }
                if (nx < 0 || nx >= len * 2 || ny > tot[nx] || ny <= 0) {
                    ok = 0;
                    continue;
                }

                mx = nx;
                my = tot[nx] - ny + 1;
                if (flg[mx][my] != tim || mp[nx][ny] == mp[mx][my]) {}
                else ok = 0;
            }
            if (ok) return 1;
        }
    return 0;
}

char cmd[1000000];

int main() {
    int cas;
    scanf(" %d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d", &n);
        foru(i, 1, n) tot[i] = i;
        gets(cmd);
        for (int i = 1; i <= n; i++) {
            int k = i;
            tot[i] = k;
            tot[n * 2 - i] = k;
        }
        m = 0;
        int t;
        for (int i = 1; i <= n * 2 - 1; i++) {
            for (int j = 1; j <= tot[i]; j++) {
                scanf(" %d", &t);
                x[m] = i - n;
                y[m] = j - 1;
                z[m] = t;
                m++;
            }
        }

//        for (int i = 0; i < m; i++) printf("%d %d %d\n", x[i], y[i], z[i]);

//        printf("%d\n", ok(n));
//        continue;
        int l, r, mid;
        for (l = n; ; l++) {
            if (ok(l)) {
                printf("Case #%d: %d\n", tt + 1, l * l - n * n);
                break;
            }
        }

    }
}
