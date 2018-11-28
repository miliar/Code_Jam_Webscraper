#include <stdio.h>
#include <string.h>

const char wcj[] = "welcome to code jam";

char str[512];

int search( const char src[], const char dst[] )
{
	int i;
	int num = 0;
	int con;

	if( *src == '\0' || *dst == '\0' )
		{
		return 0;
		}//end if

	for( i = 0; dst[i] != '\0'; ++i )
		{
		if( *src == dst[i] )
			{
			for( con = 1; dst[i+1] == dst[i]; ++con, ++i );//end for
			if( src[1] == '\0' )
				{
				num += con;
				}
			else if( dst[1] != '\0' )
				{
				num += con * search( src + 1, dst + i + 1 );
				}//end if
			}//end if
		}//end for

	return num;
}//end search

int main()
{
	int n;
	int ni;

	freopen( "C.in", "r", stdin );
	freopen( "C.out", "w", stdout );

	for( ni = 1, scanf( "%d\n", &n ); ni <= n; ++ni )
		{
		gets( str );

		printf( "Case #%d: %04d\n", ni, search( wcj, str ) );
		}//end for

	return 0;
}