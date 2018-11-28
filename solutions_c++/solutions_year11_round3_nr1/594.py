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
const double EPS = 1e-8;
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

char a[100][100];
int r,c;
void init()
{
    cin>>r>>c;
    for(int i=0;i<r;i++)
    {
        cin>>a[i];
    }

}
bool hefa(int i,int j)
{
    if(i>=r||j>=c)return false;
    if(a[i][j]!='#')return false;
    return true;
}
bool get()
{
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            if(a[i][j]=='#')
            {
                a[i][j]='/';
                if(!hefa(i+1,j))
                return false;
                else a[i+1][j]='\\';

                if(!hefa(i,j+1))
                return false;
                else a[i][j+1]='\\';

                if(!hefa(i+1,j+1))
                return false;
                else a[i+1][j+1]='/';
            }
        }
    }
    return true;
}
void print()
{
    for(int i=0;i<r;i++)
    printf("%s\n", a[i]);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    scanf("%d", &t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d:\n", i);
        init();
        if(!get())
        {
            printf("Impossible\n");
        }
        else print();
    }
    return 0;
}
