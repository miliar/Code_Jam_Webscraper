// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen( "in.txt", "r", stdin); 
	freopen( "out.txt", "w", stdout); 
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i )
#define fi( a ) for ( int i = 0; i < ( a ); ++i )
#define fj( a ) for ( int j = 0; j < ( a ); ++j )
#define fk( a ) for ( int k = 0; k < ( a ); ++k )
#define CLR( a, b ) memset( ( a ), ( b ), sizeof ( a ) )
#define clr( a ) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(), ( v ).end()

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = ( 1 << 30 );

int a[55][55];
int n, K;
int b[55][55];
char buf[100];

bool look( int state, int x, int y, int dx, int dy, int K )
{
	if ( K == 0 ) return ( true );
	if ( x < 0 || y < 0 || x >= n || y >= n ) return ( false );
	if ( a[x][y] != state ) return ( false );
	return ( look( state, x + dx, y + dy, dx, dy, K-1 ) );
}

void solve()
{
	scanf("%d%d\n", &n, &K );
	fi( n )
	{
		gets( buf );
		fj( n )
		{
			if ( buf[j] == '.' )
				a[i][j] = 0;
			else
				a[i][j] = buf[j] == 'R' ? 1 : 2;
		}
	}	
	for ( int i1 = 0, j2 = n-1; i1 < n; ++i1, --j2 )
	{
		for ( int j1 = 0, i2 = 0; j1 < n; ++j1, ++i2 )
		{
			b[i2][j2] = a[i1][j1];
		}
	}
	fi( n ) fj( n ) a[i][j] = 0;
	fj( n )
	{
	    int cnt = n-1;
		for ( int i = n-1; i >= 0; --i )
		{
			if ( b[i][j] != 0 )
			{
				a[cnt--][j] = b[i][j];
			}
		}
	}
	bool first = false, second = false;
	fi( n )
		fj( n )
		{
			if ( a[i][j] > 0 )
			{
				if ( look( a[i][j], i, j, -1, -1, K ) || 
					 look( a[i][j], i, j, 0, -1, K ) ||
					 look( a[i][j], i, j, -1, 0, K ) ||
					 look( a[i][j], i, j, -1, 1, K ) ||
					 look( a[i][j], i, j, 0, 1, K ) )
				{
					if ( a[i][j] == 1 )
						first = true;
					else
					 	second = true;
				}
			}
		}
	if ( first && second )
		printf("Both\n");
	else
		if ( first )
			printf("Red\n");
		else
			if ( second )
				printf("Blue\n");
			else
				printf("Neither\n");
}

int main()
{
	initf();
	int t;
	scanf("%d", &t );
	fi( t )
	{
	    printf("Case #%d: ", i + 1 );
		solve();
	}
	return ( 0 );
}
