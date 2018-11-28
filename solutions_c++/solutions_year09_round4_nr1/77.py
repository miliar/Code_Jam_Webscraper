#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

using namespace std;

int n;
char f[105][105];
int a[105];

int main( )
{
	int i, j, k, t, tt;

	freopen( "moo.in", "r", stdin );
	freopen( "moo.out", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		scanf( "%d", &n );
		fi( n ) scanf( "%s", f[i] );
		_( a, 0 );
		int ans = 0;
		fi( n ) fj( n ) if( f[i][j] == '1' ) a[i] = j;
		fi( n )
		{
			if( a[i] > i )
			{
				for( j = i + 1; a[j] > i; ++ j ) ;
				int q = a[j];
				for( ; j > i; -- j ) a[j] = a[j - 1], ++ ans;
				a[i] = q;
			}
		}
		printf( "Case #%d: %d\n", t, ans );
	}

	return 0;
}
