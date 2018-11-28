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

const int maxt = 10005;

string ts[maxt];
double val[maxt];
int tl[maxt];
int tr[maxt];
int pos;
char c;
char buf[1005];

void getC( )
{
	scanf( "%c", &c );
	while( c == ' ' || c == '\n' || c == '\r' )scanf( "%c", &c );
}

int gett( )
{
	int id = pos;
	++ pos;
	assert( c == '(' );
	scanf( "%lf", &val[id] );
	getC( );
	if( c == ')' )
	{
		tl[id] = -1;
	}
	else
	{
		ts[id] = "";
		do
		{
			ts[id].pb( c );
			getC( );
		} while( c != '(' );
		tl[id] = gett( ); getC( );
		tr[id] = gett( ); getC( );
	}
	return id;
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "moo.in", "r", stdin );
	freopen( "moo.out", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d:\n", t );
		int dummy;
		scanf( "%d", &dummy );
		pos = 0;
		getC( );
		gett( );
		assert( pos < maxt );
		int n;
		scanf( "%d", &n );
		fi( n )
		{
			set< string > params;
			scanf( "%s", buf );
			int m;
			scanf( "%d", &m );
			fj( m ) { scanf( "%s", buf ); params.insert( buf ); }
			int pos = 0;
			double p = 1;
			while( 1 )
			{
				p *= val[pos];
				if( tl[pos] != -1 )
				{
					if( params.find( ts[pos] ) != params.end( ) )
						pos = tl[pos];
					else pos = tr[pos];
				}
				else break;
			}
			printf( "%.18lf\n", p );
		}
	}

	return 0;
}
