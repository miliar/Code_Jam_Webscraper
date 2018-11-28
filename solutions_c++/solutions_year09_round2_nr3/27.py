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

const int maxn = 25;

char f[maxn][maxn];
int d[maxn][maxn][1025];

int nval( int x, int y, int l, char sg )
{
	if( sg == '+' ) return l;
	else if( sg == '-' ) return max( 0, l - f[x][y] - f[x][y] + '0' + '0' );
	else return min( 1024, l + sg - '0' );
	return l;
}

int nval2( int x, int y, int l, char sg )
{
	if( sg == '-' ) return l + f[x][y] + f[x][y] - '0' - '0';
	if( sg == '+' ) return l;
	return l - sg + '0';
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "moo.in", "r", stdin );
	freopen( "moo.out", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		fprintf( stderr, "%d\n", t );
		int n, m;
		printf( "Case #%d:\n", t );
		scanf( "%d %d", &n, &m );
		fi( n ) scanf( "%s", f[i] );
		_( d, 127 );
		vector< pair< pair< int, int >, int > > q;
		fi( n ) fj( n ) if( f[i][j] >= '0' && f[i][j] <= '9' )
		{
			d[i][j][510 + f[i][j] - '0'] = 1;
			q.pb( mp( mp( i, j ), 510 + f[i][j] - '0' ) );
		}
		fi( q.size( ) )
		{
			//fprintf( stderr, "%d ", q.size( ) );
			int x = q[i].first.first;
			int y = q[i].first.second;
			int l = q[i].second; if( l == 0 || l == 1024 ) continue;
			if( x && d[x - 1][y][nval( x, y, l, f[x - 1][y] )] >= 1000000 )
			{
				d[x - 1][y][nval( x, y, l, f[x - 1][y] )] = d[x][y][l] + 1;
				q.pb( mp( mp( x - 1, y ), nval( x, y, l, f[x - 1][y] ) ) );
			}
			if( y && d[x][y - 1][nval( x, y, l, f[x][y - 1] )] >= 1000000 )
			{
				d[x][y - 1][nval( x, y, l, f[x][y - 1] )] = d[x][y][l] + 1;
				q.pb( mp( mp( x, y - 1 ), nval( x, y, l, f[x][y - 1] ) ) );
			}
			if( x < n - 1 && d[x + 1][y][nval( x, y, l, f[x + 1][y] )] >= 1000000 )
			{
				d[x + 1][y][nval( x, y, l, f[x + 1][y] )] = d[x][y][l] + 1;
				q.pb( mp( mp( x + 1, y ), nval( x, y, l, f[x + 1][y] ) ) );
			}
			if( y < n - 1 && d[x][y + 1][nval( x, y, l, f[x][y + 1] )] >= 1000000 )
			{
				d[x][y + 1][nval( x, y, l, f[x][y + 1] )] = d[x][y][l] + 1;
				q.pb( mp( mp( x, y + 1 ), nval( x, y, l, f[x][y + 1] ) ) );
			}
		}
		fk( m )
		{
			int a;
			scanf( "%d", &a );
			a += 510;
			int mx = 1000000; char mxc;
			vector< pair< int, int > > q;
			fi( n ) fj( n ) if( f[i][j] >= '0' && f[i][j] <= '9' && d[i][j][a] < mx || d[i][j][a] == mx && f[i][j] >= '0' && f[i][j] <= '9' && f[i][j] < mxc )
			{
				mx = d[i][j][a];
				mxc = f[i][j];
			}
			fi( n ) fj( n ) if( d[i][j][a] == mx && f[i][j] == mxc ) q.pb( mp( i, j ) );
			printf( "%c", mxc );
//			a -= mxc - '0';
			while( 1 )
			{
				mxc = '9';
				bool stop = false;
				fi( q.size( ) )
				{
					int x = q[i].first;
					int y = q[i].second;
					if( f[x][y] >= '0' && f[x][y] <= '9' && f[x][y] - '0' == a - 510 )
					{
						stop = true;
						break;
					}
					if( x && d[x - 1][y][nval2( x - 1, y, a, f[x][y] )] == d[x][y][a] - 1 && f[x - 1][y] < mxc ) mxc = f[x - 1][y];
					if( y && d[x][y - 1][nval2( x, y - 1, a, f[x][y] )] == d[x][y][a] - 1 && f[x][y - 1] < mxc ) mxc = f[x][y - 1];
					if( x < n - 1 && d[x + 1][y][nval2( x + 1, y, a, f[x][y] )] == d[x][y][a] - 1 && f[x + 1][y] < mxc ) mxc = f[x + 1][y];
					if( y < n - 1 && d[x][y + 1][nval2( x, y + 1, a, f[x][y] )] == d[x][y][a] - 1 && f[x][y + 1] < mxc ) mxc = f[x][y + 1];
				}
				if( !stop )
				{
					printf( "%c", mxc );
					vector< pair< int, int > > nq;
					int na;
					fi( q.size( ) )
					{
						int x = q[i].first;
						int y = q[i].second;
						if( x && d[x - 1][y][nval2( x - 1, y, a, f[x][y] )] == d[x][y][a] - 1 && f[x - 1][y] == mxc ) { nq.pb( mp( x - 1, y ) ); na = nval2( x - 1, y, a, f[x][y] ); }
						if( y && d[x][y - 1][nval2( x, y - 1, a, f[x][y] )] == d[x][y][a] - 1 && f[x][y - 1] == mxc ) { nq.pb( mp( x, y - 1 ) ); na = nval2( x, y - 1, a, f[x][y] ); }
						if( x < n - 1 && d[x + 1][y][nval2( x + 1, y, a, f[x][y] )] == d[x][y][a] - 1 && f[x + 1][y] == mxc ) { nq.pb( mp( x + 1, y ) ); na = nval2( x + 1, y, a, f[x][y] ); }
						if( y < n - 1 && d[x][y + 1][nval2( x, y + 1, a, f[x][y] )] == d[x][y][a] - 1 && f[x][y + 1] == mxc ) { nq.pb( mp( x, y + 1 ) ); na = nval2( x, y + 1, a, f[x][y] ); }
					}
					a = na;
					sort( all( nq ) );
					nq.resize( unique( all( nq ) ) - nq.begin( ) );
					q = nq;
				} else break;
			}/**/
			printf( "\n" );
		}
	}

	return 0;
}
