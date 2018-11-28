#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

bool is_won(char a[10][10], char c) {
	bool yes;
	REP(i,4) {
		yes = true; REP(j,4) if ( !(a[i][j] == c || a[i][j] == 'T') ) yes = false;
		if ( yes ) return true;
		yes = true; REP(j,4) if ( !(a[j][i] == c || a[j][i] == 'T') ) yes = false;
		if ( yes ) return true;
	}
	yes = true; REP(i,4) if ( !(a[i][i] == c || a[i][i] == 'T') ) yes = false;
	if ( yes ) return true;
	yes = true; REP(i,4) if ( !(a[i][3-i] == c || a[i][3-i] == 'T') ) yes = false;
	if ( yes ) return true;
	return false;
}


bool is_complete(char a[10][10]) {
	REP(i,4) REP(j,4) if ( a[i][j] == '.' ) return false;
	return true;
}

int main()
{
	int T;
	scanf( "%d", &T );

	FOR(tc,1,T) {
		char a[10][10];
		REP(i,4) scanf( "%s", a[i] );
		
		printf( "Case #%d: ", tc );
		if      ( is_won(a,'X') ) puts( "X won" );
		else if ( is_won(a,'O') ) puts( "O won" );
		else if ( is_complete(a) ) puts( "Draw" );
		else puts( "Game has not completed" );
	}

	return 0;
}
