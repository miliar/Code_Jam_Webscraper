#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
#define N 600
#define MOD 100003
typedef long long LL;
int n;
LL dp[N][N], co[N][N];

void init( )
{
	int i, j;
	memset( co, 0, sizeof(co) );
	co[0][0] = 1;
	co[1][0] = co[1][1] = 1;
	for ( i = 2; i < N; i++ )
	{
		co[i][0] = 1;
		for ( j = 1; j <= i; j++ ) 
			co[i][j] = (co[i-1][j]+co[i-1][j-1])%MOD;
	}
}

void DP( )
{
	int i, j, k;
	LL u, v, w;
	memset( dp, 0, sizeof(dp) );
	dp[2][1] = 1;
	for ( i = 3; i < N; i++ )
	{
		dp[i][1] = 1;
		for ( j = 2; j < i; j++ )
		{
			w = 0;
			v = i-j-1;
			if ( v <= 0 ) v = 0;
			for ( k = 1; k < j; k++ )
			{
				u = j-k-1;
				w = (w+dp[j][k]*co[v][u])%MOD;
			}
			dp[i][j] = w;
		}
	}
}

int main( )
{
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.out", "w", stdout );
	int ca, t, i;
	LL ans;
	init( );
	DP( );
	scanf( "%d", &ca );
	for ( t = 1; t <= ca; t++ )
	{
		scanf( "%d", &n );
		ans = 0;
		for ( i = 1; i < n; i++ )
			ans = (ans+dp[n][i])%MOD;
		printf( "Case #%d: %lld\n", t, ans );
	}
}

