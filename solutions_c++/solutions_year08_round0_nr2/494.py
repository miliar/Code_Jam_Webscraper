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
#define all(v) (v).begin( ), (v).end( )
#define pb push_back
#define mp make_pair

int n, m;

int main( )
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	int i, j, k, t, tt;

	scanf( "%d", &t );

	for( tt = 1; tt <= t; ++ tt )
	{
		int tm;
		scanf( "%d", &tm );
		scanf( "%d %d", &n, &m );

		vector< pair< int, int > > v[2];

		fi( n )
		{
			int a, b, c, d;
			scanf( "%d:%d %d:%d", &a, &b, &c, &d );
			v[0].pb( mp( a * 60 + b, c * 60 + d ) );
		}

		fi( m )
		{
			int a, b, c, d;
			scanf( "%d:%d %d:%d", &a, &b, &c, &d );
			v[1].pb( mp( a * 60 + b, c * 60 + d ) );
		}

		sort( all( v[0] ) );
		sort( all( v[1] ) );

		vector< int > a, b;

		int a1 = 0, a2 = 0;

		fi( n ) a.pb( v[0][i].second );
		fi( m ) b.pb( v[1][i].first );

		sort( all( a ) );
		sort( all( b ) );

		j = 0;
		fi( m ) if( j < n && b[i] >= a[j] + tm ) ++ j; else ++ a1;

		a.clear( );
		b.clear( );

		fi( n ) a.pb( v[0][i].first );
		fi( m ) b.pb( v[1][i].second );

		sort( all( a ) );
		sort( all( b ) );

		j = 0;
		fi( n ) if( j < m && a[i] >= b[j] + tm ) ++ j; else ++ a2;

		printf( "Case #%d: %d %d\n", tt, a2, a1 );
	}

	fclose( stdout );

	return 0;
}
