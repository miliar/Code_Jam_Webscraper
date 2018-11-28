#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

static const int MAXLEN = 200;

int T;
char Str[ MAXLEN + 1 ];

void Read()
{
	scanf( "%s", Str );
}

char Result[ MAXLEN + 1 ];

void Work()
{
	strcpy( Result, Str );
	if( !next_permutation( Result, Result + strlen( Result ) ) )
	{
		strcpy( Result, Str );
		reverse( Result, Result + strlen( Result ) );
		strcat( Result, "0" );
		reverse( Result, Result + strlen( Result ) );
		next_permutation( Result, Result + strlen( Result ) );
	}
}

void Write( int t )
{
	printf( "Case #%d: %s\n", t, Result );
}

int main()
{
	int i;
	scanf( "%d", &T );
	for( i = 0; i < T; ++i )
	{
		Read();
		Work();
		Write( i + 1 );
	}
	return 0;
}
