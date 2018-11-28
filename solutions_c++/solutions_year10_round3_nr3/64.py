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

const int maxn = 520;

int r, c;

int rr[maxn][maxn], s[maxn][maxn], flg[maxn][maxn], mp[maxn][maxn];
bool g[maxn][maxn][maxn][2];
int tot[maxn];
char ch;

int get(int i, int j, int ni, int nj) {
    return s[i][j] - s[ni-1][j] - s[i][nj-1] + s[ni-1][nj-1];
}

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d%d", &r, &c);
        char tmp;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c / 4; j++) {
                scanf(" %c", &ch);
                if (isdigit(ch)) tmp = ch - '0'; else tmp = ch - 'A' + 10;
                for (int k = 0; k < 4; k++)
                    mp[i + 1][j * 4 + k + 1] = (tmp & (1 << (3 - k))) >= 1 ? 1 : 0;
            }
//rep(i,r) { rep(j, c) printf("%d", mp[i+1][j+1]); puts(""); }
        memset(g, 0, sizeof(g));

        for (int i = 1; i <= r; i++) for (int j = 1; j <= c; j++) g[1][i][j][mp[i][j]] = 1;

        for (int k = 2; k <= min(r, c); k++) {
            for (int i = k; i <= r; i++)
                for (int j = k; j <= c; j++) {
                    int t = mp[i][j];
                    if (g[k-1][i][j-1][1-t] && g[k-1][i-1][j][1-t] && g[k-1][i-1][j-1][t]) {
                        g[k][i][j][t] = 1;
                    }


                }
        }

        memset(s, 0, sizeof(s));
        memset(rr, 0, sizeof(rr));
        memset(tot, 0, sizeof(tot));

        for (int k = min(r, c); k >= 1; k--) {

            for (int i = 1; i <= r; i++)
                for (int j = 1; j <= c; j++) flg[i][j] = 0;

            int ni, nj, now = 0;
            for (int i = 1; i + k - 1<= r; i++)
                for (int j = 1; j + k - 1 <= c; j++) if (!flg[i][j] && get(i+k-1, j+k-1, i, j) == 0) {

                    ni = i + k - 1;
                    nj = j + k - 1;
                    if (flg[ni][nj] || flg[ni][j] || flg[i][nj]) continue;
                    if (!g[k][ni][nj][mp[ni][nj]]) continue;
                    tot[k]++;
                    for (int x = i; x <= ni; x++)
                        for (int y = j; y <= nj; y++) now++, flg[x][y] = 1;
                }

            for (int i = 1; i <= r; i++)
                for (int j = 1; j <= c; j++) if (flg[i][j]) rr[i][j] = 1;
//rep(i,r) { rep(j, c) printf("%d", rr[i+1][j+1]); puts(""); }
            memset(s, 0, sizeof(s));
            for (int i = 1; i <= r; i++) {
                int tmp = 0;
                for (int j = 1; j <= c; j++) {
                    tmp += rr[i][j];
                    s[i][j] = s[i - 1][j] + tmp;
                }
            }

        }
        int ans = 0;
        int chk = 0;
        for (int k = min(r, c); k >= 1; k--) if (tot[k] > 0) {
            ans++;
            chk += k * k * tot[k];
        }
        if (chk != r * c) while (1) printf("%d \n", tt + 1);
        printf("Case #%d: %d\n", tt + 1, ans);
        for (int k = min(r, c); k >= 1; k--) if (tot[k] > 0) printf("%d %d\n", k, tot[k]);
    }
}
