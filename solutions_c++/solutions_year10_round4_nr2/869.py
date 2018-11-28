// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen( "in.txt", "r", stdin); 
	freopen( "out.txt", "w", stdout); 
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i )
#define fi( a ) for ( int i = 0; i < ( a ); ++i )
#define fj( a ) for ( int j = 0; j < ( a ); ++j )
#define fk( a ) for ( int k = 0; k < ( a ); ++k )
#define CLR( a, b ) memset( ( a ), ( b ), sizeof ( a ) )
#define clr( a ) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(), ( v ).end()

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = ( 1 << 30 );

bool mark[1 << 13];

void rec( int v, int le, int ri, int ost, int id )
{
	int e = ( le + ri ) / 2;
	if ( ost == 0 ) return;
	mark[v] = true;
	if ( id <= e )
		rec( 2*v, le, e, ost-1, id );
	else
		rec( 2*v  + 1, e+1, ri, ost-1, id );
}

vector < pii > v;

void solve()
{
	int p;
	v.clear();
	scanf("%d", &p );
	fi( 1 << p )
	{
		int x;
		scanf("%d", &x );
		v.pb( mp( p - x, i ) );
	}
	for ( int i = 0; i < p; ++i )
	{
		int y;
		fj( 1 << i )
			scanf("%d", &y );
	}
	sort( all( v ) );
	reverse( all( v ) );
	clr( mark );
	fi( v.size() )
		rec( 1, 0, ( 1 << p ) - 1, v[i].first, v[i].second );
	int ret = 0;
	fi( 1 << 13 )
		if ( mark[i] )
			++ret;
	printf("%d\n", ret );
}

int main()
{
	initf();
	int t;
	scanf("%d", &t );
	fi( t )
	{
		printf("Case #%d: ", i + 1 );
		solve();	
	}
	return ( 0 );
}
