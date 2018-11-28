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

int n, m, l;
int w[5005][20];
char buf[1000];
int pat[20];

int main( )
{
	int i, j, k;

	freopen( "moo.in", "r", stdin );
	freopen( "moo.out", "w", stdout );

	scanf( "%d %d %d", &l, &n, &m );
	fi( n )
	{
		scanf( "%s", buf );
		fj( l ) w[i][j] = ( 1 << ( buf[j] - 'a' ) );
	}
	fi( m )
	{
		scanf( "%s", buf );
		int pos = 0;
		fj( l )
		{
			pat[j] = 0;
			if( buf[pos] == '(' )
				for( ++ pos; buf[pos] != ')'; ++ pos )
					pat[j] |= ( 1 << ( buf[pos] - 'a' ) );
			else pat[j] |= ( 1 << ( buf[pos] - 'a' ) );
			++ pos;
		}
		int ans = 0;
		fj( n )
		{
			bool ok = true;
			fk( l ) if( !( pat[k] & w[j][k] ) ) { ok = false; break; }
			if( ok ) ++ ans;
		}
		printf( "Case #%d: %d\n", i + 1, ans );
	}

	return 0;
}
