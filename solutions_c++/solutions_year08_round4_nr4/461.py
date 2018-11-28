
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
int k;
char s[1234567], s1[1234567];

int solve()
{
    int P[23], i, n = strlen(s), j;
    REP(i, k) P[i] = i;
    s1[n] = 0;
    int m, res = n;
    while ( 1 )
    {
        REP(i, n/k)
            REP(j, k) s1[i * k + j] = s[i * k + P[j]];
        m = unique(s1, s1 + n) - s1;
        res = min(res, m);
        if ( !next_permutation(P, P + k) ) break;
    }
    return res;
}

int main()
{
    int cT, t, n, i;

    freopen("c:/temp/gcj/r2/d/1.out", "w", stdout);    
    freopen("c:/temp/gcj/r2/d/1.in", "r", stdin);
    scanf("%d", &cT);
    REP(t, cT)
    {
        scanf("%d\n%s", &k, &s);
        int res = solve();
        printf("Case #%d: %d\n", t + 1, res);
    }
    fclose(stdout);
    return 0;
}
