#include <stdio.h>
#include <string.h>

#define N 1010

double miss[ N ][ N ];
double ex[ N ];

int num[ N ];

void init ( void ) {
	memset ( miss, 0, sizeof ( miss ) );
	miss[ 0 ][ 0 ] = 1;
	miss[ 1 ][ 0 ] = 0;
	miss[ 1 ][ 1 ] = 1;
	for ( int i = 2 ; i < N ; ++i ) {
		for ( int j = 0 ; j < i - 1; ++j ) {
			miss[ i ][ j ] = miss[ i - 1 ][ j ] * ( i - j - 1 ) / ( i - j ) +
					 miss[ i - 2 ][ j ] / ( i - j );
		}
		miss[ i ][ i - 1 ] = 0;
		miss[ i ][ i ] = miss[ i - 1 ][ i - 1 ] / i;
	}
	
	ex[ 0 ] = 0; ex[ 1 ] = 0; ex[ 2 ] = 2;
	for ( int i = 3 ; i < N ; ++i ) {
		double app = 1;
		for ( int j = 1 ; j < i ; ++j ) {
			app += miss[ i ][ j ] * ex[ i - j ];
		}
		ex[ i ] = app / ( 1 - miss[ i ][ 0 ] );
	}
}

inline void swap ( int a, int b ) {
	num[ b ] = num[ a ];
	num[ a ] = a;
}

int main ( void ) {
	//freopen ( "in.txt", "r", stdin );
	//freopen ( "out1.txt", "w", stdout );
	freopen ( "D-large.in", "r", stdin );
	freopen ( "D-large.out", "w", stdout );
	int cas, n;
	double ans;
	init ();
	scanf ( "%d", &cas );
	for ( int t = 0 ; t < cas ; ++t ) {
		//scanf ( "%d", &n );
		//printf ( "%lf\n", ex[ n ] );
		int i, j;
		double ans = 0;
		int times = 0;
		scanf ( "%d", &n );
		for ( int i = 1 ; i <= n ; ++i ) {
			scanf ( "%d", &num[ i ] );
		}
		for ( int i = 1 ; i <= n ; ++i ) {
			if ( num[ i ] != i ) {
				++times;
			}
		}
		printf ( "Case #%d: %.6lf\n", t + 1, times + 0.0 );
		//printf ( "Case #%d: %.6lf\n", t + 1, ex[ times ] );
	}
	return 0;
}

