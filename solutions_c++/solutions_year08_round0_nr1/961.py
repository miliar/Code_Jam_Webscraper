#include <cstdio>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector <string> se;
int sol[101][1001];

int main(){
	int tt, n, k;
	string t;
	scanf( "%d", &tt );

	for( int tp = 1; tp <= tt; ++tp ){
		scanf( "%d\n", &n );
		se.resize(n);
		memset( sol, 0x3f, sizeof sol );

		for( int i = 0; i < n; ++i ) getline( cin, se[i] );

		scanf( "%d\n", &k );
		getline( cin, t );

		for( int i = 0; i < n; ++i ) {
			if( se[i] != t ) sol[i][0] = 0;
		}

		for( int i = 1; i < k; ++i ){
			getline( cin, t );
			for( int j = 0; j < n; ++j ){
				if( se[j] != t ) {
					for( int m = 0; m < n; ++m ){
						sol[j][i] = min( sol[j][i], sol[m][i-1] + ((m == j)?0:1) );
					}
				}
			}
		}

		int rj = 0x3f3f3f3f;

		for( int i = 0; i < n; ++i ){
			rj = min( rj, sol[i][k-1] );
		}

		printf( "Case #%d: %d\n", tp, rj );

	}


	return 0;
}
