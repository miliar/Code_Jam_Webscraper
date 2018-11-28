#include <stdio.h>
#include <string.h>

const int MAXN = 51 ;

char map[MAXN][MAXN] ;
char rmap[MAXN][MAXN] ;

// 0 : horizontal
// 1 : vertical 
// 2 : diagonal
int count[MAXN][MAXN][3] ;

void rotate(int N){
	int i , j , k ;
	for ( i = 0 ; i < N ; i ++ ){
		for ( j = 0 ; j < N ; j ++ ){
			rmap[i][j] = map[j][i] ;
		}
	}
	for ( j = 0 ; j < N ; j ++ ){
		for ( i = N - 1 ; i >= 0 ; i -- ){
			if ( rmap[i][j] != '.' ) {
				for ( k = i ; k < N - 1 ; k ++ ){
					if ( rmap[k + 1][j] == '.' ) {
						rmap[k + 1][j] = rmap[k][j] ;
						rmap[k][j] = '.' ;
					}
				}
			}
		}
	}
}

int row(int N , int K , char c){
	int i , j ;

	for ( i = 0 ; i < N ; i ++ ){
		count[i][0][0] = count[i][0][1] = count[i][0][2] = (rmap[i][0] == c) ;
		count[0][i][0] = count[0][i][1] = count[0][i][2] = (rmap[0][i] == c) ;
	}
	
	for ( i = 1 ; i < N ; i ++ ){
		for ( j = 1 ; j < N ; j ++ ){
			if ( rmap[i][j] != c ) {
				count[i][j][0] = count[i][j][1] = count[i][j][2] = 0 ;
			} else {
				count[i][j][0] = count[i][j - 1][0] + 1 ;
				count[i][j][1] = count[i - 1][j][1] + 1 ;
				count[i][j][2] = count[i - 1][j - 1][2] + 1 ;
			}
			if ( count[i][j][0] == K
				|| count[i][j][1] == K 
				|| count[i][j][2] == K ) {
				return 1 ;
			}
		}
	}

	for ( j = 0 ; j < N ; j ++ ){
		count[0][j][2] = (rmap[0][j] == c );
	}
	for ( i = 0 ; i < N ; i ++ ){
		count[i][N - 1][2] = (rmap[i][N - 1] == c) ;
	}

	for ( i = 1 ; i < N ; i ++ ){
		for ( j = N - 1 ; j >= 0 ; j -- ){
			if ( rmap[i][j] != c ) {
				count[i][j][2] = 0 ;
			} else {
				count[i][j][2] = count[i - 1][j + 1][2] + 1 ;
			}
			if ( count[i][j][2] == K ) {
				return 1 ;
			}
		}
	}

	return 0 ;
}

int main(){
	
	freopen("A-large.in" , "r" , stdin) ;
	freopen("out.txt" , "w" , stdout) ;
	
	int T , N , K ;
	int i , cs = 0 ;

	scanf("%d" , &T) ;
	while ( T -- ){
		cs ++ ;
		scanf("%d%d" , &N , &K) ; gets(map[0]) ;
		for ( i = 0 ; i < N ; i ++ ){
			gets(map[i]) ;
		}
		rotate(N) ;
		int re = (row(N , K , 'R') << 1) + row(N , K , 'B') ;
		switch (re){
		case 0: printf("Case #%d: Neither\n" , cs) ;break ;
		case 1: printf("Case #%d: Blue\n" , cs) ;break ;
		case 2: printf("Case #%d: Red\n" , cs) ;break ;
		case 3: printf("Case #%d: Both\n" , cs) ;break ;
		}
	}

	return 0 ;

}