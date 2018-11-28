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

int n, m;
char buf[100];
int x, y, dir;
int mnx[6006], mny[6005];
int mxx[6006], mxy[6005];
int s;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int main( )
{
	int i, j, k, tt, t;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );

	for( tt = 1; tt <= t; ++ tt )
	{
		scanf( "%d", &n );
		memset( mny, 0x7f, sizeof( mny ) );
		memset( mnx, 0x7f, sizeof( mnx ) );
		memset( mxy, 0, sizeof( mxy ) );
		memset( mxx, 0, sizeof( mxx ) );
		s = 0;
		x = 3002;
		y = 3002;
		dir = 0;
		fi( n )
		{
			scanf( "%s %d", buf, &k );
			int l = strlen( buf );
			fj( k )
			{
				int z;
				fr( z, l )
				{
					if( buf[z] == 'R' ) ( ++ dir ) %= 4;
					else if( buf[z] == 'L' ) ( dir += 3 ) %= 4;
					else
					{
						if( dir == 0 ) s += x;
						else if( dir == 2 ) s -= x;
						if( dir == 0 )
						{
							mnx[y] = min( mnx[y], x );
							mxx[y] = max( mxx[y], x );
						}
						if( dir == 1 )
						{
							mny[x] = min( mny[x], y );
							mxy[x] = max( mxy[x], y );
						}
						x += dx[dir]; y += dy[dir];
						if( dir == 2 )
						{
							mnx[y] = min( mnx[y], x );
							mxx[y] = max( mxx[y], x );
						}
						if( dir == 3 )
						{
							mny[x] = min( mny[x], y );
							mxy[x] = max( mxy[x], y );
						}
					}
				}
			}
		}

		int ans = 0;
		fi( 6005 ) fj( 6005 ) if( i >= mnx[j] && i < mxx[j] || j >= mny[i] && j < mxy[i] ) ++ ans;
		ans -= abs( s );
		printf( "Case #%d: %d\n", tt, ans );
	}

	return 0;
}
