#include <iostream>
#include <cstdio>
using namespace std;

#define MAXN 1010

char com[ MAXN ][ MAXN ];
int WPcnt[ MAXN ], n, WPtotal[ MAXN ];
double WP[ MAXN ], OWP[ MAXN ], OOP[ MAXN ];


int main()
{
	freopen( "A.out", "w", stdout );
	int t;
	scanf( "%d", &t );

	for ( int k = 1; k <= t; ++k )
	{
		scanf( "%d", &n );

		for ( int i = 0; i < n; ++i )
			scanf( " %s", com[ i ] );
		


		for ( int i = 0; i < n; ++i )
		{
			WPcnt[ i ] = 0, WPtotal[ i ] = 0;
			for ( int j = 0; j < n; ++j )
				if ( com[ i ][ j ] != '.' )
				{
					WPcnt[ i ] += 1;
					if ( com[ i ][ j ] == '1' )
						WPtotal[ i ] += 1;
				}
		
			WP[ i ] = ( double)WPtotal[ i ] / (double)WPcnt[ i ];

		}

		for ( int i = 0; i < n; ++i )
		{
			double cnt = 0, total = 0;
			for ( int j = 0; j < n; ++j )
				if ( com[ i ][ j ] != '.' )
				{
					cnt += 1;
					if ( com[ i ][ j ] == '0' )
						total += ( WPtotal[ j ] - 1 ) / (double)(WPcnt[ j ]-1);
					else
						total += (double)WPtotal[ j ] / (double)( WPcnt[ j ] - 1 );
				}
			OWP[ i ] = total / cnt;

		}

		for ( int i = 0; i < n; ++i )
		{
			double cnt = 0, total = 0;
			for ( int j = 0; j < n; ++j )
				if ( com[ i ][ j ] != '.' )
				{
					cnt += 1;
					total += OWP[ j ];
				}
			OOP[ i ] = total / cnt;
		}

		printf( "Case #%d:\n", k );
		for ( int i = 0; i < n; ++i )
			printf( "%.10lf\n", 0.25 * WP[ i ] + 0.5 * OWP[ i ] + 0.25 * OOP[ i ] );
	}
	return 0;
}



