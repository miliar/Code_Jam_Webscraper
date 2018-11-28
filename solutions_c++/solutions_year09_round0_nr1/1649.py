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

const int maxn = 6005;
const int maxm = 5005;
const int maxLen = 17;
const double EPS = 1e-10;
const double PI = acos(-1.0);
const int INT_INF = INT_MAX / 2;
const int64 INT64_INF = 1LL << 61;

int n, m;
int L;
char ss[1000];
string word[maxn];
int sen[maxm][maxLen];
int pos[maxm]; // 记录该字符串与前一个字符串第一个不同的字符的位置.
int ans;

void Debug(void)
{
    int i, j;
    for (i = 0; i < n; i++) cout << word[i] << endl;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < L; j++)
        {
            cout << sen[i][j] << " ";
        }
        cout << endl;
    }
    for (i = 0; i < n; i++) cout << "pos : " << pos[i] << endl;
}

void Init(void)
{
    int i, j, k;
    int temp;
    mem(sen, 0);

    for (i = 0; i < m; i++)
    {
        scanf("%s", ss); k = 0;
        for (j = 0; ss[j]; j++)
        {
            if (ss[j] == '(')
            {
                temp = 0; j++;
                while (ss[j] != ')')
                {
                    temp |= 1 << (ss[j] - 'a');
                    j++;
                }
            }
            else temp = 1 << (ss[j] - 'a');
            sen[i][k++] = temp;
        }
    }

    pos[i] = 0;
    for (i = 1; i < n; i++)
    {
        for (j = 0; j < L; j++)
        {
            if (word[i][j] != word[i - 1][j]) break;
        }
        pos[i] = j;
    }
}

void Solve(void)
{
    int i, j, k(0);
    int v;
    int case_num(0);
    for (i = 0; i < m; i++)
    {
        ans = 0;
        printf("Case #%d: ", ++case_num);
        for (j = 0; j < n; j++)
        {
            k = Min(k, pos[j]);
//            cout << j << " " << pos[j] << " " << k << endl;
            for ( ; k < L; k++)
            {
                v = 1 << (word[j][k] - 'a');
                if (!(v & sen[i][k])) break;
            }
            if (k >= L)
            {
                ans++;
//                cout << word[j] << endl;
            }
        }
        printf("%d\n", ans);
    }
}

int main(void)
{
    freopen("Input.txt", "r", stdin);
    freopen("Output.txt", "w", stdout);
    int i, j;
    char st[20];
    scanf("%d %d %d", &L, &n, &m);
    for (i = 0; i < n; i++)
    {
        scanf("%s", st);
        word[i] = (string)(st);
    }
    sort(word, word + n);
    Init();
    Solve();
//    Debug();
    return 0;
}
