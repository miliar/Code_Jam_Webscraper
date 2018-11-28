#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int r, c;
char tile[ 100 ][ 100 ];
bool mark[ 100 ][ 100 ];

bool check()
{
	for ( int i = 0; i < r; ++i )
		for ( int j = 0; j < c; ++j )
			if ( tile[ i ][ j ] == '#' && !mark[ i ][ j ] )
				return 0;
	return 1;
}


int main()
{
	int t;
	freopen("A.out", "w", stdout );
	scanf( "%d", &t );

	for ( int k = 1; k <= t; ++k )
	{

		scanf( "%d %d", &r, &c );

		for ( int i = 0; i < r; ++i )
			scanf( " %s", &tile[ i ] );

		printf( "Case #%d:\n", k );

		memset( mark, 0, sizeof( mark ) );
		for ( int i = 0; i < r - 1; ++i )
			for ( int j = 0; j < c - 1; ++j )
				if ( tile[ i ][ j ] == '#' && !mark[ i ][ j ] )
					if ( tile[ i + 1 ][ j ] == '#' && tile[ i ][ j + 1 ] == '#' && tile[ i + 1 ][ j + 1 ] == '#' )
						mark[ i ][ j ] = mark[ i + 1 ][ j + 1 ] = mark[ i + 1 ][ j ] = mark[ i ][ j + 1 ] = 1;

		if ( check() )
		{
			memset( mark, 0, sizeof( mark ) );
			for ( int i = 0; i < r - 1; ++i )
				for ( int j = 0; j < c - 1; ++j )
					if ( tile[ i ][ j ] == '#' && !mark[ i ][ j ] )
					{
						tile[ i ][ j ] = tile[ i + 1 ][ j + 1 ] = '/';
						tile[ i + 1 ][ j ] = tile[ i ][ j + 1 ] = '\\';
						mark[ i ][ j ] = mark[ i + 1 ][ j + 1 ] = mark[ i ] [ j + 1 ] = mark[ i + 1 ][ j ] = 1;
					}
			for ( int i = 0; i < r; ++i )
				puts( tile[ i ] );
		}
		else
			puts( "Impossible" );
	}
	return 0;
}



		






	
