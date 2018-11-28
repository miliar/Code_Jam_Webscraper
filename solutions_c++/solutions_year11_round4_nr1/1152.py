#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int T, x, s, r, t, n, P[ 1000005 ];
int b[ 1005 ], e[ 1005 ], w[ 1005 ];

int main( void ) {
	scanf( "%d", &T );
	for( int i = 0; i < T; ++i ) {
		scanf( "%d %d %d %d %d", &x, &s, &r, &t, &n );
		
		vector< pair< int, int > > V;
		memset( P, 0, sizeof( P ) );
		
		for( int j = 0; j < n; ++j ) {
			scanf( "%d %d %d", &b[ j ], &e[ j ], &w[ j ] );
			V.push_back( make_pair( w[ j ] + s, e[ j ] - b[ j ] ) );
			for( int k = b[ j ]; k < e[ j ]; ++k ) P[ k ] = 1;
		}
		
		int p = -1;
		for( int j = 0; j <= x; ++j ) {
			if( j < x && P[ j ] == 0 ) {
				if( p == -1 ) p = j;
				continue;
			}
			
			if( p == j ) { ++p; continue; }
			if( p != -1 ) V.push_back( make_pair( s, j - p ) );
			p = j + 1;
		}
		
		sort( V.begin(), V.end() );
		int len = ( int )V.size();
		double rez = 0.0, T = ( double )t;
		
		for( int j = 0; j < len; ++j ) {
			//printf( "(%d %d)\n", V[ j ].first, V[ j ].second );
			double xx = ( double )V[ j ].second / V[ j ].first;
			
			if( T == 0 ) rez += xx;
			else {
				double brzi = ( double )V[ j ].second / ( V[ j ].first + r - s );
				if( brzi <= T ) {
					T -= brzi; rez += brzi;
				} else {
					double put = T * ( V[ j ].first + r - s );
					double ost = V[ j ].second - put;
					rez += T + ost / V[ j ].first; T = 0;
				}
			}
		}
		
		printf( "Case #%d: %lf\n", i+1, rez );
	}
	
	return( 0 );
}
