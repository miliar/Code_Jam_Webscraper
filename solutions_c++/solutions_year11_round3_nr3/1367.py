#include <vector>
#include <stdio.h>
#include <string>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <memory.h>
#include <iostream>
#include <math.h>
using namespace std;

#define filein "test"

void prepare( )
{
	freopen( filein ".in", "r", stdin );
	freopen( filein ".out", "w", stdout );
}

const int MAXN = 10101;
typedef long long lint;

lint gcd( lint a, lint b )
{
	lint c;
	while ( b != 0 )
	{
		c = b;
		b = a % b;
		a = c;
	}
	return a;
}

lint findDiv( lint g, lint q, lint l, lint h )
{
	lint res;
	if ( g % q != 0 )
		return -1;
	l = ( l + q - 1 ) / q;
	h = h / q;
	g /= q;
	//	printf( "\tdbg\t\tl = %lld g = %lld q = %lld h = %lld\n", l, g, q, h );
	if ( g == 0 )
		return l * q;
	lint i;
	for ( i = l; i <= h && i <= g; i++ )
	{
	//	printf( "%lld %% %lld = %lld\n", g, i, g % i );
		if ( g % i == 0 )
			return i * q;
	}
	return -1;
}

lint a[MAXN];
lint g[MAXN];
lint q[MAXN];

lint foolsolve( )
{
	lint n, i, l, h, k;
	cin >> n >> l >> h;
	for ( i = 0; i < n; i++ )
		cin >> a[i];
	if ( l <= 1 )
		return 1;
	for ( i = l; i <= h; i++ )
	{
		for ( k = 0; k < n; k++ )
		{
			if ( a[k] % i != 0 && i % a[k] != 0 )
				break;
		}
		if ( k == n )
			return i;
	}
	return -1;
}

lint solve( )
{
	//return foolsolve( );
	
	int n, i, k;
	lint l, h;
	cin >> n >> l >> h;
	for ( i = 0; i < n; i++ )
		cin >> a[i];
	a[n++] = 1;
	if ( l <= 1 )
		return 1;
	sort( a, a + n );
	n = unique( a, a + n ) - a;
	g[n] = 0;
	for ( i = n - 1; i >= 0; i-- )
	{
		g[i] = gcd( g[i + 1], a[i] );
		//printf( "\t\t\tg[%d] = %lld\n", i, g[i] );
	}
	q[0] = 1;
	lint z;
	lint res = -1;
	for ( i = 0; i < n; i++ )
	{
		if (i > 0)
		{
			q[i] = q[i - 1] / gcd( q[i - 1], a[i] );
			if ( (long double)q[i] * a[i] > h + 1 )
				return res;
		}
		q[i] *= a[i];
		//printf( "\ta[%d] = %lld\n", i, a[i] );
		//printf( "\tq[%d] = %lld\n", i, q[i] );
		//printf( "\t\tg[%d] = %lld\n", i + 1, g[i + 1] );
		z = findDiv( g[i + 1], q[i], l, h );
		//printf( "\tl = %lld, z = %lld, h = %lld\n", l, z, h );
		if ( z >= l && z <= h )
		{
			if ( res == -1 || res > z )
				res = z;
		}
	}
	return res;
}

int main( )
{
	int t, i;
	lint res;
	scanf( "%d\n", &t );
	for ( i = 0; i < t; i++ )
	{
		printf( "Case #%d: ", i + 1 );
		res = solve( );
		if ( res < 0 )
			cout << "NO" << endl;
		else
			cout << res  << endl;
	}
	return 0;
}














