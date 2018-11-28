#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

#define file "..\\..\\GCJ\\2012qual\\in\\c"

void prepare()
{
#ifdef _DEBUG
	freopen( "in.txt", "r", stdin );
#else
	freopen( file ".in", "r", stdin );
	freopen( file ".out", "w", stdout );
#endif
}

const int MAXN = 2000001;

vector < pair < int, int > > p;

void precalc()
{
	p.clear();
	int i, k;
	long long l = 1, p10 = 1, x;
	for ( i = 1; i < MAXN; i++ )
	{
		if ( p10 * 10 <= i )
		{
			p10 *= 10;
			l++;
		}
		x = i;
		for ( k = 1; k < l; k++ )
		{
			x = ( x % 10 ) * p10 + x / 10;
			if ( x < MAXN && x > i )
				p.push_back( make_pair( i, x ) );
		}
	}
	sort( p.begin( ), p.end( ) );
	p.resize( unique( p.begin( ), p.end( ) ) - p.begin( ) );
	sort( p.begin( ), p.end( ) );
	//fprintf( stderr, "psize=%d\n", p.size( ) );
}

bool solve()
{
	int l, r, i, res = 0;
	scanf( "%d%d", &l, &r );
	for ( i = 0; i < p.size( ); i++ )
		if ( p[i].first >=l && p[i].second <= r )
			res++;
	printf( "%d\n", res );
	return false;
}

int main()
{
	precalc( );
	prepare( );
	//solve( );
//#ifdef _DEBUG
	int tt;
	scanf( "%d", &tt );
	for (int ttt = 0; ttt < tt; ttt++)
	{
		printf( "Case #%d: ", ttt + 1 );
		solve( );
	}
//#endif
	return 0;
}