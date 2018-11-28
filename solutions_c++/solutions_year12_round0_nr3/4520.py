#include <cstdio>
#include <cstring>

bool isThat( int, int );

int main()
{
	int t, c = 0, a, b, count;
	scanf( "%d", &t );
	while( c++ < t )
	{
		count = 0;
		scanf( "%d%d", &a, &b );
		for( int i = a; i <= b; ++i )
			for( int j = i + 1; j <= b; ++j )
				if( isThat( i, j ) )
					++count;
		printf( "Case #%d: %d\n", c, count );
	}
	return 0;
}

void ToString( int n, char *S )
{
	int i = 0;
	if( n == 0 )
		S[ i++ ] = '0';
	while( n > 0 )
	{
		S[ i++ ] = ( n % 10 ) + '0';
		n /= 10;
	}
	S[ i ] = '\0';
	for( int x = 0; x < i; ++x, --i )
	{
		char c = S[ x ];
		S[ x ] = S[ i - 1 ];
		S[ i - 1 ] = c;
	}
}

unsigned int CountDigits( int n )
{
	int c = 0;
	if( n == 0 )
		return 1;
	while( n > 0 )
	{
		n /= 10;
		++c;
	}
	return c;
}

void Rotate( char *A )
{
	int len = strlen( A );
	char c = A[ len - 1 ];
	for( int i = len - 1; i > 0; --i )
		A[ i ] = A[ i - 1 ];
	A[ 0 ] = c;
}

bool isThat( int n, int m )
{
	if( CountDigits( n ) != CountDigits( m ) )
		return false;
	char A[ 10 ], B[ 10 ];
	ToString( n, A );
	ToString( m, B );
	for( int i = 0; i < 10; ++i )
	{
		if( A[ 0 ] != '0' && strcmp( A, B ) == 0 )
		{
//		printf( "%d %d <-> %s == %s\n", n, m, A, B );
			return true;
		}
		Rotate( A );
	}
	return false;
}
