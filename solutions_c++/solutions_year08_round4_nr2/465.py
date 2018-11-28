
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
int X, Y, A, x2, y2, x3, y3;

int solve()
{
    if ( A / 2 > X * Y ) return 0;
    x2 = y2 = 0;
    REP(x2, X + 1) REP(y2, Y + 1) 
        REP(x3, x2 + 1) REP(y3, Y + 1)
            if ( abs(x2 * y3 - x3 * y2) == A ) return 1;
    return 0;
}

int main()
{
    int cT, t;

    freopen("c:/temp/gcj/r2/b/1.out", "w", stdout);    
    freopen("c:/temp/gcj/r2/b/1.in", "r", stdin);
    scanf("%d", &cT);
    REP(t, cT)
    {
        scanf("%d %d %d", &X, &Y, &A);
        if ( solve() )
            printf("Case #%d: %d %d %d %d %d %d\n", t + 1, 0, 0, x2, y2, x3, y3);
        else
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
        if ( t % 10 == 0 ) fprintf(stderr, "%d\n", t);
    }
    fclose(stdout);
    return 0;
}
