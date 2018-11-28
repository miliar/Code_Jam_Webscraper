#include <stdio.h>
#include <string.h>
using namespace std;

const int MAX_WORD = 20;
const int MAX_WORD_LENGTH = 5000;
const char WORD [ MAX_WORD ] = "welcome to code jam";
int n;
int f [ MAX_WORD_LENGTH ][ MAX_WORD ];

void process ()
{
	freopen ( "C-large.in", "r", stdin );
	freopen ( "C-large.out", "w", stdout );
	char tmp [ MAX_WORD_LENGTH ];
	int test = 0;
	for ( scanf ( "%d\n", &n ); n > 0; n-- )
	{
		gets ( tmp );
		memset ( f, 0, sizeof ( f ) );
		for ( int j = 0; j < MAX_WORD; j++ )
			for ( int i = 0; i < strlen ( tmp ); i++ )
				if ( tmp [ i ] == WORD [ j ] )
				{

					if ( j - 1 >= 0 )
						for ( int k = 0; k < i; k++ )
						{
							if ( tmp [ k ] == WORD [ j - 1 ] )
							{
								f [ i ][ j ] += f [ k ][ j - 1 ];
								f [ i ][ j ] %= 10000;
							}
						}
					else
						f [ i ][ j ] = 1;
				}

		int res = 0;
		for ( int i = 0; i < strlen ( tmp ); i++ )
		{
			res += f [ i ][ 18 ];
			res %= 10000;
		}
		test++;
		printf ( "Case #%d: %04d\n", test, res );
	}
}

int main ()
{
	process ();
	return 0;
}
