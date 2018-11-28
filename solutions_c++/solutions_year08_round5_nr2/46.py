#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <cmath>
#include <cassert>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <deque>
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

struct state_t
{
	char x, y;
	char wx, wy, ws;
	char qx, qy, qs;
	int l;
};

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int n, m;
char f[maxn][maxn];
int sx, sy, ex, ey;

bool p[maxn][maxn][maxn][maxn][4][maxn][maxn][4];
deque< state_t > q;

int curl;
void add( char x, char y, char wx, char wy, char ws, char qx, char qy, char qs, int l )
{
	if( p[x][y][wx][wy][ws][qx][qy][qs] ) return;
	p[x][y][wx][wy][ws][qx][qy][qs] = 1;

	state_t moo;
	moo.x = x;
	moo.y = y;
	moo.wx = wx;
	moo.wy = wy;
	moo.ws = ws;
	moo.qx = qx;
	moo.qy = qy;
	moo.qs = qs;
	moo.l = l;

	curl = max( l, curl );

	if( l == curl ) q.push_back( moo );
	else q.push_front( moo );
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );
	for( tt = 1; tt <= t; ++ tt )
	{
		scanf( "%d %d", &n, &m );
		memset( f, '#', sizeof( f ) );
		fi( n ) scanf( "%s", &f[i + 1][1] );

		n += 2;
		m += 2;

		fi( n ) fj( m )
		{
			if( f[i][j] == 'O' )
			{
				sx = i;
				sy = j;
				f[i][j] = '.';
			}
			if( f[i][j] == 'X' )
			{
				ex = i;
				ey = j;
				f[i][j] = '.';
			}
			if( !f[i][j] ) f[i][j] = '#';
		}

		curl = 0;
		q.clear( );
		memset( p, 0, sizeof( p ) );

		add( sx, sy, 10, 0, 0, 10, 0, 0, 0 );
		while( q.size( ) )
		{
			state_t cur = q.front( );
			q.pop_front( );
			if( cur.x == ex && cur.y == ey )
			{
				printf( "Case #%d: %d\n", tt, cur.l );
				goto e;
			}

			fj( 4 ) // dir
			{
				// move
#define dir j
				int nx = cur.x + dx[j];
				int ny = cur.y + dy[j];
				if( f[nx][ny] == '.' ) add( nx, ny, cur.wx, cur.wy, cur.ws, cur.qx, cur.qy, cur.qs, cur.l + 1 );
				else if( cur.wx == nx && cur.wy == ny && cur.ws == ( dir + 2 ) % 4 && cur.qx != 10 )
				{
					if( f[cur.qx + dx[cur.qs]][cur.qy + dy[cur.qs]] == '#' )
					{
						printf( "%d %d %d\n", (int)cur.qx, (int)cur.qy, (int)cur.qs );
						return 0;
					}
					add( cur.qx + dx[cur.qs], cur.qy + dy[cur.qs], cur.wx, cur.wy, cur.ws, cur.qx, cur.qy, cur.qs, cur.l + 1 );
				}

				// shoots
				int xx = cur.x + dx[j], yy = cur.y + dy[j];
				while( f[xx][yy] != '#' ) xx += dx[j], yy += dy[j];
				add( cur.x, cur.y, xx, yy, ( dir + 2 ) % 4, cur.qx, cur.qy, cur.qs, cur.l );
				add( cur.x, cur.y, cur.wx, cur.wy, cur.ws, xx, yy, ( dir + 2 ) % 4, cur.l );
			}
		}
		printf( "Case #%d: THE CAKE IS A LIE\n", tt );
e:;
	}

	return 0;
}
