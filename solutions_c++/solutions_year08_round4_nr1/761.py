#include <iostream>
#include <cassert>
#include <cstring>

using namespace std;

int m, v;

const int INF = 1000000000;
int val[10005][2];
int dp[10005][2];

int rec( int k, int wanted ) {
	assert( 1 <= k && k <= m );
	if( k > (m-1)/2 ) {
		if( wanted != val[k][0] ) return INF;
		return 0;
	}
	int& res = dp[k][wanted];
	if( res != -1 ) return res;
	res = INF;
	// and gate
	if( val[k][0] == 1 || val[k][1] == 1 ) {
		int cost = val[k][0] == 1 ? 0 : 1;
		for( int i = 0; i < 2; ++i ) {
			int costleft = rec( 2*k, i );
			if( costleft >= INF ) continue;
			for( int j = 0; j < 2; ++j ) {
				int costright = rec( 2*k+1, j );
				if( costright >= INF ) continue;
				if( (i & j) != wanted ) continue;
				res = min( cost + costleft + costright, res );
			}
		}
	}
	// or gate
	if( val[k][0] == 0 || val[k][1] == 1 ) {
		int cost = val[k][0] == 0 ? 0 : 1;
		for( int i = 0; i < 2; ++i ) {
			int costleft = rec( 2*k, i );
			if( costleft >= INF ) continue;
			for( int j = 0; j < 2; ++j ) {
				int costright = rec( 2*k+1, j );
				if( costright >= INF ) continue;
				if( (i | j) != wanted ) continue;
				res = min( cost + costleft + costright, res );
			}
		}
	}
	return res;
}

int main() {
	int cases;
	
	cin >> cases;
	for( int c = 1; c <= cases; ++c ) {
		cin >> m >> v;
		for( int i = 1; i <= (m-1)/2; ++i ) {
			cin >> val[i][0] >> val[i][1];
		}
		for( int i = (m-1)/2+1; i <= m; ++i ) {
			cin >> val[i][0];
		}
		memset( dp, -1, sizeof(dp) );
		int res = rec( 1, v );
		cout << "Case #" << c << ": ";
		if( res >= INF ) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << res << endl;
		}
	}
	return 0;
}

