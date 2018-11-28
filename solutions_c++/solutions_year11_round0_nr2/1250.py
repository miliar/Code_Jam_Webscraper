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

const int N = 26;
int g[N][N];
bool h[N][N];
char str[1000];
int ret[1000];

int main()
{
    freopen("B-large.in", "r", stdin); freopen("B.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int num = 1; num <= cas; ++num)
    {
        int C, D;
        scanf("%d", &C);
        memset(g, 255, sizeof(g));
        while (C--)
        {
            scanf("%s", str);
            int x = str[0] - 'A';
            int y = str[1] - 'A';
            int z = str[2] - 'A';
            g[y][x] = g[x][y] = z;
        }
        scanf("%d", &D);
        memset(h, 0, sizeof(h));
        while (D--)
        {
            scanf("%s", str);
            int x = str[0] - 'A';
            int y = str[1] - 'A';
            h[y][x] = h[x][y] = true;
        }
        int n;
        scanf("%d %s", &n, str);
        n = 0;
        for (int i = 0; str[i]; ++i)
        {
            int x = str[i] - 'A';
            if (n > 0 && g[ret[n - 1]][x] >= 0)
                ret[n - 1] = g[ret[n - 1]][x];
            else
            {
                bool found = false;
                for (int j = 0; j < n; ++j)
                    if (h[ret[j]][x]) found = true;
                if (found) n = 0;
                else ret[n++] = x;
            }
        }
        printf("Case #%d: [", num);
        for (int i = 0; i < n; ++i)
        {
            if (i > 0) printf(", ");
            printf("%c", (char)('A' + ret[i]));
        }
        puts("]");
    }
    return 0;
}
