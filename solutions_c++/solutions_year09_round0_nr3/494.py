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

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

using namespace std;

const int mod = 10000;

int n, m;
char w[] = "welcome to code jam";
char buf[505];
int l, ll;
int d[505][100];

int main( )
{
	int i, j, k, t, tt;

	freopen( "moo.in", "r", stdin );
	freopen( "moo.out", "w", stdout );

	ll = strlen( w );
	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		gets( buf );
		l = strlen( buf );
		memset( d, 0, sizeof( d ) );
		if( l && buf[0] == 'w' ) d[0][0] = 1;
		fi( l ) if( i )
		{
			fj( ll ) d[i][j] = d[i - 1][j];
			if( buf[i] == 'w' ) ( d[i][0] += 1 ) %= mod;
			fj( ll ) if( j ) if( buf[i] == w[j] ) ( d[i][j] += d[i - 1][j - 1] ) %= mod;
		}
		printf( "Case #%d: ", t );
		if( d[l - 1][ll - 1] < 1000 ) printf( "0" );
		if( d[l - 1][ll - 1] < 100 ) printf( "0" );
		if( d[l - 1][ll - 1] < 10 ) printf( "0" );
		printf( "%d\n", d[l - 1][ll - 1] );
	} /**/

	return 0;
}
