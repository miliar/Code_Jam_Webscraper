#include <iostream>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>
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
inline int64 mod(int64 x, int64 y) { return x - floor(1.0 * x / y + EPS) * y; }

template <class T> void out(T x, int n) { for(int i = 0; i < n; ++i) cout << x[i] << ' '; cout << endl; }
template <class T> void out(T x, int n, int m) {  for(int i = 0; i < n; ++i) out(x[i], m); cout << endl; }
#define Out(x) (cout << #x << " = " << x << endl)

const int maxn = 105;
const int maxm = 1 << 12;

int n, m;
int arr[maxn];
int f[maxn][maxn]; // f[i][j]表示删除[i + 1, j - 1]之间的人的最优解.
int64 ans;

void Debug(void)
{
    int i, j;
}

void Init(void)
{
    int i, j;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            f[i][j] = INT_INF;
        }
    }
    ans = 0;
}

void Calc(int a, int b)
{
    int i;
    if (a + 1 == b)
    {
        f[a][b] = 0;
        return ;
    }
    for (i = a + 1; i <= b - 1; i++)
    { // 删除第i个人.
        if (f[a][i] == INT_INF) Calc(a, i);
        if (f[i][b] == INT_INF) Calc(i, b);
        f[a][b] = Min(f[a][b], f[a][i] + f[i][b] + arr[b] - arr[a] - 2);
    }
//    cout << a << " " << b << " " << f[a][b] << endl;
}

int main(void)
{
    freopen("Input.txt", "r", stdin);
    freopen("Output.txt", "w", stdout);
    int i, j;
    int cases;
    int case_num(0);
    scanf("%d", &cases);
    while (cases--)
    {
        scanf("%d %d", &m, &n);
        for (i = 2; i <= n + 1; i++) scanf("%d", &arr[i]);
        arr[1] = 0, arr[n + 2] = m + 1; n += 2;
        sort(arr + 1, arr + n + 1);
        if (n == 3)
        {
            printf("Case #%d: %d\n", ++case_num, m - 1);
            continue;
        }
        Init();
        Calc(1, n);
        printf("Case #%d: %d\n", ++case_num, f[1][n]);
//        Debug();
    }
    return 0;
}
