#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-10;
const double PI = acos(-1.0);
typedef long long int64;
#define MP(x, y) make_pair(x, y)
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x) * (x))
template<class T> T gcd(T a, T b) { for (T c; b; c = a, a = b, b = c % b); return a; }
template<class T> void out(const vector<T> &a) { for (int i = 0; i < SZ(a); ++i) cout << a[i] << " "; cout << endl; }
int countbit(int n) { return n == 0 ? 0 : 1 + countbit(n & (n - 1)); }
const int d8[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};
const int d4[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
typedef complex<double> point;
inline int dcmp(double x) { return (x > EPS) - (x < -EPS); }
inline double cross(const point &a, const point &b) { return (conj(a) * b).imag(); }
inline double dot(const point &a, const point &b) { return (conj(a) * b).real(); }

const int N = 500 + 10;
char s[N][N];
int a[N][N];
int sum[N][N], sum_x[N][N], sum_y[N][N];

bool check(int i, int j, int len)
{
    int all = sum[i + len][j + len] - sum[i][j + len] - sum[i + len][j] + sum[i][j];
    int all_x = sum_x[i + len][j + len] - sum_x[i][j + len] - sum_x[i + len][j] + sum_x[i][j];
    int all_y = sum_y[i + len][j + len] - sum_y[i][j + len] - sum_y[i + len][j] + sum_y[i][j];
    all -= a[i][j] + a[i + len - 1][j + len - 1] + a[i][j + len - 1] + a[i + len - 1][j];
    all_x -= a[i][j] * (i + 1) + a[i + len - 1][j + len - 1] * (i + len)
        + a[i][j + len - 1] * (i + 1) + a[i + len - 1][j] * (i + len);
    all_y -= a[i][j] * (j + 1) + a[i + len - 1][j + len - 1] * (j + len)
        + a[i][j + len - 1] * (j + len) + a[i + len - 1][j] * (j + 1);
    return all_x * 2 == (2 * i + len + 1) * all && all_y * 2 == (2 * j + len + 1) * all;
}

int run(int n, int m)
{
    for (int k = min(n, m); k >= 3; --k)
    {
        for (int i = 0; i + k <= n; ++i)
            for (int j = 0; j + k <= m; ++j)
                if (check(i, j, k)) return k;
    }
    return 2;
}

int main()
{
    freopen("B-large.in", "r", stdin); freopen("B.out", "w", stdout);
    // freopen("test.in", "r", stdin);
    int cas;
    scanf("%d", &cas);
    for (int num = 1; num <= cas; ++num)
    {
        int n, m, D;
        scanf("%d %d %d", &n, &m, &D);
        for (int i = 0; i < n; ++i)
            scanf("%s", s[i]);
        memset(sum, 0, sizeof(sum));
        memset(sum_x, 0, sizeof(sum_x));
        memset(sum_y, 0, sizeof(sum_y));
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= m; ++j)
            {
                int v = s[i - 1][j - 1] - '0';
                a[i - 1][j - 1] = v;
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + v;
                sum_x[i][j] = sum_x[i - 1][j] + sum_x[i][j - 1] - sum_x[i - 1][j - 1] + v * i;
                sum_y[i][j] = sum_y[i - 1][j] + sum_y[i][j - 1] - sum_y[i - 1][j - 1] + v * j;
            }
        int ret = run(n, m);
        printf("Case #%d: ", num);
        if (ret >= 3) printf("%d\n", ret);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
