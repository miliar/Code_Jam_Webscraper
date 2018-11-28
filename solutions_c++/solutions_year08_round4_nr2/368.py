#include <stdio.h>
#include <math.h>

int N, M, A ;


void go(){
	int x1, y1, x2, y2, x3, y3 ;
	int sum ;
	
	y1 = x2 = 0 ;
	for( x1=0 ; x1<=N ; x1++ ){
		for( y2=0 ; y2<=M ; y2++){
			for( x3=0 ; x3<=N ; x3++){
				for( y3=0 ; y3<=M ; y3++){
					sum = 0 ;
					sum += x1*y2 - x2*y1 ;
					sum += x2*y3 - x3*y2 ;
					sum += x3*y1 - x1*y3 ;
					
					if( sum == A || sum == -A){
						printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3) ;
						return ;
					}
				}
			}
		}
	}
	
	x1 = y2 = 0 ;
	for( y1=0 ; y1<=M ; y1++){
		for( x2=0 ; x2<=N ; x2++ ){
			for( x3=0 ; x3<=N ; x3++){
				for( y3=0 ; y3<=M ; y3++){
					sum = 0 ;
					sum += x1*y2 - x2*y1 ;
					sum += x2*y3 - x3*y2 ;
					sum += x3*y1 - x1*y3 ;
					
					if( sum == A || sum == -A){
						printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3) ;
						return ;
					}
				}
			}
		}
	}	
}

int main(void){

	int cases, c ;
	int i, j, e ;
	
	scanf("%d", &c) ;
	for( cases=1 ; cases<=c ; cases++){
		scanf("%d%d%d", &N, &M, &A) ;
		
		printf("Case #%d: ", cases) ;
		if( N*M < A ){
			puts("IMPOSSIBLE") ;
			continue ;
		}
			
		e = sqrt(A) ;
		for( i=1 ; i<=e ; i++ ){
			if(A%i == 0){
				j = A/i ;
				
				if( i<=N && j<=M ){
					printf("0 0 %d 0 0 %d\n", i, j) ;
					break ;
				}
				else if( j<=N && i<=M ){
					printf("0 0 %d 0 0 %d\n", j, i) ;
					break ;
				}
			}
		}
		if( i<=e )
			continue ;

		go() ;
	}
	

	return 0 ;
}
