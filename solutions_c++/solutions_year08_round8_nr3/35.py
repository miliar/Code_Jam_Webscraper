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
typedef pair<int, int> TP;
typedef unsigned char ui8;
/*---------------------------------------------------------*/
const LL MOD = 1000000009;

int g[1234][1234], n, K;

LL go(int k, int a, int p)
{	
	int i, c = 0;
	FOR(i, 1, n)
		if ( i != p && g[a][i] )
			++c;
	if ( c > k ) return 0;
	int m = K - c - (p > 0);
	if ( m < 0 ) return 0;

	//fprintf(stderr, "go: %d %d %d\n", k, a, p);
	LL res = 1;
	FOR(i, 1, n)
		if ( i != p && g[a][i] )
		{
			LL t = go(m, i, a);
			res *= t;
			res %= MOD;
		}

	REP(i, c)
	{
		res *= (k - i);
		res %= MOD;
	}
	//fprintf(stderr, "res: %lld\n", res);
	return res % MOD;
}

LL solve()
{
	LL res = go(K, 1, -1);
	return res;
}

int main()
{
    int cT, t, i, a, b;
    
    freopen("c:/gcj/c/2.out", "w", stdout);
    freopen("c:/gcj/c/2.in", "r", stdin);
    scanf("%d", &cT);
    REP(t, cT)
    {		
        printf("Case #%d: ", t + 1);
		scanf("%d%d", &n, &K);
		CL(g, 0);
		REP(i, n - 1) 
		{
			scanf("%d%d", &a, &b);
			g[a][b] = g[b][a] = 1;
		}

        LL res = solve();
            
        printf("%Ld\n", res);
		//fprintf(stderr, "%d\n", t);
    }
    fclose(stdout);
    return 0;
}
