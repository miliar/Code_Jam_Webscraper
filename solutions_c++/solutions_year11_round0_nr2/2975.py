#include <cstdio>

int combinable( char, char, char T[ 50 ][ 3 ], int );
bool oposable( char *, int, char, char T[ 50 ][ 2 ], int );
void push( char *, int &, char, char C[ 50 ][ 3 ], int, char O[ 50 ][ 2 ], int );
void print( char *, int );

int main()
{
	int t, c, d, caso = 0, n, size;
	char C[ 50 ][ 3 ], O[ 50 ][ 2 ], L[ 110 ], tmp;
	scanf( "%d", &t );
	while( caso++ < t )
	{
		scanf( "%d", &c );
		for( int i = 0; i < c; ++i )
			for( int j = 0; j < 3; )
			{
				tmp = getchar();
				if( tmp >= 'A' && tmp <= 'Z' )
					C[ i ][ j++ ] = tmp;
			}
		scanf( "%d", &d );
		for( int i = 0; i < d; ++i )
			for( int j = 0; j < 2; )
			{
				tmp = getchar();
				if( tmp >= 'A' && tmp <= 'Z' )
					O[ i ][ j++ ] = tmp;
			}
		scanf( "%d", &n );
		size = 0;
		for( int i = 0; i < n; )
		{
			tmp = getchar();
			if( tmp >= 'A' && tmp <= 'Z' )
			{
				++i;
				push( L, size, tmp, C, c, O, d );
			}
		}
		printf( "Case #%d: ", caso );
		print( L, size );
	}
	return 0;
}

void print( char *L, int n )
{
	putchar( '[' );
	for( int i = 0; i < n; ++i )
	{
		if( i > 0 )
			printf( ", " );
		putchar( L[ i ] );
	}
	printf( "]\n" );
}

int combinable( char last, char next, char T[ 50 ][ 3 ], int n )
{
	for( int i = 0; i < n; ++i )
		if( ( T[ i ][ 0 ] == last && T[ i ][ 1 ] == next ) || /* can they be in diferent order ? */
			( T[ i ][ 0 ] == next && T[ i ][ 1 ] == last ) )
			return i;
	return -1;
}

bool oposable( char *L, int n, char next, char T[ 50 ][ 2 ], int sn )
{
	for( int i = 0; i < n; ++i )
		for( int j = 0; j < sn; ++j )
			if( ( T[ j ][ 0 ] == next && T[ j ][ 1 ] == L[ i ] ) ||
				( T[ j ][ 1 ] == next && T[ j ][ 0 ] == L[ i ] ) )
				return true;
	return false;
}

void push( char *L, int &size, char tmp, char C[ 50 ][ 3 ], int c, char O[ 50 ][ 2 ], int d )
{
	int tk;
	if( size > 0 && ( tk = combinable( L[ size - 1 ], tmp, C, c ) ) >= 0 )
	{
		--size;
		push( L, size, C[ tk ][ 2 ], C, c, O, d );
	}
	else if( size > 0 && oposable( L, size, tmp, O, d ) )
		size = 0;
	else
		L[ size++ ] = tmp;
}

