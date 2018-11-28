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

const int maxn = 305;
const int maxm = 1 << 12;

int n, m;
char st[maxn];
int Index[maxn];
int a[maxn];
int64 ans;

void Debug(void)
{
    int i, j;
}

void Init(void)
{
    int i, j;
    for (i = 0; i < maxn; i++) Index[i] = -1;
    ans = 0;
}

void Solve(void)
{
    int i, j;
    int m(0);
    Index[st[0]] = 1; a[0] = Index[st[0]]; n = 1;
    for (i = 1; st[i]; i++)
    {
        if (Index[st[i]] == -1)
        {
            Index[st[i]] = m++;
            if (m == 1) m++;
        }
        a[n++] = Index[st[i]];
    }
//    out(a, n);
    if (m == 0) m = 2;
    for (i = 0; i < n; i++) ans = ans * m + a[i];
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
        scanf("%s", st);
        Init();
        Solve();
        cout << "Case #" << ++case_num << ": " << ans << endl;
//        Debug();
    }
    return 0;
}
