#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <memory.h>
#include <assert.h>
#include <vector>
#include <string>
#include <functional>
#include <algorithm>
#include <map>
#include <set>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define pb push_back
#define mp make_pair
#define all(v) (v).begin( ), (v).end( )

using namespace std;

int n, m;
int a[10005];
int b[10005];
int c[10005];
int r[10005];

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		scanf( "%d", &n );
		fi( n )
		{
			scanf( "%d %d %d", &a[i], &b[i], &c[i] );
		}
		int ans = 0;
		fi( 10001 )
		{
			memset( r, 0, sizeof( r ) );
			fj( n ) if( a[j] <= i )
			{
				if( b[j] < 10000 - c[j] - i + 1 )
				{
					++ r[b[j]];
					-- r[10000 - c[j] - i + 1];
				}
			}
			int cur = 0;
			fj( 10001 - i )
			{
				cur += r[j];
				if( cur > ans )
					ans = cur;
			}
		}
		printf( "Case #%d: %d\n", t, ans );

	}

	return 0;
}
