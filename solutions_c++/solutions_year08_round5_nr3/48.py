#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <cmath>
#include <cassert>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

#define fo(a,b,c) for( (a) = (b); (a) < (c); ++ (a) )
#define fr(a,b) fo( (a), 0, (b) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define all(v) (v).begin( ), (v).end( )
#define pb push_back
#define mp make_pair

const int maxn = 11;

int n, m;
char f[maxn][maxn];
int ff[maxn];
int d[1 << maxn];
int nd[1 << maxn];

int main( )
{
	int i, j, k, z, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );
	for( tt = 1; tt <= t; ++ tt )
	{
		scanf( "%d %d", &n, &m );
		fi( n )
		{
			scanf( "%s", f[i] );
			ff[i] = 0;
			fj( m ) if( f[i][j] == 'x' ) ff[i] |= ( 1 << j );
		}

		memset( d, 0, sizeof( d ) );
		d[0] = 0;
		fi( n )
		{
			memset( nd, 0, sizeof( nd ) );
			fj( 1 << m ) fk( 1 << m ) if( ( k & ff[i] ) == 0 )
			{
				int cnt = 0;
				fr( z, m ) if( k & ( 1 << z ) )
				{
					++ cnt;
					if( z && ( ( k & ( 1 << ( z - 1 ) ) ) || ( j & ( 1 << ( z - 1 ) ) ) ) )
					{
						goto e;
					}
					if( z < m - 1 && ( ( k & ( 1 << ( z + 1 ) ) ) || ( j & ( 1 << ( z + 1 ) ) ) ) )
					{
						goto e;
					}
				}
				nd[k] = max( nd[k], d[j] + cnt );
e:;
			}

			memcpy( d, nd, sizeof( d ) );
		}

		int ans = 0;
		fi( 1 << m ) ans = max( ans, d[i] );
		printf( "Case #%d: %d\n", tt, ans );
	}

	return 0;
}
