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

typedef long long LL;
typedef long double LD;
/*---------------------------------------------------------*/
#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAX 128
#define MOD 10007

int n, m, r;
int b[MAX][MAX];
int P[MAX][MAX];

int solve()
{
    int i, j, x, y;
    scanf("%d%d%d", &n, &m, &r);
    memset(b, 0, sizeof(b));
    memset(P, 0, sizeof(P));
    for (i=0; i<r; i++)
    {
        scanf("%d%d", &x, &y);
        b[x-1][y-1] = 1;
    }

    P[0][0] = 1;
    REP(i, n)
    {
        REP(j, m)
        {
            if (P[i][j] > 0)
            {
                if (!b[i+1][j+2])
                    P[i+1][j+2] = (P[i+1][j+2] + P[i][j]) % MOD;
                if (!b[i+2][j+1])
                    P[i+2][j+1] = (P[i+2][j+1] + P[i][j]) % MOD;
            }
        }
    }
    return P[n-1][m-1];
}

int main()
{
    int cT, t, i;

    freopen("c:/temp/gcj/r3/d/1.out", "w", stdout); 
    freopen("c:/temp/gcj/r3/d/1.in", "r", stdin);
    scanf("%d", &cT);
    REP(t, cT)
    {
        printf("Case #%d: %d\n", i, solve());        
    }
    fclose(stdout);
    return 0;
}