#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
enum {MAX = 101 };
int TABLE[ MAX ][ MAX ];
int TABLENEW[ MAX ][ MAX ];


int ev()
{
	int cc = 0;
	int N = 101;
	for( int i=0;i<N;i++ ) 
		for( int j=0;j<N;j++ ) {
			if( ( i-1 < 0 || TABLE[ i - 1 ][ j ] == 0 ) && ( j-1 < 0 || TABLE[ i ][ j - 1 ] == 0 ) ) 
				TABLENEW[ i ][ j ] = 0;
			else if( i-1 >= 0 && TABLE[ i - 1 ][ j ] == 1 && j-1 >= 0 && TABLE[ i ][ j - 1 ] == 1 ) 
				TABLENEW[ i ][ j ] = 1;
			else 
				TABLENEW[ i ][ j ] = TABLE[ i ][ j ];
			if( TABLENEW[ i ][ j ] == 1 )
				cc = 1;
		}
	memcpy( TABLE, TABLENEW, sizeof( TABLE ) );
	return cc;
}
int main()
{
	int ccN;
	scanf("%d", &ccN);
	for( int cc=0;cc<ccN;cc++ ) {
		int R;
		scanf("%d", &R );
		
		memset( TABLE, 0 ,sizeof( TABLE ) );

		for( int i=0;i<R;i++ ) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2 );
			for( int x=min(x1,x2);x<=max(x1,x2);x++)
				for( int y=min(y1,y2);y<=max(y1,y2);y++)
					TABLE[ x ][ y ] = 1;
		}
		int count = 0;
		while( ev() )
			count++;
		printf("Case #%d: %d\n", cc+1, count+1 );
	}
	return 0;
}
