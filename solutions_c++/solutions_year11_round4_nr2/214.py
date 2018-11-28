#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;

//BEGIN TEMPLATE HERE
typedef long long int64;

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
//END TEMPLATE HERE

const int maxn = 500 + 5;
const double eps = 1e-8;

int Sign(double x) {
    return fabs(x) < eps ? 0 : x < 0 ? -1 : 1;
}

double sw[maxn][maxn], sx[maxn][maxn], sy[maxn][maxn];
double d[maxn][maxn], dx[maxn][maxn], dy[maxn][maxn];
char g[maxn][maxn];
int R, C;
double D;

double sqr(double x) {
    return x * x;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
    //freopen("input.txt", "r", stdin);
    int tests;
    scanf("%d", &tests);
    for (int caseId = 1; caseId <= tests; caseId++) {
        printf("Case #%d: ", caseId);
        scanf("%d%d%lf", &R, &C, &D);
        for (int i = 1; i <= R; ++i) scanf("%s", g[i] + 1);
        for (int i = 1; i <= R; ++i) for (int j = 1; j <= C; ++j) d[i][j] = (int)(g[i][j] - '0') + D;
        for (int i = 0; i <= R; ++i) {
            for (int j = 0; j <= C; ++j) {
                sx[i][j] = sy[i][j] = sw[i][j] = 0.0;
            }
        }
        for (int i = 1; i <= R; ++i) {
            double cntx = 0.0, cnty = 0.0, cnt2 = 0.0;
            for (int j = 1; j <= C; ++j) {
                dx[i][j] = i * d[i][j];
                dy[i][j] = j * d[i][j];
                cntx += dx[i][j];
                sx[i][j] = sx[i - 1][j] + cntx;
                cnty += dy[i][j];
                sy[i][j] = sy[i - 1][j] + cnty;
                cnt2 += d[i][j];
                sw[i][j] = sw[i - 1][j] + cnt2;
            }
        }
        int ans = 0;
        for (int K = 3; K <= min(R, C); ++K) {
            for (int x = 0; x + K <= R; ++x) {
                for (int y = 0; y + K <= C; ++y) {
                    if (ans >= K) {
                        continue;
                    }
                    double w = sw[x + K][y + K] - sw[x][y + K] - sw[x + K][y] + sw[x][y];
                    w -= d[x + 1][y + 1];
                    w -= d[x + 1][y + K];
                    w -= d[x + K][y + 1];
                    w -= d[x + K][y + K];
                    double mx = sx[x + K][y + K] - sx[x][y + K] - sx[x + K][y] + sx[x][y];
                    mx -= dx[x + 1][y + 1];
                    mx -= dx[x + 1][y + K];
                    mx -= dx[x + K][y + 1];
                    mx -= dx[x + K][y + K];
                    double my = sy[x + K][y + K] - sy[x][y + K] - sy[x + K][y] + sy[x][y];
                    my -= dy[x + 1][y + 1];
                    my -= dy[x + 1][y + K];
                    my -= dy[x + K][y + 1];
                    my -= dy[x + K][y + K];
                    mx /= w;
                    my /= w;
                    if (Sign(mx - (x + 1 + x + K) / 2.0) == 0 && Sign(my - (y + 1 + y + K) / 2.0) == 0) {
                        ans = max(ans, K);
                    }
                }
            }
        }
        if (ans == 0) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}

