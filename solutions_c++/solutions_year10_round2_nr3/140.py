#pragma comment( linker, "/stack:128000000" )
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>

void prepare( )
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
}

#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <deque>

using namespace std;

#define fo(a,b,c) for(a =(b);a<(c);++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define _(a,b) memset((a),(b),sizeof(a))
#define __(a) _((a),0)

typedef long long lint;

const lint MOD = 100003;
const int MAXN = 505;
int n, m;

lint c[MAXN][MAXN];

lint C( int n, int m )
{
	if ( n < 0 || m < 0 )
		return 0;
	if ( c[n][m] >= 0 )
		return c[n][m];
	if ( m > n )
		return c[n][m] = 0;
	if ( n == 0 || m == 0 )
		return c[n][m] = 1;
	return c[n][m] = ( C( n - 1, m ) + C( n - 1, m - 1 ) ) % MOD;
}

lint dp[MAXN][MAXN];

lint getAns( int n, int m )
{
	lint &res = dp[n][m]; 
	if ( res >= 0 )
		return res;
	if ( n == 1 )
	{
		if ( m == 0 )
			return res = 1;
		else
			return res = 0;
	}
	if ( m >= n )
		return res = 0;
	if ( m == 0 )
		return res = 0;
	if ( m == 1 )
		return res = 1;
	res = 0;
	int i;
	fi( m - 1 )
	{
		res += ( getAns( m, i + 1 ) * C( n - m - 1, m - i - 2 ) ) % MOD;
	}
	return res %= MOD;
}

int main( )
{
	prepare( );
	int i, j, k;
	int t, tn;
	cin >> tn;
	_( dp, -1 );
	_( c, -1 );
	fr( t, tn )
	{
		scanf( "%d", &n );
		lint ans = 0;
		fi( n ) if ( i )
		{
			ans += getAns( n, i );
		}
		ans %= MOD;
		printf( "Case #%d: %d\n", t + 1, ans );
	}
	return 0;
}