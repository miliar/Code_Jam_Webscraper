#include <cstdio>
#include <cstring>

#include <algorithm>

using namespace std;

int n;
bool grid[ 300 ][ 300 ];

int L[ 300 ], R[ 300 ], D[ 300 ], U[ 300 ];

int np;
int px[ 100000 ], py[ 100000 ];

char Command[ 20 ];
int T;

int cross( int x0, int y0, int x1, int y1, int x2, int y2 ) {
	return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0);
}

const int dx[4] = { 0, 1, 0, -1 };
const int dy[4] = { 1, 0, -1, 0 };

void small( int &a, int b ) { if( b < a ) a = b; }
void large( int &a, int b ) { if( b > a ) a = b; }

int main( void )
{
	freopen( "A-small.in", "r", stdin );
	freopen( "A-small.out", "w", stdout );

	int T; scanf( "%d", &T );

	for( int counter = 0; counter < T; ++counter ) {
		int x, y, d; x = y = 120, d = 0;

		np = 0;
		px[np] = x, py[np] = y, ++np;

		for( int i = 0; i < 300; ++i ) {
			L[i] = D[i] = 100000;
			R[i] = U[i] = -100000;
		}

		scanf( "%d", &n );

		for( int i = 0; i < n; ++i ) {
			int T; scanf( "%s %d", Command, &T );

			while( T-- ) {
				for( int j = 0; Command[j]; ++j ) {
					switch( Command[j] ) {
					case 'F': 
						x += dx[d], y += dy[d]; 
						px[np] = x, py[np] = y, ++np;
						break;
					case 'L': d = (d + 3) % 4; break;
					case 'R': d = (d + 1) % 4; break;
					}
				}
			}
		}
		px[np] = *px, py[np] = *py;

		for( int i = 0; i < np; ++i ) {
			if( px[i] == px[i+1] ) {
				small( L[ min( py[i], py[i+1] ) ], px[i] );
				large( R[ min( py[i], py[i+1] ) ], px[i] );
			} else {
				small( D[ min( px[i], px[i+1] ) ], py[i] );
				large( U[ min( px[i], px[i+1] ) ], py[i] );
			}
		}

		int area = 0;

		for( int i = 2; i < np; ++i )
			area += cross( *px, *py, px[i-1], py[i-1], px[i-2], py[i-2] );
		if( area < 0 ) area = -area;
		area /= 2;

		int ret = 0;

		for( int i = 0; i < 300; i++ )
			for( int j = 0; j < 300; ++j )
				if( j >= L[i] && j < R[i] || i >= D[j] && i < U[j] ) ++ret;

		printf( "Case #%d: %d\n", counter + 1, ret-area );
	}

	return 0;
}
