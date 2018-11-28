#include <cstdio>
#include <cstring>

static const int MAXL = 512;

char Str[ MAXL + 1 ];

void Read()
{
	gets( Str );
}

const char Phrase[] = "welcome to code jam";
static const int PHRASE_LENGTH = 19;

int Result;
int Count[ PHRASE_LENGTH + 1 ][ MAXL + 1 ];

void Work()
{
	int i, j;
	int length = ( int )strlen( Str );
	for( i = 0; i <= length; ++i )
	{
		Count[ 0 ][ i ] = 1;
	}
	for( j = 1; j <= PHRASE_LENGTH; ++j )
	{
		Count[ j ][ 0 ] = 0;
	}

	for( j = 1; j <= PHRASE_LENGTH; ++j )
	{
		for( i = 1; i <= length; ++i )
		{
			Count[ j ][ i ] = Count[ j ][ i - 1 ];
			if( Phrase[ j - 1 ] == Str[ i - 1 ] )
				Count[ j ][ i ] = ( Count[ j ][ i ] + Count[ j - 1 ][ i - 1 ] ) % 10000;
		}
	}

	Result = Count[ PHRASE_LENGTH ][ length ];
}

void Write( int t )
{
	printf( "Case #%d: %04d\n", t, Result ); 
}

int main()
{
	int n;
	scanf( "%d\n", &n );
	for( int t = 0; t < n; ++t )
	{
		Read();
		Work();
		Write( t + 1 );
	}
	return 0;
}
