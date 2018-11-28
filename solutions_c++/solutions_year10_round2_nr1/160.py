#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cctype>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <ctime>
using namespace std;

static const int MAXLEN = 111;
static const int MAXN = 111;
static const int MAXM = 111;

int N, M;

void Read()
{
	scanf( "%d%d\n", &N, &M );
}

class cList
{
public:
	map< string, cList * > Dir;
	int Create( const char dir[] );
};

cList List[ ( MAXM + MAXN ) * ( MAXM + MAXN ) / 2 + 1 ];
int Size;

int cList::Create( const char dir[] )
{
	static char buf[ MAXLEN + 1 ];
	int n;
	if( sscanf( dir, "/%[^/]%n", buf, &n ) != 1 )
		return 0;
	if( Dir.find( buf ) != Dir.end() )
		return Dir[ buf ]->Create( dir + n );
	Dir.insert( make_pair( buf, List + Size++ ) );
	return Dir[ buf ]->Create( dir + n ) + 1;
}

cList &Root = List[ 0 ];

int Result;

void Work()
{
	int i;
	static char dir[ MAXLEN + 1 ];

	for( i = 0; i < sizeof( List ) / sizeof( *List ); ++i )
	{
		List[ i ].Dir.clear();
	}
	Size = 1;

	for( i = 0; i < N; ++i )
	{
		gets( dir );
		Root.Create( dir ); 
	}
	Result = 0;
	for( i = 0; i < M; ++i )
	{
		gets( dir );
		Result += Root.Create( dir );
	}
}

void Write( int test )
{
	printf( "Case #%d: %d\n", test, Result );
}

int T;

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

