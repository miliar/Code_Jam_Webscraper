/*
	author: AmazingCaddy
	time: 2011/5/22  0:56
*/
#include <cstdio>
#include <complex>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <vector>
#include <map>
#include <queue>
using namespace std;

typedef __int64 ll;

const int maxn = 204;
const int maxm = 1000010;
const double pi = acos( -1.0 );
const double inf = 1e20;
const double eps = 1e-8;

struct node
{
	int p, v;
};
node dog[ maxn ];
double six[ maxm ];

int D( double x ) { return ( x < -eps ? -1 : x > eps ); }

bool cmp( const node & a, const node & b )
{
	return a.p < b.p;
}

int check( double x, int d, int n )
{
	six[ 0 ] = -inf;
	int len = 1;
	//double dis = d;
	for( int i = 0; i < n; i++ )
	{
		double tmp = dog[ i ].p - x;
		if( tmp < ( six[ len - 1 ] + d ) ) 
			tmp = six[ len - 1 ] + d;
		//int t = len;
		if( tmp + ( dog[ i ].v - 1 ) * d - dog[ i ].p > x ) return 0;
		six[ len++ ] = tmp + ( dog[ i ].v - 1 ) * d;
		/*
		for( int j = 0; j < dog[ i ].v; j++ )
		{
			six[ len ] = tmp;
			if( six[ len ] - )
			tmp += dis;
			if( six[ len ] < six[ t ] )
				return 0;
		}
		*/
	}
	return 1;
}

int main(int argc, char *argv[])
{
	int cas, d, c;
	freopen( "B-small-attempt1.in", "r", stdin );
	freopen( "small_B1.txt", "w", stdout );
	scanf( "%d", &cas );
	for( int t = 1; t <= cas; t++ )
	{
		scanf( "%d%d", &c, &d );
		for( int i = 0; i < c; i++ )
			scanf( "%d%d", &dog[ i ].p, &dog[ i ].v );

		sort( dog, dog + c, cmp );
		double l = 0, r = 1e5, mid;
		while( r - l > eps )
		{
			mid = ( l + r ) / 2.0;
			if( check( mid, d, c ) ) r = mid;
			else l = mid;
		}
		printf( "Case #%d: %.8lf\n", t, mid );
	}
	return 0;
}
