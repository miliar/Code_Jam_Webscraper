#include <cstdio>
#include <memory>

static const int MAXL = 24;
static const int MAXD = 5012;
static const int MAXN = 512;

int L, D, N;
char Word[ MAXD ][ MAXL + 1 ];

void Read()
{
	int i;
	scanf( "%d%d%d\n", &L, &D, &N );
	for( i = 0; i < D; ++i )
	{
		scanf( "%s", Word[ i ] );
	}
}

int Result;
bool IsUsed[ MAXL ][ 26 ];

void Work()
{
	int i, j;
	memset( IsUsed, 0, sizeof( IsUsed ) );
	scanf( " " );
	for( i = 0; i < L; ++i )
	{
		int c = getchar();
		if( c == '(' )
		{
			while( ( c = getchar() ) != ')' )
			{
				IsUsed[ i ][ c - 'a' ] = true;
			}
		}
		else
		{
			IsUsed[ i ][ c - 'a' ] = true;
		}
	}

	Result = 0;
	for( i = 0; i < D; ++i )
	{
		for( j = 0; j < L; ++j )
		{
			if( !IsUsed[ j ][ Word[ i ][ j ] - 'a' ] )
				break;
		}
		if( j < L )
			continue;
		++Result;
	}

}

void Write( int t )
{
	printf( "Case #%d: %d\n", t, Result );
}

int main()
{
	int t;
	Read();
	for( t = 0; t < N; ++t )
	{
		Work();
		Write( t + 1 );
	}
	return 0;
}
