#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int n, t, x;
char ch;

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d ", &n );
		
		int rez = 0, pA = 1, pB = 1;
		int d = 0; char last = 0;
		
		for( int j = 0; j < n; ++j ) {
			scanf( "%c %d ", &ch, &x );
			if( last == ch ) {
				if( ch == 'O' ) {
					d += abs( x - pA ) + 1;
					rez += abs( x - pA ) + 1;
					pA = x;
				} else {
					d += abs( x - pB ) + 1;
					rez += abs( x - pB ) + 1;
					pB = x;
				}
			} else {
				if( ch == 'O' ) {
					int t = max( abs( x - pA ) - d, 0 );
					d = t + 1; rez += t + 1; pA = x; last = ch;
				} else {
					int t = max( abs( x - pB ) - d, 0 );
					d = t + 1; rez += t + 1; pB = x; last = ch;
				}
			}
		}
		
		printf( "Case #%d: %d\n", i+1, rez );
	}
	
	return( 0 );
}
