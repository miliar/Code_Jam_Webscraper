#include <stdio.h>
#include <string.h>

int ans[19] ;
char target[] = "welcome to code jam" ;
char str[512] ;

int main(void){
	int n ;

	gets(str) ;
	sscanf(str, "%d", &n) ;

	for( int i_cases = 1 ; i_cases <= n ; i_cases++ ){
		gets(str) ;
		memset(ans, 0, sizeof(ans)) ;

		for( char *s=str ; *s ; s++ ){
			for( int i=18 ; i>0 ; i-- ){
				if( *s == target[i] )
					ans[i] = (ans[i]+ans[i-1]) % 10000 ;
			}

			if( *s == target[0] )
				ans[0] = (ans[0]+1) % 10000 ;
		}

		printf("Case #%d: %04d\n", i_cases, ans[18]) ;
	}

	return 0 ;
}

