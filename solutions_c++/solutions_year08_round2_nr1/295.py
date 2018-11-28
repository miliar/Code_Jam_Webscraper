
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

struct Vec
{
    int x, y;
};
/*---------------------------------------------------------*/
Vec P[123456];
LL r[3][3];
int n;


LL solve()
{
    int i, rx, ry;

//    REP(i, n) printf("%d %d\n", P[i].x, P[i].y);
    CL(r, 0);
    REP(i, n) ++r[P[i].x % 3][P[i].y % 3];

    LL res = 0, p;
    REP(rx, 3) REP(ry, 3)
    {
        p = r[rx][ry];
        res += p * (p - 1) * (p - 2) / 6;
    }

    REP(rx, 3)
        res += r[rx][0] * r[rx][1] * r[rx][2];

    REP(ry, 3)
        res += r[0][ry] * r[1][ry] * r[2][ry];
    
    int perm[3];
    REP(i, 3) perm[i] = i;
    while ( 1 ) 
    {
        res += r[0][perm[0]] * r[1][perm[1]] * r[2][perm[2]];
        if ( !next_permutation(perm, perm + 3) ) break;
    }

    return res;
}

int main()
{
    LL A, B, C, D, x, y, x1, y1, M;
    int cT, t, i;

    freopen("c:/temp/gcj/r1/a/1.out", "w", stdout);    
    freopen("c:/temp/gcj/r1/a/1.in", "r", stdin);    
    scanf("%d", &cT);
    REP(t, cT)
    {
        scanf("%d %I64d %I64d %I64d %I64d %I64d %I64d %I64d", &n, &A, &B, &C, &D, &x, &y, &M);
        REP(i, n)
        {
            P[i].x = x;
            P[i].y = y;
            x1 = (A * x + B) % M;
            y1 = (C * y + D) % M;
            x = x1;
            y = y1;
        }
        LL res = solve();
        printf("Case %d: %d\n", t + 1, res);
    }
    fclose(stdout);
    return 0;
}
