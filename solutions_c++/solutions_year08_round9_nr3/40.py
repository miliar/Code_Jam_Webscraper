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
int a[7][7], f[7][7];

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		fprintf( stderr, "%d\n", t );
		scanf( "%d %d", &n, &m );
		fi( n ) fj( m ) scanf( "%d", &a[i][j] );

		int ans = 0;
		fi( 1 << ( n * m ) )
		{
			int id = 0;
			int mid = 0;
			fj( n ) fk( m ) f[j][k] = 0;
			fj( n ) fk( m ) 
			{
				if( ( i & ( 1 << id ) ) )
				{
					for( int x = j - 1; x <= j + 1; ++ x )if( x >= 0 && x < n )
						for( int y = k - 1; y <= k + 1; ++ y )if( y >= 0 && y < m )
							++ f[x][y];
							
					if( j + j + 1 == n ) ++ mid;
				}
				++ id;
			}

			bool ok = true;
			fj( n ) fk( m ) if( f[j][k] != a[j][k] ) { ok = false; break; }
			if( ok ) ans = max( ans, mid );
		}

		printf( "Case #%d: %d\n", t, ans );
	}

	return 0;
}
