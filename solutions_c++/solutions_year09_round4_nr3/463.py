/*
TASK: 
LANG: C++
USER: smilitude1
*/

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REV(x) reverse( ALL( x ) )

#define IO freopen("c.in","r",stdin); freopen("c.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl

int p[20][30];
bool ok[20][20], loved[1<<16];
int N, K ;

int memo[1<<16];
int solve( int mask ) {
	if( mask == 0 ) return 0;
	int& ret = memo[ mask ];
	if( ret != -1 ) return ret;

	ret = N;

	int good = 0;
	int m = mask;
	while( m ) {
		if( loved[ m ] ) ret = min( ret, 1 + solve(mask & ~m) );
		m = ( m -1 ) & mask;
	}
	
	return ret;
}

void init() {
	
	REP(i,1<<N) loved[i] = 0;
	REP(mask,1<<N) {
		bool love = true;
		REP(i,N) if( mask & (1<<i) ) REP(j,N) if( mask & (1<<j) ) if( !ok[i][j]	) love = false;
		loved[ mask ] = love;
	}
}

bool check( int a, int b ) {
	REP(i,K-1) {
		int ya1 = p[a][i], ya2 = p[a][i+1];
		int yb1 = p[b][i], yb2 = p[b][i+1];

		if( yb1 >= ya1 && yb2 <= ya2 ) return false;
		swap( ya1, yb1 ); swap( ya2, yb2 ); 
		if( yb1 >= ya1 && yb2 <= ya2 ) return false;
	}
	return true;
}

int main() {
	int ncase = 0, t;
	
	IO
	
	scanf("%d",&t);
	while( t-- ) {
		scanf("%d %d",&N,&K);
		REP(i,N) REP(j,K) scanf("%d",&p[i][j] );
		REP(i,N) REP(j,N) if( i != j ) ok[i][j] = check(i,j);
		REP(i,N) ok[i][i] = true;
		init();
	/*	
		REP(i,N) {
			REP(j,N) cout << " " <<ok[i][j] ;
			cout << endl;
		} */

		REP(i,1<<N) memo[i] = -1;
		printf("Case #%d: %d\n", ++ncase, solve( (1<<N)-1 ));
	}

	return 0;
}
