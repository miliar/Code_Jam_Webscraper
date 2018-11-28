#include <cstdio>
#include <memory>

static const int MAXW = 112;
static const int MAXH = 112;

int T;
int H, W;
int A[ MAXH ][ MAXW ];

void Read()
{
	int i, j;
	scanf( "%d%d", &H, &W );
	for( i = 0; i < H; ++i )
	{
		for( j = 0; j < W; ++j )
		{
			scanf( "%d", &A[ i ][ j ] );
		}
	}
}

bool Less( int i, int j, int a )
{
	return 0 <= i && i < H && 
		    0 <= j && j < W &&
			 A[ i ][ j ] < a;
}

int BasinIndex;
int Basin[ MAXH ][ MAXW ];

int GetBasin( int i, int j )
{
	if( Basin[ i ][ j ] == -1 )
	{
		int dir = -1;
		int a = -1;
		if( Less( i - 1, j, A[ i ][ j ] ) && ( dir == -1 || A[ i - 1 ][ j ] < a ) )
		{
			dir = 0;
			a = A[ i - 1 ][ j ];
		}
		if( Less( i, j - 1, A[ i ][ j ] ) && ( dir == -1 || A[ i ][ j - 1 ] < a ) )
		{
			dir = 1;
			a = A[ i ][ j - 1 ];
		}
		if( Less( i, j + 1, A[ i ][ j ] ) && ( dir == -1 || A[ i ][ j + 1 ] < a ) )
		{
			dir = 2;
			a = A[ i ][ j + 1 ];
		}
		if( Less( i + 1, j, A[ i ][ j ] ) && ( dir == -1 || A[ i + 1 ][ j ] < a ) )
		{
			dir = 3;
			a = A[ i + 1 ][ j ];
		}
		switch( dir )
		{
		case 0:
			Basin[ i ][ j ] = GetBasin( i - 1, j );
			break;
		case 1:
			Basin[ i ][ j ] = GetBasin( i, j - 1 );
			break;
		case 2:
			Basin[ i ][ j ] = GetBasin( i, j + 1 );
			break;
		case 3:
			Basin[ i ][ j ] = GetBasin( i + 1, j );
			break;
		default:
			Basin[ i ][ j ] = BasinIndex++;
			break;
		}
	}
	return Basin[ i ][ j ];
}

char Result[ MAXH ][ MAXW ];
char Index[ 26 ];

void Work()
{
	int i, j;
	memset( Basin, -1, sizeof( Basin ) );
	memset( Result, 0, sizeof( Result ) );
	memset( Index, -1, sizeof( Index ) );
	int curr_basin = 0;
	BasinIndex = 0;
	for( i = 0; i < H; ++i )
	{
		for( j = 0; j < W; ++j )
		{
			int basin = GetBasin( i, j );
			if( Index[ basin ] == -1 )
				Index[ basin ] = curr_basin++;
			Result[ i ][ j ] = 'a' + Index[ basin ];
		}
	}
}

void Write( int t )
{
	int i, j;
	printf( "Case #%d:\n", t );
	for( i = 0; i < H; ++i )
	{
		for( j = 0; j < W; ++j )
		{
			if( j != 0 )
				putchar( ' ' );
			putchar( Result[ i ][ j ] );
		}
		putchar( '\n' );
	}
}

int main()
{
	int t;
	scanf( "%d", &T );
	for( t = 0; t < T; ++t )
	{
		Read();
		Work();
		Write( t + 1 );
	}
	return 0;
}
