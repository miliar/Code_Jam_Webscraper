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
#define INF 12345678
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
const int MAXN = 123456; 
int m, v, g[MAXN], c[MAXN], a[MAXN], P[2][MAXN];

int go(int d, int i)
{
    if(i > m)return INF;
    if(P[d][i] != -1) return P[d][i];

    int res = INF;
    int a0 = go(0, i*2);
    int b0 = go(0, i*2+1);
    int a1 = go(1, i*2);
    int b1 = go(1, i*2+1);

    if(g[i] == 1)
    {
        if ( d )
        {
            res = min(res, a1+b1);
            if(c[i] == 1)
                res = min(res, min(a0+b1+1,a1+b0+1));
        }
        else
            res = min(res, min(a1+b0, min(a0+b0, a0+b1)));
    }
    else
    {
        if ( !d )
        {
            res = min(res, a0+b0);
            if(c[i] == 1)
                res = min(res, min(a1+b0+1, a0+b1+1));
        }            
        else
            res = min(res, min(a1+b1, min(a1+b0, a0+b1)));
    }    
    return P[d][i] = res;
}

int solve()
{
    int i;
    FOR(i,1,(m-1)/2)
        P[0][i] = P[1][i] = -1;
    FOR(i,(m-1)/2+1,m*2)
    {
        P[0][i] = P[1][i] = INF;
        P[a[i]][i] = 0;
    }
    int res = go(v, 1);
    return res >= INF ? -1 : res;
}

int main()
{
    int cT, t, i;

    freopen("c:/temp/gcj/r2/a/1.out", "w", stdout); 
    freopen("c:/temp/gcj/r2/a/1.in", "r", stdin);
    scanf("%d", &cT);
    REP(t, cT)
    {
        scanf("%d%d", &m, &v);
        FOR(i,1,(m-1)/2) scanf("%d%d", &g[i], &c[i]);            
        FOR(i,(m-1)/2+1,m) scanf("%d", &a[i]);

        int res = solve();        
        if ( res >= 0 )
            printf("Case #%d: %d\n", t + 1, res);
        else
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
    }
    fclose(stdout);
    return 0;
}
