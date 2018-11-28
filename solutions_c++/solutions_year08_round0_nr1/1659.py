#include <cstdio>
#include <string>
#include <map>
using namespace std;

const int MAX_LENGTH = 106;
const int MAX_ENGINES = 106;
const int MAX_QUERIES = 1006;

int S, Q;
string Engine[ MAX_ENGINES ];
map< string, int > EngineIndex;
int Query[ MAX_QUERIES ];

void Read()
{
	int i;
	char str[ MAX_LENGTH + 1 ];
	scanf( "%d\n", &S );
	EngineIndex.clear();
	for( i = 0; i < S; ++i )
	{
		gets( str );
		Engine[ i ] = str;
		EngineIndex.insert( make_pair( string( str ), ( int )EngineIndex.size() ) );
	}
	scanf( "%d\n", &Q );
	for( i = 0; i < Q; ++i )
	{
		gets( str );
		Query[ i ] = EngineIndex[ str ];
	}
}

int Result;
int _CurrCount[ MAX_ENGINES + 1 ], _PrevCount[ MAX_ENGINES + 1 ], *CurrCount = _CurrCount, *PrevCount = _PrevCount;

void Work()
{
	int i, j, k;
	memset( _CurrCount, 0, sizeof( _CurrCount ) );
	memset( _PrevCount, 0, sizeof( _PrevCount ) );

	for( i = Q - 1; i >= 0; --i )
	{
		swap( CurrCount, PrevCount );
		for( j = 0; j < S; ++j )
		{
			if( Query[ i ] == j )
			{
				int count = -1;
				for( k = 0; k < S; ++k )
				{
					if( k == j )
						continue;
					if( count == -1 || count > PrevCount[ k ] + 1 )
						count = PrevCount[ k ] + 1;
				}
				CurrCount[ j ] = count;
			}
			else
			{
				CurrCount[ j ] = PrevCount[ j ];
			}
		}
	}

	Result = -1;
	for( i = 0; i < S; ++i )
	{
		if( Result == -1 || Result > CurrCount[ i ] )
			Result = CurrCount[ i ];
	}
}

void Write( int n )
{
	printf( "Case #%d: %d\n", n, Result );
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
