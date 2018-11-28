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

const int maxn = 105;

int n, m;
bool p[maxn][maxn];
int w, h, dx[2], dy[2], x, y;
int ans;

void rec( int a, int b )
{
	if( a < 0 || b < 0 || a >= w || b  >= h ) return;
	if( p[a][b] ) return;
	p[a][b] = 1;
	++ ans;
	rec( a + dx[0], b + dy[0] );
	rec( a + dx[1], b + dy[1] );
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		scanf( "%d %d", &w, &h );
		fi( 2 ) scanf( "%d %d", &dx[i], &dy[i] );
		scanf( "%d %d", &x, &y );

		memset( p, 0, sizeof( p ) );
		ans = 0;
		rec( x, y );

		printf( "Case #%d: %d\n", t, ans );
	}

	return 0;
}
