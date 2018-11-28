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

bool f[104][104];
bool f1[104][104];
int n, m;

void genn()
{
	clr( f1 );
	fi( n )
		fj( m )
		{
			if ( f[i][j] )
			{
				if ( ( !f[i-1][j] && !f[i][j-1] ) )
					f1[i][j] = false;
				else
					f1[i][j] = true;

			}
			else
			{
				if ( ( f[i-1][j] && f[i][j-1] ) )
					f1[i][j] = true;
				else
					f1[i][j] = false;
			}
		}
	memcpy( f, f1, sizeof f );
}

bool emp()
{
	fi( n ) fj( m ) if ( f[i][j] ) return ( false );
	return ( true );
}

void solve()
{
	int r;
	int x1, y1, x2, y2;
	scanf("%d", &r );
	clr( f );
	fi( r )
	{
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2 );
		if ( x1 > x2 ) swap( x1, x2 );
		if ( y1 > y2 ) swap( y1, y2 );
		fr(x,x1,x2)
			fr(y,y1,y2)
				f[x][y] = true;
	}
	n = 0;
	m = 0;
	fi( 104 )
		fj( 104 )
		{
			if ( f[i][j] )
			{
				n = max( n, i );
				m = max( m, j );
			}
		}
	++n;
	++m;
	int ret = 0;

	for ( ; ; ++ret )
	{
	/*	fi( n )
		{
			fj( m )
			{
				if ( f[i][j] )
					cout << "1 ";
				else
					cout << "0 ";
			}
			cout << "\n";
		}
		cout << "----------\n";*/
		if ( emp() )
		{
			printf("%d\n", ret );
			return;
		}
		else
		{
			genn();
		}
	}
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
}