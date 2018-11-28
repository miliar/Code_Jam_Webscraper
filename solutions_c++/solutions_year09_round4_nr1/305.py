#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/*---------------------------------------------------------*/
#define INF 123456789
#define SI(a) ((int)(a).size())
#define ALL(a) a.begin(),a.end()
#define CL(a,v) memset(a, v, sizeof(a))
#define FOR(i,a,b) for ( int i = (a); i <= (b); ++i )
#define REP(i,n) for ( int i = 0; i < (n); ++i )
#define IT(T,a,i) for ( T::iterator i = (a).begin(); i != (a).end(); ++i )
#define BIT(mask,i) (!!((mask) & (1 << (i))))
/*---------------------------------------------------------*/
int lowbit(int set) { return (set^(set-1))&set; }
int countbit(int set) { return (set==0)?0:(1+countbit(set-lowbit(set))); }
/*---------------------------------------------------------*/
template<class T> void print(vector<T> A,int n=-1){if(n==-1||n>SI(A))n=SI(A);cerr<<"VEC "<<n<<" {";REP(i,n)cerr<<A[i]<<" ";cerr<<"}"<<endl;}
template<class T> void print(T A[],int n){cerr<<"ARR "<<n<<"{";REP(i,n)cerr<<A[i]<<" ";cerr<<"}"<<endl;}
/*---------------------------------------------------------*/
typedef vector<int> VI;
typedef vector<string> VS;
typedef double LD;
typedef long long LL;
typedef pair<int, int> TP;

const LD PI = 2.0 * acos(0.0);
const LD EPS = 1e-10;
/*---------------------------------------------------------*/
VS split(const char* s, const char* del = " ")
{
    VS res;
    const char* beg = 0, *p;
    for(p = s; *p; ++p)
        if (strchr(del, *p))
        {
            if (beg) res.push_back(string(beg, p - beg));
            beg = 0;
        }
        else
            if (!beg) beg = p;
    if (beg) res.push_back(string(beg, p - beg));
    return res;
}

template<typename T, typename S> T cast(S s)
{
    stringstream ss;
    ss << s;
    T res;
    ss >> res;
    return res;
}

/*---------------------------------------------------------*/
template<typename T> T sqr(T a) { return a * a; }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
/*---------------------------------------------------------*/
const int maxn = 12345678;
char buf[123456];
int n;
int res;
int a[1234];

void read()
{
    scanf("%d\n", &n);
    REP(i,n)
    {
        scanf("%s\n", buf);
        a[i] = n - 1;
        while (a[i] > 0 && buf[a[i]] == '0') --a[i];
    }
}

void solve()
{
//    print(a,n);
    res = 0;
    REP(i,n) if(a[i] > i)
    {
        int j = i + 1;
        while(a[j] > i) ++j;
        while(j>i)
        {
            swap(a[j],a[j-1]);
            --j;
            ++res;
        }
    }
}

int main()
{
    int ct;
    scanf("%d\n", &ct);
    for (int t = 1; t <= ct; ++t)
    {
        read();
        solve();
        printf("Case #%d: ", t);
        printf("%d\n", res);
    }
    return 0;
}


