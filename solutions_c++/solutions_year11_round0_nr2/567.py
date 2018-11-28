#include <string.h>
#include <stdio.h>

char comb[26][26];
bool oppo[26][26];
int num[26];
char str[128];
char list[128];

int main()
{
	freopen( "B.in", "r", stdin );
	freopen( "B.out", "w", stdout );
	
	int t, i;
	int c, d, n;
	int j, k;
	int len;
	char tmp;


	for( i = 1, scanf( "%d", &t ); i <= t; ++i )
		{
		memset( comb, 0, sizeof( comb ) );
		memset( oppo, false, sizeof( oppo ) );
		for( j = 0, scanf( "%d", &c ); j < c; ++j )
			{
			scanf( "%s", str );
			comb[str[0]-'A'][str[1]-'A'] = comb[str[1]-'A'][str[0]-'A'] = str[2];
			}//end for
		for( j = 0, scanf( "%d", &d ); j < d; ++j )
			{
			scanf( "%s", str );
			oppo[str[0]-'A'][str[1]-'A'] = oppo[str[1]-'A'][str[0]-'A'] = true;
			}//end for
		scanf( "%d", &n );
		scanf( "%s", str );
		len = 0;
		memset( num, 0, sizeof( num ) );
		for( j = 0; j < n; ++j )
			{
			list[len++] = str[j];
			++num[str[j]-'A'];
			if( len >= 2 )
				{
				tmp = comb[list[len-1]-'A'][list[len-2]-'A'];
				if( tmp )
					{
					--num[list[len-1]-'A'];
					--num[list[len-2]-'A'];
					--len;
					list[len-1] = tmp;
					++num[tmp-'A'];
					}//end if
				if( len >= 2 )
					{
					for( k = 0; k < 26; ++k )
						{
						if( num[k] > 0 && oppo[list[len-1]-'A'][k] )
							{
							len = 0;
							memset( num, 0, sizeof( num ) );
							break;
							}//end if
						}//end for
					}//end if
				}//end if
			}//end for

		printf( "Case #%d: [", i );
		if( len > 0 )
			{
			putchar( list[0] );
			if( len > 1 )
				{
				for( j = 1; j < len; ++j )
					{
					printf( ", %c", list[j] );
					}//end for
				}//end if
			}//end if
		printf( "]\n" );
		}//end for
	return 0;
}//end main