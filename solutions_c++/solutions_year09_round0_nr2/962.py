#include <stdio.h>
#include <string.h>

int R, C ;
int raw[128][128] ;
char dir[128][128] ;
char ans[128][128] ;

int go[4][2] = {{-1,0},{0,-1},{0,1},{1,0}} ;

int ch ;
void dfs(int r, int c){
	ans[r][c] = ch ;

	for( int i=0 ; i<4 ; i++ ){
		int nr = r+go[i][0] ;
		if( nr<1 || R<nr )
			continue ;

		int nc = c+go[i][1] ;
		if( nc<1 || C<nc )
			continue ;

		if( ans[nr][nc] )
			continue ;

		if( dir[nr][nc] + i == 3 || i == dir[r][c] )
			dfs(nr, nc) ;
	}
}


int main(void){
	int N ;
	int r, c ;

	scanf("%d", &N) ;
	for( int i_cases=1 ; i_cases<=N ; i_cases++ ){
		scanf("%d%d", &R, &C) ;

		for( r=1 ; r<=R ; r++ ){
			for( c=1 ; c<=C ; c++ )
				scanf("%d", &raw[r][c]) ;
		}

		for( r=1 ; r<=R ; r++ )
			raw[r][0] = raw[r][C+1] = 0x7FFFFFFF ;
		for( c=1 ; c<=C ; c++ )
			raw[0][c] = raw[R+1][c] = 0x7FFFFFFF ;

		for( r=1 ; r<=R ; r++ ){
			for( c=1 ; c<=C ; c++ ){
				dir[r][c] = -1 ;
				int min = raw[r][c] ;
				for( int i=0 ; i<4 ; i++ ){
					int nr = r+go[i][0] ;
					int nc = c+go[i][1] ;

					if( min > raw[nr][nc] ){
						min = raw[nr][nc] ;
						dir[r][c] = i ;
					}
				}

				ans[r][c] = 0 ;
			}
		}

		printf("Case #%d:\n", i_cases) ;
		ch = 'a' ;
		for( r=1 ; r<=R ; r++ ){
			for( c=1 ; c<=C ; c++ ){
				if( !ans[r][c] ){
					dfs(r, c) ;
					ch ++ ;
				}

				if( c > 1 )
					putchar(' ') ;
				putchar( ans[r][c] ) ;
			}

			putchar('\n') ;
		}
	}

	return 0 ;
}


