#define _CRT_SECURE_NO_DEPRECATE
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

typedef long long lint;
typedef long double lod;

void prepare( )
{
	#ifdef _DEBUG
		freopen( "in.txt", "r", stdin );
	#else
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	#endif
}

const int MAXN = 522;

char s[MAXN][MAXN];
char st[MAXN];

int dp[MAXN][MAXN];
set < pair < int , pair <int , int> > > a;
int m, n;

int getdp( int x, int y )
{
	if ( x < 0 || y < 0 || x >= m || y >= n )
		return -1;
	if ( s[x][y] == '2' )
		return 0;
	if ( dp[x][y] < 0 )
	{
		if ( x + 1 == m || y + 1 == n )
			dp[x][y] = 1;
		else
		if ( s[x + 1][y] == '2' || s[x + 1][y + 1] == '2' || s[x][y + 1] == '2' )
			dp[x][y] = 1;
		else
		if ( s[x + 1][y + 1] == s[x][y] && s[x][y + 1] == s[x + 1][y] && s[x][y + 1] - '0' + s[x][y] - '0' == 1 )
			dp[x][y] = min( min( getdp( x + 1, y ), getdp( x, y + 1 ) ), getdp( x + 1, y + 1 ) ) + 1;
		else
			dp[x][y] = 1;
		a.insert( make_pair( -dp[x][y], make_pair( x, y ) ) );
	}
	return dp[x][y];
}

int res[MAXN];

int iter( )
{
	static int i, k, x, y, l, t, r, b;
	x = a.begin( )->second.first;
	y = a.begin( )->second.second;
	res[dp[x][y]]++;
	t = max( x - dp[x][y], 0 );
	b = x + dp[x][y];
	l = max( y - dp[x][y], 0 );
	r = y + dp[x][y];
	for ( i = x; i < b; i++ )
		for ( k = y; k < r; k++ )
			s[i][k] = '2';
	for ( i = t; i < b; i++ )
		for ( k = l; k < r; k++ )
		{
			a.erase( make_pair( -dp[i][k], make_pair( i, k ) ) );
			dp[i][k] = -1;
		}
	for ( i = t; i < b; i++ )
		for ( k = l; k < r; k++ )
			getdp( i, k );
	return 0;
}

bool solve( )
{
	int i, k, j;
	char c;
	scanf( "%d%d\n", &m, &n );
	for ( i = 0; i <= m || i <= n; i++ )
		res[i] = 0;
	for ( i = 0; i < m; i++ )
	{
		gets( st );
		for ( k = 0; k < n; )
		{
			c = st[k / 4];
			if ( c >= 'A' )
				c = c - 'A' + 10;
			else
				c -= '0';
			for ( j = 8; j > 0; j >>= 1 )
			{
				dp[i][k] = -1;
				s[i][k++] = ( c / j ) + '0';
				c %= j;
			}
		}
		s[i][k] = '2';
		s[i][k + 1] = 0;
	}
	for ( k = 0; k <= n; k++ )
		s[m][k] = '2';
	s[m][k] = 0;
	for ( i = 0; i < m; i++ )
		for ( k = 0; k < n; k++ )
			getdp( i, k );
	while ( a.size( ) > 0 )
		iter( );
	int result = 0;
	for ( i = max( m, n ); i > 0; i-- )
		if ( res[i] > 0 )
			result++;
	printf( "%d\n", result );
	for ( i = max( m, n ); i > 0; i-- )
		if ( res[i] > 0 )
			printf( "%d %d\n", i, res[i] );
	return true;
}

int main( )
{
	prepare( );
	int i, t;
	scanf( "%d", &t );
	for ( i = 0; i < t; i++ )
	{
		printf( "Case #%d: ", i + 1 );
		( solve( ) );
	}
	return 0;
}
