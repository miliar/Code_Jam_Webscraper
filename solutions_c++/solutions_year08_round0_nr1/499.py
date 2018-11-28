#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <cmath>
#include <cassert>
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
#define all(v) (v).begin( )
#define pb push_back
#define mp make_pair

int n, m;
char buf[10005];

int main( )
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	int i, j, k, t, tt;

	scanf( "%d", &t );

	for( tt = 1; tt <= t; ++ tt )
	{
		scanf( "%d\n", &n );

		map< string, int > mm;
		fi( n )
		{
			gets( buf );
			mm[buf] = i;
		}

		vector< int > v1( n );
		vector< int > v2( n );

		scanf( "%d\n", &m );
		fi( m )
		{
			int a;
			v2 = v1;

			gets( buf );
			if( mm.find( buf ) == mm.end( ) ) a = -1;
			else a = mm[buf];

			int mn = 1000000;
			fj( n )
				mn = min( mn, v2[j] );
			fj( n )
				v1[j] = min( v1[j], mn + 1 );
			if( a != -1 ) v1[a] = 1000000;
		}
		int mn = 1000000;
		fj( n )
			mn = min( mn, v1[j] );

		printf( "Case #%d: %d\n", tt, mn );
	}

	fclose( stdout );

	return 0;
}
