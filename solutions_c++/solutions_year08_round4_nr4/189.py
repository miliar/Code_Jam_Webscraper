#include <stdio.h>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <set>
#include <map>

using namespace std;

#define fo(a,b,c) for( ( a ) = ( b ); ( a ) < ( c ); ++ ( a ) )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

int n, m;
char buf[50005];
char str[50005];
int p[20];

int main( )
{
	int i, j, k, tt, t;
	
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );
	
	for( tt = 1; tt <= t; ++ tt )
	{
		scanf( "%d", &m );
		scanf( "%s", buf );
		n = strlen( buf );
		int ans = 1000000000;
		fi( m ) p[i] = i;
		do
		{
			for( i = 0; i < n; i += m )
			{
				fj( m ) str[i + p[j]] = buf[i + j];
			}
			int cnt = 1;
			fi( n ) if( i ) if( str[i] != str[i - 1] ) ++ cnt;
			ans = min( ans, cnt );
		} while( next_permutation( p, p + m ) );
		
		printf( "Case #%d: %d\n", tt, ans );
	}
	
	return 0;
}
