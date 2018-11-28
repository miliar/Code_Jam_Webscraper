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

const int maxn = 35;
const int max2 = 35 * 35;

int n, m;
char f[maxn][maxn];
int v[maxn][maxn];
int z[maxn][maxn];

int sm[max2][max2];
int ids[maxn][maxn];
int tx[max2];
int ty[max2];
int nn;

int sub[maxn][maxn];

int xx[4] = { -1, 0, 1, 0 };
int yy[4] = { 0, -1, 0, 1 };

void moo( int a, int b )
{
	memset( v, -1, sizeof( v ) );
	vector< pair< int, int > > q;
	q.pb( mp( a, b ) );
	v[a][b] = 0;

	int i;
	fi( q.size( ) )
	{
		int x = q[i].first;
		int y = q[i].second;
		int l = v[x][y];

		int j;
		fj( 4 )
		{
			int nx = x + xx[j];
			int ny = y + yy[j];
			if( nx >= 0 && nx < n && ny >= 0 && ny < m && f[nx][ny] != '.' && v[nx][ny] == -1 )
			{
				v[nx][ny] = l + 1;
				q.pb( mp( nx , ny ) );
			}
		}
	}
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		scanf( "%d %d", &n, &m );
		fi( n ) scanf( "%s", f[i] );

		nn = 0;
		int ans = 0;
		fi( n ) fj( m ) if( f[i][j] == 'T' )
		{
			tx[nn] = i;
			ty[nn] = j;
			ids[i][j] = nn;
			++ nn;
		}

		moo( 0, 0 );
		memcpy( z, v, sizeof( z ) );
		fi( nn ) if( i )
		{
			moo( tx[i], ty[i] );
			int dst = v[0][0];
			fk( ( dst + 1 ) / 2 ) ans = ans - ( k ) + dst - k;
		}

		fi( n ) fj( m ) if( f[i][j] != '.' ) ans += min( v[i][j], z[i][j] );

		printf( "Case #%d: %d\n", t, ans );
	}

	return 0;
}
