#include <iostream>
using namespace std;

bool map[ 1000 ][ 1000 ], map2[ 1000 ][ 1000 ];
int x1[ 20 ], x2[ 20 ], y1[ 20 ], y2[ 20 ];
int n, X, Y;

int main()
{
	
	int t = 0, test, i, j, k;
	bool flag;
	
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "Cout.txt", "w", stdout );
	
	scanf( "%d", &test );

	
	while ( test-- )
	{
		
		scanf( "%d", &n ); 
		
		memset( map, 0, sizeof( map ) );
		
		X = 0;
		Y = 0;
		for ( i = 0; i < n; ++i )
		{
			scanf( "%d %d %d %d", &x1[ i ], &y1[ i ], &x2[ i ], &y2[ i ] );
			X = max( X, x1[ i ] );
			X = max( X, x2[ i ] );
			Y = max( Y, y1[ i ] );
			Y = max( Y, y2[ i ] );
			
			for ( j = y1[ i ]; j <= y2[ i ]; ++j )
				for ( k = x1[ i ]; k <= x2[ i ]; ++k )
					map[ j ][ k ] = 1;
			
		}
		++X, ++Y;
		
		
		flag = 1;
		for ( i = 0; flag; ++i )
		{
			
			flag = 0;
			for ( j = 0; j <= Y; ++j )
			{
				for ( k = 0; k <= X; ++k )
					if ( map[ j ][ k ] )
					{
						flag = 1;
						break;
					}
				if ( flag )
					break;
			}
			
			if ( !flag )
				break;
			
			for ( j = 0; j <= Y; ++j )
			{
				for ( k = 0; k <= X; ++k )
				{
					map2[ j ][ k ] = map[ j ][ k ];
					if ( map[ j ][ k ] )
					{
						if ( j == 0 && k == 0 )
						{
							map2[ j ][ k ] = 0;
							continue;
						}
						
						if ( j == 0 )
							if ( !map[ j ][ k - 1 ] )
							{
								map2[ j ][ k ] = 0;
								continue;
							}
						
						if ( k == 0 )
							if ( !map[ j - 1 ][ k ] )
							{
								map2[ j ][ k ] = 0;
								continue;
							}
						
						if ( !map[ j - 1 ][ k ] && !map[ j ][ k -1 ] )
							map2[ j ][ k ] = 0;
					}
					else
					{
						if ( j - 1 >= 0 && k - 1 >= 0 )
							if ( map[ j - 1 ][ k ] && map[ j ][ k - 1 ] )
								map2[ j ][ k ] = 1;
					}
				}
			}
			
			memcpy( map, map2, sizeof( map ) );
			/*
			for ( j = 0; j <= Y; ++j )
			{
				for ( k = 0; k <= X; ++k )
					printf( "%d", map[ j ][ k ] );
				putchar( '\n' );
			}
				putchar( '\n' );
				
				//getchar();
			
			*/
		}
		
		printf( "Case #%d: %d\n", ++t, i );
	}
	
	return 0;
}
			
