#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>

using namespace std;

char str[64];
int map[128];

int main()
{
	int t, ti;
	int rad;
	int i;
	bool zero;
	long long res;

	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	for( scanf( "%d", &t ), ti = 1; ti <= t; ++ti )
		{
		scanf( "%s", str );
		memset( map, -1, sizeof( map ) );
		rad = 1;
		map[str[0]] = 1;
		zero = false;
		for( i = 1; str[i] != '\0'; ++i )
			{
			if( map[str[i]] < 0 )
				{
				if( !zero )
					{
					map[str[i]] = 0;
					zero = true;
					}
				else{
					++rad;
					map[str[i]] = rad;
					}
				}//end if
			}//end for
		++rad;
		res = 0;
		for( i = 0; str[i] != '\0'; ++i )
			{
			res = rad * res + map[str[i]];
			}//end for
		printf( "Case #%d: %lld\n", ti, res );
		}//end for
	return 0;
}

