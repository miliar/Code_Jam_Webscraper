#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <complex>
#include <utility>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <numeric>
#include <functional>
using namespace std;

const double PI = acos(-1.0);
const double EPS = 1e-7;

#define MP make_pair
#define PB push_back
#define SIZE(X) ((int)((X).size()))

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef vector<int> vint;
typedef vector<int64> vint64;
typedef vector<double> vdouble;
typedef vector<string> vstring;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vpii;

int N, M;
long long D;
long long tbl[505][505];
long long sum[505][505] = {};

bool Valid_odd(int i, int j, int k) {
    k /= 2;
    return 1 <= i - k && i + k <= N && 1 <= j - k && j + k <= M;
}
bool Valid_even(int i, int j, int k) {
    k /= 2;
    k--;
    return 1 <= i - k && i + k < N && 1 <= j - k && j + k < M;
}

inline int Abs(int a) {
    return a >= 0 ? a : -a;
}

int main() {
    int t, casN;
    char buf[505];
    int i, j, k;

    scanf("%d", &t);
    for (casN = 1; casN <= t; casN++) {
        scanf("%d%d%lld", &N, &M, &D);
        for (i = 1; i <= N; i++) {
            scanf("%s", buf + 1);
            for (j = 1; j <= M; j++) {
                tbl[i][j] = D + (buf[j] - '0');
            }
        }
        for (i = 1; i <= N; i++) {
            for (j = 1; j <= M; j++) {
                sum[i][j] = sum[i][j - 1] + tbl[i][j];
            }
        }
        int ans = 0;
        for (i = 1; i <= N; i++) {
            for (j = 1; j <= M; j++) {
                long long x = 0, y = 0;
                for (k = 3; Valid_odd(i, j, k); k += 2) {
                    for (int a = i - k / 2 + 1; a < i + k / 2; a++) {
                        x += tbl[a][j + k / 2] * (a - i);
                        x += tbl[a][j - k / 2] * (a - i);
                    }
                    for (int b = j - k / 2 + 1; b < j + k / 2; b++) {
                        x += tbl[i + k / 2][b] * (k / 2);
                        x -= tbl[i - k / 2][b] * (k / 2);
                    }
                    for (int a = i - k / 2 + 1; a < i + k / 2; a++) {
                        y += tbl[a][j + k / 2] * (k / 2);
                        y -= tbl[a][j - k / 2] * (k / 2);
                    }
                    for (int b = j - k / 2 + 1; b < j + k / 2; b++) {
                        y += tbl[i + k / 2][b] * (b - j);
                        y += tbl[i - k / 2][b] * (b - j);
                    }
                    if (k > 3) {
                        x -= tbl[i - k / 2 + 1][j - k / 2 + 1] * (k / 2 - 1);
                        x -= tbl[i - k / 2 + 1][j + k / 2 - 1] * (k / 2 - 1);
                        x += tbl[i + k / 2 - 1][j - k / 2 + 1] * (k / 2 - 1);
                        x += tbl[i + k / 2 - 1][j + k / 2 - 1] * (k / 2 - 1);
                        y -= tbl[i - k / 2 + 1][j - k / 2 + 1] * (k / 2 - 1);
                        y += tbl[i - k / 2 + 1][j + k / 2 - 1] * (k / 2 - 1);
                        y -= tbl[i + k / 2 - 1][j - k / 2 + 1] * (k / 2 - 1);
                        y += tbl[i + k / 2 - 1][j + k / 2 - 1] * (k / 2 - 1);
                    }
                    if (x == 0 && y == 0) {
                        //cerr << i << " " << j << endl;
                        ans = max(ans, k);
                    }
                }

                double xx = 0.0, yy = 0.0;
                double ii = 0.5 + i, jj = 0.5 + j;
                if (i + 1 > N || j + 1 > M) continue;
                xx += tbl[i][j] * (i - ii);
                xx += tbl[i + 1][j] * (i + 1 - ii);
                xx += tbl[i][j + 1] * (i - ii);
                xx += tbl[i + 1][j + 1] * (i + 1 - ii);
                yy += tbl[i][j] * (j - jj);
                yy += tbl[i + 1][j] * (j - jj);
                yy += tbl[i][j + 1] * (j + 1 - jj);
                yy += tbl[i + 1][j + 1] * (j + 1 - jj);
                for (k = 4; Valid_even(i, j, k); k += 2) {
                    int kk = k / 2 - 1;
                    for (int a = i - kk + 1; a <= i + kk; a++) {
                        xx += tbl[a][j + kk + 1] * (a - ii);
                        xx += tbl[a][j - kk] * (a - ii);
                    }
                    for (int b = j - kk + 1; b <= j + kk; b++) {
                        xx += tbl[i + kk + 1][b] * (i + kk + 1 - ii);
                        xx += tbl[i - kk][b] * (i - kk - ii);
                    }
                    for (int a = i - kk + 1; a <= i + kk; a++) {
                        yy += tbl[a][j + kk + 1] * (j + kk + 1 - jj);
                        yy += tbl[a][j - kk] * (j - kk - jj);
                    }
                    for (int b = j - kk + 1; b <= j + kk; b++) {
                        yy += tbl[i + kk + 1][b] * (b - jj);
                        yy += tbl[i - kk][b] * (b - jj);
                    }
                    if (k > 4) {
                        xx += tbl[i - kk + 1][j - kk + 1] * (i - kk + 1 - ii);
                        xx += tbl[i - kk + 1][j + kk] * (i - kk + 1 - ii);
                        xx += tbl[i + kk][j - kk + 1] * (i + kk - ii);
                        xx += tbl[i + kk][j + kk] * (i + kk - ii);
                        yy += tbl[i - kk + 1][j - kk + 1] * (j - kk + 1 - jj);
                        yy += tbl[i - kk + 1][j + kk] * (j + kk - jj);
                        yy += tbl[i + kk][j - kk + 1] * (j - kk + 1 - jj);
                        yy += tbl[i + kk][j + kk] * (j + kk - jj);
                    }
                    if (fabs(xx) < EPS && fabs(yy) < EPS) {
                        //cerr << i << " " << j << endl;
                        ans = max(ans, k);
                    }
                }
            }
        }
        if (ans == 0) printf("Case #%d: IMPOSSIBLE\n", casN);
        else printf("Case #%d: %d\n", casN, ans);
    }

    return 0;
}

