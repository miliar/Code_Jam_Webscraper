#include<cstdio>
#include<cstring>
#define ELEN 8
using namespace std;
bool comb[ 128 ][ 128 ];
bool oppo[ 128 ][ 128 ];
int appear[ 128 ];
char form[ 128 ][ 128 ];
char list[ 101 ];
char stack[ 101 ];
char ele[ 8 ] = { 'Q','W','E','R','A','S','D','F' };
int top;
int main(){
	int T, _case = 0;
	scanf( "%d", &T );
	while( T -- ){
		int C, D, N;
		char rel[ 3 ];
		memset( comb, 0 , sizeof( comb ) );
		memset( oppo, 0 , sizeof( oppo ) );
		memset( appear, 0 , sizeof( appear ) );

		scanf( "%d", &C );
		for( int i = 0; i < C; i ++ ){
			scanf( "%s", rel );
			comb[ rel[ 0 ] ][ rel[ 1 ] ] = 1;
			comb[ rel[ 1 ] ][ rel[ 0 ] ] = 1;
			
			form[ rel[ 0 ] ][ rel[ 1 ] ] = rel[ 2 ];
			form[ rel[ 1 ] ][ rel[ 0 ] ] = rel[ 2 ];
		}
		scanf( "%d", &D );
		for( int i = 0; i < D; i ++ ){
			scanf( "%s", rel );
			oppo[ rel[ 0 ] ][ rel[ 1 ] ] = 1;
			oppo[ rel[ 1 ] ][ rel[ 0 ] ] = 1;
		}
		scanf( "%d %s", &N, list );
		top = 0;
		for( int i = 0; i < N; i ++ ){
			char c = list[ i ];
			if( top == 0 ){
				stack[ top ++ ] = c;
				++ appear[ c ];
			}else{
				char d = stack[ top-1 ];
				if( comb[ d ][ c ] == 1 ){
					stack[ top-1 ] = form[ d ][ c ];
					-- appear[ d ];
					++ appear[ form[ d ][ c ] ];
				}else{
					bool flag = 0;
					for( int j = 0; j < ELEN; j ++ ){
						if( appear[ ele[ j ] ] > 0 && oppo[ c ][ ele[ j ] ] == 1 ){
							flag = 1;
							break;
						}
					}
					if( flag == 0 ){
						stack[ top ++ ] = c;
						++ appear[ c ];
					}else{
						top = 0;
						memset( appear, 0 , sizeof( appear ) );
					}
				}
			}
		}
		printf( "Case #%d: [", ++ _case );
		for( int i = 0; i < top; i ++ ){
			if( i == 0 ){
				printf( "%c", stack[ i ] );
			}else{
				printf( ", %c", stack[ i ] );
			} 
		}
		printf("]\n");
	}
	return 0;
}
