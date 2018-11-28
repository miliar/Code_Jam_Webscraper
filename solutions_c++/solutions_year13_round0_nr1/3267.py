
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <bitset>
#include <functional>
#include <map>

#define LL(a) (a<<1)
#define RR(a) (a<<1|1)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define FOE(i,a,b) for(i=a;i<=b;i++)
#define FOD(i,a,b) for(i=a;i>=b;i--)
#define foreach(it,v) for (__typeof((v).begin()) it = (v).begin();it != (v).end();++it)
#define iter(c) __typeof((c).begin())
#define Clr(a,b) memset(a,b,sizeof(a))
#define Cpy(a,b) memcpy(a,b,sizeof(a))
#define TTI template <class T> inline
#define MP(a,b) make_pair(a,b)
#define fi first
#define se second

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<double,int> pdi;
typedef pair<int,double> pid;

const double eps = 1e-8;
const double pi  = acos(-1.0);
const double inf = 1e20;
const int INF = (~0u)>>2;
const i64 INF64 = (~0uLL)>>2;

inline bool eq(double x, double y) { return (x-y<-eps)?0:x-y<eps; }
TTI T sqr(T x) { return x * x; }
TTI T gcd(T a, T b) { return (b)?gcd(b, a%b): a; }
u64 rand64(){
	return u64(rand()) ^ (u64(rand())<<15) ^ (u64(rand())<<30) ^ (u64(rand())<<45) ^ (u64(rand())<<60);
}
inline bool isAlphabet(char a) {
    return ('a' <= a && a <= 'z') || ('A' <= a && a <= 'Z');
}
inline bool isDigit(char a) {
    return '0' <= a && a <= '9';
}

char mm[4][4];
char ans[100];

void solve()
{
    for(int i=0; i<4; i++)
    {
        bool iso = true;
        for(int j=0; j<4; j++)
            if(mm[i][j] == 'X' || mm[i][j] == '.')
            {
                iso = false;
                break;
            }
        if(iso)
        {
            strcpy(ans, "O won");
            return;
        }

        bool isx = true;
        for(int j=0; j<4; j++)
            if(mm[i][j] == 'O' || mm[i][j] == '.')
            {
                isx = false;
                break;
            }
        if(isx)
        {
            strcpy(ans, "X won");
            return;
        }
    }

    for(int i=0; i<4; i++)
    {
        bool iso = true;
        for(int j=0; j<4; j++)
            if(mm[j][i] == 'X' || mm[j][i] == '.')
            {
                iso = false;
                break;
            }
        if(iso)
        {
            strcpy(ans, "O won");
            return;
        }

        bool isx = true;
        for(int j=0; j<4; j++)
            if(mm[j][i] == 'O' || mm[j][i] == '.')
            {
                isx = false;
                break;
            }
        if(isx)
        {
            strcpy(ans, "X won");
            return;
        }
    }

    bool iso = true, isx = true;
    for(int i=0, j=0; i<4; i++, j++)
    {
        if(mm[i][j] == 'X' || mm[i][j] == '.')
            iso = false;
        if(mm[i][j] == 'O' || mm[i][j] == '.')
            isx = false;
    }
    if(iso)
    {
        strcpy(ans, "O won");
        return;
    }
    if(isx)
    {
        strcpy(ans, "X won");
        return;
    }

    iso = true, isx = true;
    for(int i=0, j=3; i<4; i++, j--)
    {
        if(mm[i][j] == 'X' || mm[i][j] == '.')
            iso = false;
        if(mm[i][j] == 'O' || mm[i][j] == '.')
            isx = false;
    }
    if(iso)
    {
        strcpy(ans, "O won");
        return;
    }
    if(isx)
    {
        strcpy(ans, "X won");
        return;
    }

    bool isdraw = true;
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            if(mm[i][j] == '.')
                goto out;

    strcpy(ans, "Draw");
    return;

    out:strcpy(ans, "Game has not completed");
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas)
    {
        for(int i=0; i<4; i++)
            scanf("%s", mm[i]);
        solve();
        printf("Case #%d: %s\n", cas, ans);
    }

    return 0;
}
