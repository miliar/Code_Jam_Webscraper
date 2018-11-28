#include <stdio.h>

int main(void){

	int t ;
	scanf("%d", &t) ;

	for( int i_cases=1 ; i_cases<=t ; i_cases++ ){
		int n, k ;

		scanf("%d%d", &n, &k) ;
		printf("Case #%d: ", i_cases) ;

		int sum = 0 ;
		for( int i=0 ; i<n ; i++ ){
			if( (k>>i)&1 )
				sum ++ ;
		}
		if( sum == n )
			puts("ON") ;
		else
			puts("OFF") ;
	}

	return 0 ;
}
