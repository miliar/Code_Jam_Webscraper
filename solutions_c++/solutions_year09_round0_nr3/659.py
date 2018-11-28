#include <stdlib.h>
#include <stdio.h>
#include <math.h>
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
#define FOR(i,a,b) for ( int i = (a); i <= (b); ++i )
#define REP(i,N) for ( int i = 0; i < N; ++i )
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
const int maxn = 523;
int n, pn;
const char pat[] =
//"a";
"welcome to code jam";
char s[maxn];

void read()
{
    gets(s);
    n = strlen(s);
    pn = strlen(pat);
}

const int MOD = 10000;
int dp[maxn][52];

void solve()
{
    CL(dp, 0);
    REP(i, 1) dp[i][0] = 1;
    REP(i, n) REP(j, pn) FOR(k, i+1, n)
        if (s[k - 1] == pat[j])
        {
            dp[k][j + 1] += dp[i][j];
            dp[k][j + 1] %= MOD;
        }
    int res = 0;
    REP(i, n + 1) res += dp[i][pn];
    n = res % MOD;
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
        printf("%.4d\n", n);
    }
    return 0;
}

