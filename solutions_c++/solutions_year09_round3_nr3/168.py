#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_n=(b);i<=_n;i++)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n;i--)
#define REP(i,n) FOR(i,0,n-1)
typedef long long int64;
#define two(X) (1<<(X))
#define two64(X) (((int64)1)<<(X))
#define contain(S,x) (((S)&two(x))>0)

const int inf = 1000000000;

int P,Q;
int pos[111];
int f[111][111];

int solve( int l, int r ) {
	int &ret = f[l][r];
	if ( ret!=-1 ) return ret;
	ret = inf;

	FOR(i,l+1,r-1)
		ret = min( ret, pos[r]-pos[l]-2 + solve( l,i ) + solve( i,r ) );

	if ( ret==inf ) ret=0;
	return ret;
}

int main() {
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.out", "w", stdout );

	int ntc;
	scanf( "%d",&ntc );
	REP(tc,ntc) {
		scanf( "%d%d", &P,&Q );
		
		pos[0] = 0;
		FOR(i,1,Q) scanf( "%d",&pos[i] );
		pos[Q+1] = P+1;

		memset( f,-1,sizeof(f) );
		printf( "Case #%d: %d\n", tc+1, solve(0,Q+1) );
	}
	return 0;
}
