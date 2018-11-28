#include <iostream>
#include <string>
using namespace std;

string tile[50];
int R, C;

bool Judge() {
	for( int i=0; i<R; i++ ) {
		for( int j=0; j<C; j++ ) {
			if( tile[i][j] == '#' ) {
				if( i == R-1 ) return false;
				if( j == C-1 ) return false;
				if( tile[i+1][j] != '#' ) return false;
				if( tile[i][j+1] != '#' ) return false;
				if( tile[i+1][j+1] != '#' ) return false;
				tile[i][j] = tile[i+1][j+1] = '/';
				tile[i+1][j] = tile[i][j+1] = '\\';
			}
		}
	}
}

int main() {
	freopen( "A_Large.in", "r", stdin );
	freopen( "A_Large.out", "w", stdout );

	int TC;
	cin >> TC;

	for( int TCC=1; TCC<=TC; TCC++ ) {
		int T = 0;
		cin >> R >> C;
		for( int i=0; i<R; i++ ) {
			cin >> tile[i];
			for( int j=0; j<C; j++ )
				if( tile[i][j] == '#' ) T++;
		}

		cout << "Case #" << TCC << ":" << endl;
		if( T%4 != 0 ) {
			cout << "Impossible" << endl;
			continue;
		}

		bool poss = Judge();
		if( !poss ) {
			cout << "Impossible" << endl;
			continue;
		}

		for( int i=0; i<R; i++ ) cout << tile[i] << endl;
	}
}