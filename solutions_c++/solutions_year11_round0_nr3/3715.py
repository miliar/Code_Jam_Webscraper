
#include <stdio.h>
#define MAX_N 15

int main( void ){

	int T, cases=1 ;
	int N ;
	unsigned int candys[MAX_N], sean, patrick ;
	int answer ;

	scanf("%d", &T ) ;
	while( T-- ){
		scanf("%d", &N ) ;
		for(int i=0 ; i<N ; ++i ){
			scanf("%u", &candys[i] ) ;
		}
		answer = 0 ;
		for(int i=1 ; i<(1<<N)-1 ; ++i ){
			patrick = sean = 0 ;
			int aux = 0 ;
			for(int k=1, j=0 ; k<(1<<N) ; k<<=1, ++j ){
				if( i & k ){
					patrick ^= candys[j] ;
					aux += candys[j] ;
				}else{
					sean ^= candys[j] ;
				}
			}
//			printf("i = %d patrick = %u sean = %u aux = %d\n", i, patrick, sean, aux) ;
			if( patrick == sean ){
				if( aux > answer ){
					answer = aux ;
				}
			}
		}
		if( answer )
			printf("Case #%d: %d\n", cases++, answer );
		else
			printf("Case #%d: NO\n", cases++ );

	}

	return 0 ;
}
