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
#define mem(a, b) memset(a, b, sizeof(a))
#define Sqr(x) ((x) * (x))
template <class T>
inline T Max(T a, T b) { if (a < b) a = b; return a; }
template <class T>
inline T Min(T a, T b) { if (a > b) a = b; return a; }
template <class T>
inline void Swap(T & a, T & b) { T t = a; a = b; b = t; }
inline int64 mod(int64 x, int64 y) { return x - floor(1.0 * x / y) * y; }

const int maxn = 505;
const int maxm = 22;
const double EPS = 1e-10;
const double PI = acos(-1.0);
const int INT_INF = INT_MAX / 2;
const int64 INT64_INF = 1LL << 61;
const int MOD = 10000;

const char sen[maxm] = "welcome to code jam";

int n, m;
char st[maxn];
int len;
int f[maxn][maxm];
int64 ans;

void Debug(void)
{
    int i, j;
}

void Init(void)
{
    int i, j;
    ans = 0; m = 19;
    mem(f, 0);
}

void Solve(void)
{
    int i, j, k;
    int temp;
    for (i = 0; i < len; i++)
    {
        for (j = 0; j < m; j++)
        {
            if (st[i] != sen[j]) continue;
            if (j == 0)
            {
                f[i][j] = 1;
                continue;
            }
            temp = 0;
            for (k = i - 1; k >= 0; k--)
            {
                if (st[k] == sen[j - 1])
                {
                    temp = (temp + f[k][j - 1]) % MOD;
                }
            }
            f[i][j] = temp;
        }
    }
}

int main(void)
{
    freopen("Input.txt", "r", stdin);
    freopen("Output.txt", "w", stdout);
    int i, j;
    int cases;
    int case_num(0);
    scanf("%d", &cases); gets(st);
    while (cases--)
    {
        gets(st);
        len = strlen(st);
//        cout << st << endl;
        Init();
        Solve();
        for (i = 0; i < len; i++)
        {
            ans += f[i][m - 1];
        }
        printf("Case #%d: %04d\n", ++case_num, ans);
//        Debug();
    }
    return 0;
}
