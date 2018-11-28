#include <stdio.h>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <set>
#include <map>

using namespace std;

#define fo(a,b,c) for( ( a ) = ( b ); ( a ) < ( c ); ++ ( a ) )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

int n, m;

int main( )
{
	int i, j, k, t, tt;
	
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );
	
	for( tt = 1; tt <= t; ++ tt )
	{
		int a;
		scanf( "%d %d %d", &n, &m, &a );
		
		printf( "Case #%d: ", tt );
		fi( n + 1 ) fj( m + 1 )
		{
			int ii, jj;
			fr( ii, n + 1 ) fr( jj, m + 1 )
			{
				if( abs( ii * j - jj * i ) == a )
				{
					printf( "0 0 %d %d %d %d\n", i, j, ii, jj );
					goto e;
				}
			}
		}
		printf( "IMPOSSIBLE\n" );
		e:;
	}
	
	return 0;
}
