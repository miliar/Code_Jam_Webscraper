// {{{
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <complex>
#include <stack>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <assert.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PI;
typedef pair<LD,LD> PD;

#define VAR(v,n) __typeof(n) v=(n)
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<=(b); i++)
#define FORD(i,a,b) for(int i=(a); i>=(b); i--)
#define FORE(i,c) for(VAR(i,(c).begin()); i!=(c).end(); i++)
#define CLR(A,v) memset((A),v,sizeof((A)))

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define ALL(x) x.begin(),x.end()
#define SIZE(x) ((int)(x).size())
// }}}

#define Q 15
#define M 2055
#define inf 1000000000

int n;
int T[M];
int W[Q][M];

int res[Q][Q][M];


inline void oblicz(int p, int x, int ile) {
	if (res[p][ile][x]!=inf) return;
	if (p==0) {
		if (ile>=T[x]) res[p][ile][x]=0;
		else if (ile==T[x]-1) res[p][ile][x]=W[p][x];
		return;
	}
	oblicz(p-1,2*x,ile);
	oblicz(p-1,2*x+1,ile);
	res[p][ile][x]=min(res[p][ile][x],res[p-1][ile][2*x]+res[p-1][ile][2*x+1]);
	oblicz(p-1,2*x,ile+1);
	oblicz(p-1,2*x+1,ile+1);
	res[p][ile][x]=min(res[p][ile][x],res[p-1][ile+1][2*x]+res[p-1][ile+1][2*x+1]+W[p][x]);
}


int main() {
	int test,number=0;
	scanf("%d",&test);
	while (test--) {
		printf("Case #%d: ",++number);

		scanf("%d",&n);
		REP(i,(1<<n)) scanf("%d",&T[i]);
		REP(i,n)
			REP(j,(1<<(n-i-1))) scanf("%d",&W[i][j]);

		FOR(i,0,n) FOR(j,0,n)
			REP(k,(1<<(n-i-1))) res[i][j][k]=inf;

		REP(i,(1<<(n-1))) T[i]=n-min(T[2*i],T[2*i+1]);

		oblicz(n-1,0,0);
		printf("%d\n",res[n-1][0][0]);
	}
	return 0;
}
