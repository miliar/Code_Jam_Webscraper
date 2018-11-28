#include <cstdio>
#include <iostream>
#include <memory.h>
#include <vector>
#include <ctime>
#include <string>
#include <algorithm>
#include <cstring>
#include <utility>
#include <map>
#include <set>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
typedef pair<int,int> pii;
typedef long long ll;

const ll md = 100003;

void add( ll& x, ll y )
{
	x = ( x+y ) % md;
}

ll f[510][510];
ll C[510][510];

int main()
{
		int n;
		C[0][0] = 1;
		for ( int i=1; i<=500; i++ )
		{
			C[i][0] = 1;
			for ( int j=1; j<=500; j++ )
			{
				C[i][j] = C[i-1][j-1];
				add( C[i][j], C[i-1][j] );
			}
		}
				
		int t;
		scanf( "%d", &t );
		f[1][1] = 1;
		for ( int i=2; i<=500; i++ )
		{
			f[i][1] = 1;
			for ( int j=2; j<i; j++ )
			{
				f[i][j] = 0;
				for ( int k=1; k<j; k++ )
					add( f[i][j], f[j][k]*C[i-j-1][j-k-1] );
			}
		}
/*		
	for ( int i=2; i<=5; i++ )
		for ( int j=1; j<i; j++ )
			printf( "f[%d][%d] = %d\n", i, j, (int)f[i][j] );
*/		
	for ( int q=1; q<=t; q++ )
	{
		scanf( "%d", &n );
		ll ans = 0;
		for ( int j=1; j<=n; j++ )
			add( ans, f[n][j] );
		printf( "Case #%d: %d\n", q, (int)ans );
	}
	return 0;
}

