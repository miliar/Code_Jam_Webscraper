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

const int N = 1000;
int a[N];
double D[N + 1];
double A[N + 1];
double F[N + 1];
double C[N + 1][N + 1];
bool flag[N];

int main()
{
    freopen("D-small-attempt1.in", "r", stdin); freopen("D.out", "w", stdout);
    for (int i = 0; i <= N; ++i)
    {
        C[i][0] = C[i][i] = 1.0;
        for (int j = 1; j < i; ++j)
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
    }
    F[0] = 1.0;
    for (int i = 1; i <= N; ++i) F[i] = F[i - 1] * i;
    D[1] = 0.0;
    for (int i = 2; i <= N; ++i)
    {
        D[i] = F[i] - 1;
        for (int j = 1; j <= i - 2; ++j)
            D[i] -= C[i][j] * D[i - j];
    }
    A[1] = 0.0;
    for (int i = 2; i <= N; ++i)
    {
        double sum = 1.0;
        for (int j = 1; j <= i - 2; ++j)
            sum += D[i - j] * C[i][j] * (1 + A[i - j]);
        sum += D[i];
        A[i] = sum / (F[i] - D[i]);
    }
    int cas;
    scanf("%d", &cas);
    for (int num = 1; num <= cas; ++num)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%d", a + i), --a[i];
        memset(flag, 0, sizeof(flag));
        double ret = 0.0;
        for (int i = 0; i < n; ++i)
        {
            if (flag[i]) continue;
            int cnt = 0;
            for (int j = i; ;)
            {
                flag[j] = true;
                j = a[j];
                ++cnt;
                if (j == i) break;
            }
            ret += A[cnt];
        }
        printf("Case #%d: %.6f\n", num, ret);
    }
    return 0;
}
