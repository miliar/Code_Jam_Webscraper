#include <iostream>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
using namespace std;

char combine[ 26 ][ 26 ];
vector< int > oppose[ 26 ];
bool exist[ 1010 ];
char str[ 1010 ];
int pos[ 26 ];

int main( int argc, char* argv[] )
{

	freopen( "B.out", "w", stdout );
	int t;
	scanf( "%d", &t );


	for ( int k = 0; k < t; ++k )
	{
		printf( "Case #%d: ", k + 1 );
		memset( combine, -1, sizeof( combine ) );

		for ( int i = 0; i < 26; ++i )
			oppose[ i ].clear();

		int C, O, L;
		scanf( "%d", &C );

		for ( int i = 0; i < C; ++i )
		{
			char a, b, c;
			scanf( " %c %c %c", &a, &b, &c );
			a -= 'A', b -= 'A', c -= 'A';
			combine[ a ][ b ] = combine[ b ][ a ] = c;
		}
		


		scanf( "%d", &O );

		for ( int i = 0; i < O; ++i )
		{
			char a, b;
			scanf( " %c %c", &a, &b );
			a -= 'A', b -= 'A';
			oppose[ a ].push_back( b );
			oppose[ b ].push_back( a );
		}
		
		scanf( "%d", &L );

		scanf( "%s", str );
		memset( exist, -1, sizeof( exist ) );
		memset( pos, -1, sizeof( pos ) );

		int last = -1;
		
		for ( int i = 0; i < L; ++i )
		{
			if ( !exist[ i ] )
				continue;

			int now = str[ i ] - 'A', next = i + 1 == L ? -1 : str[ i + 1 ] - 'A';
			
			int pre = 1e9;
			for ( int j = 0; j < oppose[ now ].size(); ++j )
			{
				int x = oppose[ now ][ j ];
				if ( pos[ x ] != -1 )
					pre = min( pre, pos[ x ] );
			}
			
			if ( pre == 1e9 )
			{
				if ( next != -1 && combine[ now ][ next ] != -1 )
				{
					str[ i ] = combine[ now ][ next ] + 'A';
					exist[ i + 1 ] = 0;
					
					continue;
				}
				else
					pos[ now ] = i;
			}
			else
			{
				for ( int j = 0; j <= i; ++j )
				{
					exist[ j ] = 0;
					int x = str[ j ] - 'A';
					if ( pos[ x ] == j )
						pos[ x ] = -1;
				}
			}
		}

		putchar( '[' );
		bool first = 1;
		for ( int i = 0; i < L; ++i )
			if ( exist[ i ] )
			{
				if ( !first )
					putchar( ',' ), putchar( ' ' );
				else
					first = 0;
				putchar( str[ i ] );
			}
		puts( "]" );
	}
	return 0;
}






