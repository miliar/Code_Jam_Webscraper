#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>

using namespace std;

#define FOR( i, a, b ) for( i = a; i < b; ++i )
#define FORN( i, a, b ) for( i = a; i <= b; ++i )

#define sint(x) scanf( "%d", &x )
#define sdouble(x) scanf( "%lf", &x )
#define sint64(x) scanf( "%I64d", &x )
#define pint(x) printf(  "%d ", x )
#define pintn(x) printf( "%d\n", x )

typedef long long ll;
typedef unsigned long long ull;

const int maxn = 1100000;
double a[ maxn ];
double pcorr[ maxn ];

double solve()
{
	int i;
	int k, n;
	sint( k );
	sint( n );
	double p = 1;
	FOR( i, 0, k )
	{
		sdouble( a[ i ] );
		p *= a[ i ];
		pcorr[ i ] = p;
	}
	double ans = n + 2;
	FORN( i, 1, k )
		ans = min( ans, 2 * ( k - i ) + n - k + 1 +  ( 1 - pcorr[ i - 1 ] ) * ( n + 1 ) );
	return ans;

}

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	int t;
	cin >> t;
	for( int i = 1; i <= t; ++i )
	{
//	cout << "x ";
		printf("Case #%d: %.6lf\n", i, solve()); 
	}
	return 0;
}

