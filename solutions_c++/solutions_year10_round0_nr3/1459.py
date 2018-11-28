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

const int MAXN = 1005;
const int MAXM = 1 << 12;

int R, K;
int n, m;
int a[MAXN];
bool visited[MAXN];
bool iscycle[MAXN];
int64 cycle, times;
int64 ans;

void Calc(int t)
{
    int i, j, k;
    cycle = times = 0;
    for (i = 0; i < n; ++i) iscycle[i] = 0;
    iscycle[t] = 1;
    i = t;
    while (1)
    {
        for (j = 0; j < n; ++j) visited[j] = 0;
        k = K;
        while (1)
        {
            if (visited[i] || k - a[i] < 0) break;
            visited[i] = 1;
            k -= a[i];
            cycle += a[i];
            i = (i + 1) % n;
        }
        times++;
//        cout << i << endl;
        if (!iscycle[i]) iscycle[i] = 1;
        else break;
    }
//    cout << cycle << " " << times << " " << i << endl;
//    cout << R << endl;
    ans += cycle * (R / times);
    R %= times;
    i = t;
    while (R)
    {
//        cout << R << endl;
        for (j = 0; j < n; ++j) visited[j] = 0;
        k = K;
        while (1)
        {
            if (visited[i] || k - a[i] < 0) break;
            visited[i] = 1;
            k -= a[i];
            ans += a[i];
            i = (i + 1) % n;
        }
        R--;
    }
}

void Solve(void)
{
    int i, j, k;
    for (i = 0; i < n; ++i) iscycle[i] = 0;
    iscycle[0] = 1;
    ans = 0;
    i = 0;
    while (R)
    {
        for (j = 0; j < n; ++j) visited[j] = 0;
        k = K;
        while (1)
        {
            if (visited[i] || k - a[i] < 0) break;
            visited[i] = 1;
            k -= a[i];
            ans += a[i];
            i = (i + 1) % n;
        }
        R--;
//        cout << ans << endl;
        if (!iscycle[i]) iscycle[i] = 1;
        else
        {
            Calc(i);
            break;
        }
    }
}

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
        scanf("%d %d %d", &R, &K, &n);
        for (i = 0; i < n; ++i) scanf("%d", a + i);
        Solve();
        cout << "Case #" << ++case_num << ": " << ans << endl;
//        printf("Case #%d: %d\n", ++case_num, ans);
    }
    return 0;
}
