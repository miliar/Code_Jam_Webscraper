#include <stdio.h>
#include <string.h>
using namespace std;

char tmp [ 100 ];
int tmp2 [ 100 ];
int hash [ 256 ];
int t, base;

void init ()
{
	gets ( tmp );
	base = 0;
	for ( int i = 0; i < 256; i++ )
		hash [ i ] = 0;
	
	for ( int i = 0; i < strlen ( tmp ); i++ )
	{
		if ( hash [ tmp [ i ] ] != 1 )
			base++;
		hash [ tmp [ i ] ] = 1;
	}
}

void process ()
{
	int d = -1;
	for ( int i = 0; i < 256; i++ )
		hash [ i ] = -1;

	hash [ tmp [ 0 ] ] = 1;
	tmp2 [ 0 ] = 1;
	for ( int i = 1; i < ( strlen ( tmp ) ); i++ )
		if ( hash [ tmp [ i ] ] == -1 )
		{
			if ( ++d == 1 )
				d++;
			hash [ tmp [ i ] ] = d;
			tmp2 [ i ] = d;
		}
		else
		{
			tmp2 [ i ] = hash [ tmp [ i ] ];
		}
		
	if ( base == 1 )
		base++;
	int res = 0;
	int b = 1;
	for ( int i = ( strlen ( tmp ) ) - 1; i >= 0; i-- )
	{
		res += tmp2 [ i ] * b;
		b *= base;
	}
	printf ( "Case #%d: %d\n", t, res );
}

int main ()
{
	freopen ( "xx.in", "r", stdin );
	freopen ( "xx.out", "w", stdout );
	int test;
	scanf ( "%d\n", &test );
	for ( t = 1; t <= test; t++ )
	{
		init ();
		process ();
	}
	return 0;
}


