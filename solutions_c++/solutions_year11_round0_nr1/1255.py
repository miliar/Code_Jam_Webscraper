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

const int N = 100;
int a[N], b[N];

int main()
{
    freopen("A-large.in", "r", stdin); freopen("A.out", "w", stdout);
    int cas;
    scanf("%d", &cas);

    for (int num = 1; num <= cas; ++num)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            char str[10];
            scanf("%s %d", str, b + i);
            a[i] = (str[0] == 'O');
        }
        int pos[2];
        pos[0] = pos[1] = 1;
        int turn = 0;
        int ret = 0;
        for (int i = 0, j; i < n; i = j)
        {
            for (j = i + 1; j < n && a[j] == a[i]; ++j);
            int cnt = 0;
            for (int k = i; k < j; ++k)
            {
                cnt += abs(pos[turn] - b[k]) + 1;
                pos[turn] = b[k];
            }
            ret += cnt;
            turn = 1 - turn;
            if (j < n)
            {
                if (b[j] > pos[turn]) pos[turn] += min(cnt, b[j] - pos[turn]);
                else pos[turn] -= min(cnt, pos[turn] - b[j]);
            }
        }
        printf("Case #%d: %d\n", num, ret);
    }
    return 0;
}
