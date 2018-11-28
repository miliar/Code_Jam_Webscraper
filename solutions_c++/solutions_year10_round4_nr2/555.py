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

static const int MAXP = 10;
static const int MAXTWOP = 1024;
static const int TWO[] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096 };

int P;
int M[ MAXTWOP ];
int Price[ MAXTWOP ];

void Read()
{
	int i;
	scanf( "%d", &P );
	for( i = TWO[ P ] - 1; i >= 0; --i )
	{
		scanf( "%d", &M[ i ] );
	}
	for( i = TWO[ P ] - 1; i >= 1; --i )
	{
		scanf( "%d", &Price[ i ] );
	}
}

int Count[ MAXTWOP * 2 ];
int Best[ MAXTWOP * 2 ][ MAXP + 1 ];

int Result;

void Init()
{
}

void Work()
{
	int i, j;

	memset( Best, -1, sizeof( Best ) );

	for( i = 0; i < TWO[ P ]; ++i )
	{
		Count[ TWO[ P ] + i ] = P - M[ i ];
	}
	for( i = TWO[ P ] - 1; i >= 1; --i )
	{
		Count[ i ] = max( Count[ i * 2 ], Count[ i * 2 + 1 ] );
	}

	for( i = TWO[ P + 1 ] - 1; i >= TWO[ P ]; --i )
	{
		for( j = 0; j <= P; ++j )
		{
			if( j >= Count[ i ] )
				Best[ i ][ j ] = 0;
			else
				Best[ i ][ j ] = -1;
		}
	}

	for( i = TWO[ P ] - 1; i >= 1; --i )
	{
		for( j = 0; j <= P; ++j )
		{
			int look, pass;

			if( j + 1 <= P && Best[ i * 2 ][ j + 1 ] != -1 && Best[ i * 2 + 1 ][ j + 1 ] != -1 )
				look = Price[ i ] + Best[ i * 2 ][ j + 1 ] + Best[ i * 2 + 1 ][ j + 1 ];
			else
				look = -1;

			if( Best[ i * 2 ][ j ] != -1 && Best[ i * 2 + 1 ][ j ] != -1 )
				pass = Best[ i * 2 ][ j ] + Best[ i * 2 + 1 ][ j ];
			else
				pass = -1;

			if( look != -1 && pass != -1 )
				Best[ i ][ j ] = min( look, pass );
			else if( look != -1 )
				Best[ i ][ j ] = look;
			else if( pass != -1 )
				Best[ i ][ j ] = pass;
			else
				Best[ i ][ j ] = -1;
		}	
	}

	Result = Best[ 1 ][ 0 ];
}

void Write( int test )
{
	printf( "Case #%d: %d\n", test, Result );
}

int main()
{
	int i, t;
	scanf( "%d", &t );
	Init();
	for( i = 0; i < t; ++i )
	{
		Read();
		Work();
		Write( i + 1 );
	}
	return 0;
}
