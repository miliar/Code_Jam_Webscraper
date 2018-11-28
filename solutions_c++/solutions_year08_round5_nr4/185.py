#include <cstdio>
#include <memory>

const int MAX = 100;

int H, W, R;
bool IsRock[ MAX ][ MAX ];

void Read()
{
	int i;
	scanf( "%d%d%d", &H, &W, &R );
	memset( IsRock, 0, sizeof( IsRock ) );
	for( i = 0; i < R; ++i )
	{
		int r, c;
		scanf( "%d%d", &r, &c );
		--r;
		--c;
		IsRock[ r ][ c ] = true;
	}
}

int Count[ MAX ][ MAX ];

void Work()
{
	int i, j;
	memset( Count, 0, sizeof( Count ) );
	Count[ 0 ][ 0 ] = 1;
	for( i = 0; i < H; ++i )
	{
		for( j = 0; j < W; ++j )
		{
			if( IsRock[ i ][ j ] )
				continue;
			if( i + 1 < H && j + 2 < W )
				Count[ i + 1 ][ j + 2 ] = ( Count[ i + 1 ][ j + 2 ] + Count[ i ][ j ] ) % 10007;
			if( i + 2 < H && j + 1 < W )
				Count[ i + 2 ][ j + 1 ] = ( Count[ i + 2 ][ j + 1 ] + Count[ i ][ j ] ) % 10007;
		}
	}
}

void Write( int i )
{
	printf( "Case #%d: %d\n", i, Count[ H - 1 ][ W - 1 ] );
}

int main()
{
	int i, n;
	scanf( "%d", &n );
	for( i = 1; i <= n; ++i )
	{
		Read();
		Work();
		Write( i );
	}
	return 0;
}
