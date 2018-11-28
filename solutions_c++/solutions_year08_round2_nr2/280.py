
#pragma warning (disable:4786)
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/*---------------------------------------------------------*/
#define INF 123456789
#define SI(A) ((int)(A).size())
#define ALL(A) A.begin(),A.end()
#define CL(A,v) memset(A, v, sizeof(A))
#define FOR(i,a,b) for ( i = (a); i <= (b); ++i )
#define IFOR(i,a,b) for ( i = (a); i >= (b); --i )
#define REP(i,N) for ( i = 0; i < N; ++i )
#define IREP(i,N) for ( i = N - 1; i >= 0; --i )
#define IT(T,A,i) for ( T::iterator i = (A).begin(); i != (A).end(); ++i )
#define BIT(mask,i) ((mask) & (1 << (i)))
/*---------------------------------------------------------*/
int lowbit(int set) { return (set^(set-1))&set; }
int countbit(int set) { return (set==0)?0:(1+countbit(set-lowbit(set))); }
/*---------------------------------------------------------*/
template<class T> void print(vector<T> A,int n=-1){if(n==-1||n>A.size())n=A.size();cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<" ";cout<<"}"<<endl;}
template<class T> void print(T A[],int n){cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<" ";cout<<"}"<<endl;}
/*---------------------------------------------------------*/
typedef vector<int> VI;
typedef vector<string> VS;
typedef double LD;

typedef long long LL;
/*---------------------------------------------------------*/
LL a, b, p;
int m[1234567];
int pr[1234567], cPr;
char s[1234567];

void buildPrime(int* p, int& cP, int n)
{
    CL(s, 1);
    int i, j;
    FOR(i, 2, n)
        if ( s[i] )
            for ( j = i + i; j <= n; j += i ) s[j] = 0;
    cP = 0;
    FOR(i, 2, n) if ( s[i] ) p[cP++] = i;
  //  REP(i, 23) printf("%d ", pr[i]);
}

LL gcd(LL a, LL b)
{
    return a ? gcd(b % a, a) : b;
}

int same(int a, int b)
{
    //LL d = gcd(a, b);
    //if ( d < p ) return 0;

    int i = 0, m = min(a, b);
    while ( pr[i] < p ) ++i;
    for ( ; i < cPr && pr[i] <= a && pr[i] <= b; ++i )
        if ( a % pr[i] == 0 && b % pr[i] == 0 )
        {
            if ( pr[i] >= p ) return 1;          
        }
    return 0;
}

int g[1234][1234];

void dfs(int v)
{
    if ( m[v] ) return;
    m[v] = 1;
    int i;
    FOR(i, a, b) if ( g[v][i] ) dfs(i);
}

LL solve()
{
    
    CL(g, 0);
    int mark = 0, i, j;    
    FOR(i, a, b) 
        FOR(j, a, i - 1)
            if ( same(i, j) ) 
                g[i][j] = g[j][i] = 1;                                
    
    CL(m, 0);
    FOR(i, a, b) if ( !m[i] )
    {
        ++mark;
        dfs(i);
    }
    return mark;
}

int main()
{
    int cT, t;

    buildPrime(pr, cPr, 1234);
    freopen("c:/temp/gcj/r1/b/1.out", "w", stdout);    
    freopen("c:/temp/gcj/r1/b/1.in", "r", stdin);    
    scanf("%d", &cT);
    REP(t, cT)
    {
        scanf("%I64d %I64d %I64d", &a, &b, &p);
        LL res = solve();
        printf("Case #%d: %I64d\n", t + 1, res);
    }
    fclose(stdout);
    return 0;
}
