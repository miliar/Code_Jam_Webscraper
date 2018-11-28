#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <memory.h>

static const int MAXC = 40;
static const int MAXD = 32;
static const int MAXN = 111;

int C, D, N;
char _Combine[ 26 ][ 26 ], ( *Combine )[ 26 ] = ( char ( * )[ 26 ] )&_Combine[ -'A' ][ -'A' ];
bool _Opposed[ 26 ][ 26 ], ( *Opposed )[ 26 ] = ( bool ( * )[ 26 ] )&_Opposed[ -'A' ][ -'A' ];
char Str[ MAXN + 1 ];

void Read()
{
	int i;
	memset( _Combine, 0, sizeof( _Combine ) );
	memset( _Opposed, 0, sizeof( _Opposed ) );

	scanf( "%d", &C );
	for( i = 0; i < C; ++i )
	{
		char f, s, r;
		scanf( " %c%c%c", &f, &s, &r );
		Combine[ f ][ s ] = Combine[ s ][ f ] = r;
	}
	scanf( "%d", &D );
	for( i = 0; i < D; ++i )
	{
		char f, s;
		scanf( " %c%c", &f, &s );
		Opposed[ f ][ s ] = Opposed[ s ][ f ] = true;
	}
	scanf( "%d", &N );
	scanf( "%s", Str );
}

int Length;
char Result[ MAXN + 1 ];

void Work()
{
	int i, k;
	Length = 0;
	for( k = 0; k < N; ++k )
	{
		Result[ Length++ ] = Str[ k ];
		if( Length >= 2 && Combine[ Result[ Length - 2 ] ][ Result[ Length - 1 ] ] )
		{
			Result[ Length - 2 ] = Combine[ Result[ Length - 2 ] ][ Result[ Length - 1 ] ];
			--Length;
		}
		for( i = 0; i < Length; ++i )
		{
			if( Opposed[ Result[ i ] ][ Result[ Length - 1 ] ] )
				Length = 0;
		}
	}
}

void Write( int t )
{
	int i;
	printf( "Case #%d: [", t );
	for( i = 0; i < Length; ++i )
	{
		if( i != 0 )
			printf( ", " );
		putchar( Result[ i ] );
	}
	printf( "]\n" );
}

int main()
{
	int i, t;
	scanf( "%d", &t );
	for( i = 0; i < t; ++i )
	{
		Read();
		Work();
		Write( i + 1 );
	}
	return 0;
}
