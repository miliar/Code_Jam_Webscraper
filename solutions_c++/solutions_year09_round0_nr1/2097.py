#include <stdio.h>
#include <string.h>
using namespace std;

const int MAXL = 15 + 10;
const int MAXD = 5000 + 10;
const int MAXN = 500 + 10;
int l, d, n;
char dictionary [ MAXD ][ MAXL ];

void init ()
{
	freopen ( "A-large.in", "r", stdin );
	freopen ( "A-large.out", "w", stdout );
	scanf ( "%d%d%d\n", &l, &d, &n );
	for ( int i = 0; i < d; i++ )
		scanf ( "%s\n", dictionary [ i ] );
}

void process ()
{
	char tmp [ 15000 ];
	int hash [ 256 ];

	for ( int i = 0; i < n; i++ )
	{
		scanf ( "%s", &tmp );
		int res = 0;

		for ( int j = 0; j < d; j++ )
		{
			int p_tmp = -1;
			int flag = 1;

			for ( int k = 0; k < l; k++ )
			{
				memset ( hash, 0, sizeof ( hash ) );
				p_tmp++;
				if ( tmp [ p_tmp ] != '(' )
				{
					hash [ tmp [ p_tmp ] ] = 1;
				}
				else
				{
					while ( tmp [ p_tmp ] != ')' )
					{
						hash [ tmp [ p_tmp ] ] = 1;
						p_tmp++;
					}
				}

				if ( !hash [ dictionary [ j ][ k ] ] )
					flag = 0;

				if ( !flag )
					break;
			}

			if ( flag )
				res++;
		}
		printf ( "Case #%d: %d\n", i + 1, res );
	}
}

int main ()
{
	init ();
	process ();
	return 0;
}

