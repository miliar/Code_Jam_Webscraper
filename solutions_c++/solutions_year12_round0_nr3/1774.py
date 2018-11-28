#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int A, B;

void Read()
{
	scanf( "%d%d", &A, &B );
}

int Result;

void Work()
{
	int x, y, i;
	int mod = 1;
	int len = 0;

	while( mod <= B )
	{
		mod *= 10;
		++len;
	}

	Result = 0;

	for( x = A; x <= B; ++x )
	{
		y = x;
		for( i = 1; i < len; ++i )
		{
			y = ( y % 10 * mod + y ) / 10;
			if( y == x )
				break;
			if( x < y && y <= B )
				++Result;
		}
	}
}

void Write( int t )
{
	printf( "Case #%d: %d\n", t, Result );
}

int main()
{
	int i, t;
	scanf( "%d", &t );
	for( i = 1; i <= t; ++i )
	{
		Read();
		Work();
		Write( i );
	}
	return 0;
}
