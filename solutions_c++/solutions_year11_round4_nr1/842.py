/*
	author: AmazingCaddy
	time: 2011/6/4  21:44
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

const int maxn = 1004;
const double eps = 1e-8;

struct node
{
	int st, ed;
	int len;
	int w;
};
node wa[ maxn ];

bool cmp( const node &a, const node &b )
{
	return a.w < b.w;
}

int main(int argc, char *argv[])
{
	int X, S, R, t, n, cas, st, ed;
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	scanf( "%d", &cas );
	for( int k = 1; k <= cas; k++ )
	{
		scanf( "%d%d%d%d%d", &X, &S, &R, &t, &n );
		int sum = 0;
		for( int i = 0; i < n; i++ )
		{
			scanf( "%d%d%d", &st, &ed, &wa[ i ].w );
			wa[ i ].len = ed - st;
			sum += wa[ i ].len;
		}
		wa[ n ].len = X - sum;
		wa[ n ].w = 0;
		n++;
		sort( wa, wa + n, cmp );
		double tim = t;
		double ans = 0;
		for( int i = 0; i < n; i++ )
		{
			if( tim == 0 )
			{
				ans += wa[ i ].len * 1.0 / ( wa[ i ].w + S );
				continue;
			}
			double tmp = wa[ i ].len * 1.0 / ( wa[ i ].w + R );
			if( tmp > tim )
			{
				ans += tim;
				double d = ( wa[ i ].len - ( wa[ i ].w + R ) * tim ) / ( wa[ i ].w + S );
				ans += d;
				tim = 0;
			}
			else
			{
				tim -= tmp;
				ans += tmp;
			}
		}
		printf( "Case #%d: %.7lf\n", k, ans );
	}
	return 0;
}
