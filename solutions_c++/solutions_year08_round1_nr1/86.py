#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <cmath>
#include <cassert>
#include <sstream>
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

const int maxn = 1000;

int n, m;
long long a[maxn];
long long b[maxn];

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );
	for( tt = 1; tt <= t; ++ tt )
	{
		scanf( "%d", &n );
		fi( n ) scanf( "%lld", &a[i] );
		fi( n ) scanf( "%lld", &b[i] );

		sort( a, a + n );
		sort( b, b + n );

		long long ret = 0;
		fi( n ) ret += a[i] * b[n - i - 1];

		printf( "Case #%d: %lld\n", tt, ret );
	}

	return 0;
}
