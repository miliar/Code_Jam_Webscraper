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

static const int MAXR = 1012;
static const int MAXX = 111;
static const int MAXY = 111;

int R;
int C[ MAXX ][ MAXY ];

void Read()
{
	int i, a, b;
	scanf( "%d", &R );

	memset( C, 0, sizeof( C ) );

	for( i = 0; i < R; ++i )
	{
		int x1, y1, x2, y2;
		scanf( "%d%d%d%d", &x1, &y1, &x2, &y2 );
		for( a = x1; a <= x2; ++a )
		{
			for( b = y1; b <= y2; ++b )
			{
				C[ a ][ b ] = 1;
			}
		}
	}
}

void Init()
{
}

int Result;

int _C[ MAXX ][ MAXY ], ( *Curr )[ MAXY ] = C, ( *Prev )[ MAXY ] = _C;

void Work()
{
	int x, y;

	Curr = C;
	Prev = _C;

	for( Result = 0; ; ++Result )
	{
		bool end = true;
		for( x = 0; x < MAXX; ++x )
		{
			for( y = 0; y < MAXY; ++y )
			{
				if( Curr[ x ][ y ] != 0 )
					end = false;
			}
		}

		if( end )
			return;

		for( x = 0; x < MAXX; ++x )
		{
			for( y = 0; y < MAXY; ++y )
			{
				if( Curr[ x ][ y ] == 0 && 
					 x > 0 && Curr[ x - 1 ][ y ] != 0 && 
					 y > 0 && Curr[ x ][ y - 1 ] != 0 ||
					 Curr[ x ][ y ] == 1 &&
					 ( x > 0 && Curr[ x - 1 ][ y ] != 0 ||
					   y > 0 && Curr[ x ][ y - 1 ] != 0 ) )
					Prev[ x ][ y ] = 1;
				else
					Prev[ x ][ y ] = 0;
			}
		}

		swap( Curr, Prev );
	}
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
