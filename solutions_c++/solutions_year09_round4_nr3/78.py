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

int n, m;
int a[105][55];
bool omg[105][105];
int d[70000];
bool okk[70000];
int main( )
{
	int i, j, k, t, tt;

	freopen( "moo.in", "r", stdin );
	freopen( "moo.out", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		fprintf( stderr, "%d\n", t );
		_( omg, 0 );
		scanf( "%d %d", &n, &m );
		fi( n ) fj( m ) scanf( "%d", &a[i][j] );
		fi( n ) fj( n ) if( i != j )
		{
			bool ok = true;
			fk( m )
			{
				if( a[j][k] <= a[i][k] ) ok = false;
			}
			if( ok ) { omg[i][j] = 1; omg[j][i] = 1; }
		}

		_( d, -1 );
		_( okk, 0 );
		d[0] = 0;
		fj( 1 << n )
		{
			bool ok = true;
			for( k = 0; k < n; ++ k ) if( j & ( 1 << k ) )
				for( int z = 0; z < k; ++ z ) if( j & ( 1 << z ) && !omg[k][z] ) ok = false;
			if( ok ) okk[j] = 1;
		}
		fi( 1 << n ) if( i )
		{
			for( j = i; ; j = ( j - 1 ) & i )
			{
				if( okk[j] )
				{
					int nv = d[i & ~j] + 1;
					if( d[i] == -1 || d[i] > nv ) d[i] = nv;
				}
				if( !j ) break;
			}
		}

		printf( "Case #%d: %d\n", t, d[( 1 << n ) - 1] );
	}

	return 0;
}
