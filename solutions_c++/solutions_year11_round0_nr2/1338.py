#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;


int comb[ 30 ][ 30 ], opp[ 30 ][ 30 ];
int pilha[ 200 ], sp;
char str[ 200 ];

int main(){
	int casos, n, c, d;
	
	scanf( "%d", &casos );
	
	for( int k = 1; k <= casos; ++k ){
		for( int i = 0; i < 30; ++i ){
			for( int j = 0; j < 30; ++j ){
				comb[ i ][ j ] = comb[ j ][ i ] = -1;
				opp[ i ][ j ] = opp[ j ][ i ] = -1;
			}
				
		}
		
		printf( "Case #%d: ", k ); 
		
		scanf( "%d", &c );
		for( int i = 0; i < c; ++i ){
			scanf( "%s", str );
			comb[ str[0] - 'A' ][ str[1] - 'A' ] = str[ 2 ] - 'A';
			comb[ str[1] - 'A' ][ str[0] - 'A' ] = str[ 2 ] - 'A';
		}
		
		scanf( "%d", &d );
		for( int i = 0; i < d; ++i ){
			scanf( "%s", str );
			opp[ str[0] - 'A' ][ str[1] - 'A' ] = str[ 2 ] - 'A';
			opp[ str[1] - 'A' ][ str[0] - 'A' ] = str[ 2 ] - 'A';
		}
		
		scanf( "%d %s", &n, str );
		sp = 0;
		for( int i = 0; i < n; ++i ){
			if( sp && comb[ str[i] - 'A' ][ pilha[sp - 1] ] != -1 )
				pilha[ sp - 1 ] = comb[ str[i] - 'A' ][ pilha[sp - 1] ];
			else
				pilha[ sp++ ] = str[i] - 'A';
				
			for( int j = 0; j < sp - 1; ++j ){
				if( opp[ pilha[j] ][ pilha[sp - 1] ] != -1 ){
					sp = 0;
				}
			}
		}
		
		printf( "[" );
		for( int i = 0; i < sp; ++i ){
			printf( "%c", pilha[ i ] + 'A' );
			if( i != sp - 1 )
				printf( ", " ); 
		}	
		printf( "]\n" );
	}
}

