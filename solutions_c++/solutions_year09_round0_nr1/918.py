#include <stdio.h>
#include <string.h>

char dic[5000][16] ;
char able[15][26] ;
int L, D, N ;

int main(void){
	char str[1024] ;

	scanf( "%d%d%d", &L, &D, &N ) ;
	for( int i=0 ; i<D ; i++ )
		scanf("%s", dic[i] ) ;

	for( int i_cases=1 ; i_cases <= N ; i_cases++ ){
		memset( able, 0, L*26 ) ;
		scanf("%s", str) ;

		char *s = str ;
		for( int i=0 ; *s ; i++ ){
			if( *s != '(' ){
				able[i][*s-'a'] = 1 ;
				s ++ ;
			}
			else{
				s ++ ;
				for( ; *s != ')' ; s++ )
					able[i][*s-'a'] = 1 ;
				s ++ ;
			}
		}

		int ans = 0 ;
		for( int i=0 ; i<D ; i++ ){
			int j ;
			for( j=0 ; j<L ; j++ ){
				if( !able[j][dic[i][j]-'a'] )
					break ;
			}
			if( j == L )
				ans ++ ;
		}

		printf("Case #%d: %d\n", i_cases, ans) ;
	}

	return 0 ;
}

