#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

long long xx[2][501][501];
long long yy[2][501][501];
long long ww[2][501][501];
int re[501][501];
long long rr[501][501], cc[501][501];
long long rri[501][501], cci[501][501];
long long rrj[501][501], ccj[501][501];
int R, C, D;
char tmp[10000];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d%d", &R, &C, &D);
        for (int i = 0; i < R; ++i) {
            scanf("%s", &tmp);
            for (int j = 0; j < C; ++j)
                re[i][j] = D + tmp[j] - '0';
        }
        for (int i = 0; i < R; ++i) {
            rr[i][0] = re[i][0];
            rri[i][0] = i * re[i][0];
            rrj[i][0] = 0;
            for (int j = 1; j < C; ++j) {
                rr[i][j] = rr[i][j - 1] + re[i][j];
                rri[i][j] = rri[i][j - 1] + i * re[i][j];
                rrj[i][j] = rrj[i][j - 1] + j * re[i][j];
            }
        }
        for (int i = 0; i < C; ++i) {
            cc[i][0] = re[0][i];
            cci[i][0] = 0;
            ccj[i][0] = i * re[0][i];
            for (int j = 1; j < R; ++j) {
                cc[i][j] = cc[i][j - 1] + re[j][i];
                cci[i][j] = cci[i][j - 1] + j * re[j][i];
                ccj[i][j] = ccj[i][j - 1] + i * re[j][i];
            }
        }
        int now = 1, pre = 0;
        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j) {
                xx[pre][i][j] = re[i][j] * i;
                yy[pre][i][j] = re[i][j] * j;
                ww[pre][i][j] = re[i][j];
            }
        int ans = 0;
        for (int k = 2; k <= min(R, C); ++k) {
            for (int i = 0; i < R; ++i)
                for (int j = 0; j < C; ++j) {
                    if (i + k - 1 >= R || j + k - 1 >= C) continue;
                    xx[now][i][j] = xx[pre][i][j] +
                        rri[i + k - 1][j + k - 1] - (j > 0 ? rri[i + k - 1][j - 1] : 0) +
                        cci[j + k - 1][i + k - 1] - (i > 0 ? cci[j + k - 1][i - 1] : 0) -
                        re[i + k - 1][j + k - 1] * (i + k - 1);
                    yy[now][i][j] = yy[pre][i][j] +
                        rrj[i + k - 1][j + k - 1] - (j > 0 ? rrj[i + k - 1][j - 1] : 0) +
                        ccj[j + k - 1][i + k - 1] - (i > 0 ? ccj[j + k - 1][i - 1] : 0) -
                        re[i + k - 1][j + k - 1] * (j + k - 1);
                    ww[now][i][j] = ww[pre][i][j] +
                        rr[i + k - 1][j + k - 1] - (j > 0 ? rr[i + k - 1][j - 1] : 0) +
                        cc[j + k - 1][i + k - 1] - (i > 0 ? cc[j + k - 1][i - 1] : 0) -
                        re[i + k - 1][j + k - 1];
                    long long x1 = xx[now][i][j] -
                        re[i][j] * i - re[i + k - 1][j] * (i + k - 1) -
                        re[i][j + k - 1] * i - re[i + k - 1][j + k - 1] * (i + k - 1);
                    long long y1 = yy[now][i][j] -
                        re[i][j] * j - re[i + k - 1][j] * j -
                        re[i][j + k - 1] * (j + k - 1) - re[i + k - 1][j + k - 1] * (j + k - 1);
                    long long w1 = ww[now][i][j] -
                        re[i][j] - re[i + k - 1][j] -
                        re[i][j + k - 1] - re[i + k - 1][j + k - 1];
                    if ((j + j + k - 1) * w1 == 2 * y1 &&
                        (i + i + k - 1) * w1 == 2 * x1) {
                        ans = max(ans, k);
                    }
                }
            pre = now;
            now = 1 - now;
        }
        if (ans < 3) printf("Case #%d: IMPOSSIBLE\n", ca);
        else printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
