#include <iostream>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>
#include <iomanip>
#include <map>
#include <memory.h>
using namespace std;

typedef long long int64; // 2 ^ 63 - 1 = 9223372036854775807.
typedef unsigned long long uint64; // 2 ^ 64 - 1 = 18446744073709551615.
const double EPS = 1e-10;
const double PI = acos(-1.0);
const int INT_INF = INT_MAX / 2;
const int64 INT64_INF = 1LL << 61;
#define mem(a, b) memset(a, b, sizeof(a))
#define Sqr(x) ((x) * (x))
template <class T> inline T Max(T a, T b) { if (a < b) a = b; return a; }
template <class T> inline T Min(T a, T b) { if (a > b) a = b; return a; }
template <class T> inline void Swap(T & a, T & b) { T t = a; a = b; b = t; }
inline int64 MOD(int64 x, int64 y) { return x - (floor)(1.0 * x / y + EPS) * y; }
inline int mod(int a, int b) { a %= b; return a < 0 ? a + b : a; }
inline int sgn(const double & a)
{ // 返回1表示大于0，0表示等于0，-1表示小于0.
    return (a > EPS) - (a < -EPS);
}

template <class T> void out(T x, int n) { for(int i = 0; i < n; ++i) cout << x[i] << ' '; cout << endl; }
template <class T> void out(T x, int n, int m) {  for(int i = 0; i < n; ++i) out(x[i], m); cout << endl; }
#define Out(x) (cout << #x << " = " << x << " ")
#define Outendl(x) (cout << #x << " = " << x << endl)

const int MAXN = 10005;
const int MAXM = 1 << 12;

int n, k;

int main(void)
{
//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
    int i, j;
    int cases;
    int case_num(0);
    scanf("%d", &cases);
    while (cases--)
    {
        scanf("%d %d", &n, &k);
        if (k % (1 << n) == (1 << n) - 1) printf("Case #%d: ON\n", ++case_num);
        else printf("Case #%d: OFF\n", ++case_num);
    }
    return 0;
}
