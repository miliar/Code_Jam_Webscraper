#include<stdio.h>

int cnt_it(int p)
{
	int c = 0;
	while( p & 1 )
	{
		++c;
		p >>= 1;
	}
	return c;
}

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int n, s, d;
	scanf( "%d", &n );

	for( int i = 0; i < n; ++i )
	{
		printf( "Case #%d: ", i+1 );
		scanf( "%d %d", &s, &d );
		if( cnt_it( d ) >= s )
			printf( "ON\n" );
		else
			printf( "OFF\n" );
	}
	return 0;
}