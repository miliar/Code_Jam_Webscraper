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
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

int n, m;
int cur;

set< pair< int, int > > st;
bool exist( int x, int y )
{
	return st.find( mp( x, y ) ) != st.end( );
}

void change( int x, int y, bool state )
{
	if( state ) st.insert( mp( x, y ) );
	else st.erase( mp( x, y ) );
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		fprintf( stderr, "%d\n", t );
		printf( "Case #%d:", t );
		n = ni( );
		vector< pair< int, int > > v[2];
		cur = 1;
		st.clear( );
		fi( n )
		{
			int x1 = ni( );
			int y1 = ni( );
			int x2 = ni( );
			int y2 = ni( );
			for( int x = x1; x <= x2; ++ x )
				for( int y = y1; y <= y2; ++ y )
				{
					v[0].pb( mp( x, y ) );
				}
		}
		cur = 0;
		int ans = 0;
		while( v[cur].size( ) )
		{
			++ ans;
			st.clear( );
			v[1 - cur].clear( );
			fi( v[cur].size( ) ) change( v[cur][i].first, v[cur][i].second, true );
			fi( v[cur].size( ) )
			{
				int x = v[cur][i].first;
				int y = v[cur][i].second;
				if( !exist( x - 1, y ) && !exist( x, y - 1 ) ) ;
				else v[1 - cur].pb( mp( x, y ) );

				if( !exist( x + 1, y ) && exist( x + 1, y - 1 ) )
				{
					v[1 - cur].pb( mp( x + 1, y ) );
				}
			}

			cur = 1 - cur;
		}
		printf( " %d\n", ans );
	}

	return 0;
}
