#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

using namespace std;

int n, m;
int a[105][105];
int clr[105*105];
char c2a[105*105];

int gc( int a ) { if( a == clr[a] ) return a; return clr[a] = gc( clr[a] ); }
void paint( int i, int j, int ii, int jj )
{
	clr[gc( i * m + j )] = gc( ii * m + jj );
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "moo.in", "r", stdin );
	freopen( "moo.out", "w", stdout );

	scanf( "%d", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		scanf( "%d %d", &n, &m );
		fi( n ) fj( m ) scanf( "%d", &a[i][j] );
		fi( n * m ) clr[i] = i;
		fi( n ) fj( m )
		{
			int a1 = ( i ? a[i-1][j] : a[i][j] );
			int a2 = ( j ? a[i][j-1] : a[i][j] );
			int a3 = ( ( j < m - 1 ) ? a[i][j+1] : a[i][j] );
			int a4 = ( ( i < n - 1 ) ? a[i+1][j] : a[i][j] );
			int mn = min( min( a1, a2 ), min( a3, a4 ) );
			if( mn < a[i][j] )
			{
				if( a1 == mn ) paint( i, j, i - 1, j );
				else if( a2 == mn ) paint( i, j, i, j - 1 );
				else if( a3 == mn ) paint( i, j, i, j + 1 );
				else  paint( i, j, i + 1, j );
			}
		}
		memset( c2a, 0, sizeof( c2a ) );
		char ltr = 'a';
		printf( "Case #%d:\n", t );
		fi( n ) fj( m )
		{
			int c = gc( i * m + j );
			if( c2a[c] == 0 ) c2a[c] = ltr ++;
			printf( "%c%c", c2a[c], " \n"[j == m-1] );
		}
		assert( ltr - 1 <= 'z' );
	} /**/

	return 0;
}
