#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char str[24];
char res[24];

int main()
{
	int t;
	int ti;
	int i;

	freopen( "B.in", "r", stdin );
	freopen( "B.out", "w", stdout );

	for( scanf( "%d", &t ), ti = 1; ti <= t; ++ti )
		{
		scanf( "%s", str );
		strcpy( res, str );
		next_permutation( res, res + strlen( res ) );
		if( strcmp( res, str ) <= 0 )
			{
			res[0] = '0';
			strcpy( res + 1, str );
			next_permutation( res, res + strlen( res ) );
			if( res[0] == '0' )
				{
				for( i = 0; res[i] == '0'; ++i );//end for
				res[0] = res[i];
				res[i] = '0';
				}//end if
			}//end if
		printf( "Case #%d: %s\n", ti, res );
		}//end for
	return 0;
}