#include <stdio.h>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <set>
#include <map>

using namespace std;

#define fo(a,b,c) for( ( a ) = ( b ); ( a ) < ( c ); ++ ( a ) )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

const int maxn = 10005;

int n, m;
int isAnd[maxn];
int isChg[maxn];
int moo[maxn][2];

int andop( int v1, int v2, int an, int ch )
{
	int ret = 0;
	if( !an && !ch ) return -1;
	if( v1 == -1 || v2 == -1 ) return -1;
	ret = v1 + v2;
	if( !an ) ++ ret;
	return ret;
}

int orop( int v1, int v2, int an, int ch )
{
	int ret = 0;
	if( an && !ch ) return -1;
	if( v1 == -1 || v2 == -1 ) return -1;
	ret = v1 + v2;
	if( an ) ++ ret;
	return ret;
}

int smin( int a, int b )
{
	if( a == -1 ) return b;
	if( b == -1 ) return a;
	return min( a, b );
}

int mmin( int a, int b, int c, int d )
{
	return smin( smin( a, b ), smin( c, d ) );
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
		fi( ( n - 1 ) / 2 ) scanf( "%d %d", &isAnd[i + 1], &isChg[i + 1] );
		for( i = ( n - 1 ) / 2; i < n; ++ i )
		{
			int a;
			scanf( "%d", &a );
			moo[i + 1][a] = 0;
			moo[i + 1][1 - a] = -1;
		}
		
		for( i = ( n - 1 ) / 2; i >= 1; -- i )
		{
			moo[i][1] = mmin( andop( moo[i * 2][1], moo[i * 2 + 1][1], isAnd[i], isChg[i] ),
					orop( moo[i * 2][1], moo[i * 2 + 1][1], isAnd[i], isChg[i] ), 
					orop( moo[i * 2][0], moo[i * 2 + 1][1], isAnd[i], isChg[i] ), 
					orop( moo[i * 2][1], moo[i * 2 + 1][0], isAnd[i], isChg[i] ) );
			moo[i][0] = mmin( orop( moo[i * 2][0], moo[i * 2 + 1][0], isAnd[i], isChg[i] ),
					andop( moo[i * 2][0], moo[i * 2 + 1][0], isAnd[i], isChg[i] ), 
					andop( moo[i * 2][0], moo[i * 2 + 1][1], isAnd[i], isChg[i] ), 
					andop( moo[i * 2][1], moo[i * 2 + 1][0], isAnd[i], isChg[i] ) );
		}
		
		printf( "Case #%d: ", tt );
		if( moo[1][m] == -1 ) printf( "IMPOSSIBLE\n" );
		else printf( "%d\n", moo[1][m] );
	}
	
	return 0;
}
