#include <stdio.h>
#include <stdlib.h>

int P, K ;
int L ;
int data[1024] ;


int cmp(const void*a ,const void*b){
	return *(int*)b - *(int*)a ;
}


int main(void){

	int cases, N ;
	int i;
	double ans ;
	
	scanf("%d", &N) ;
	for( cases=1 ; cases<=N ;cases++){
		scanf("%d%d%d", &P, &K, &L) ;
		for( i=0 ; i<L ; i++ ){
			scanf("%d", &data[i]) ;
			//printf("%d\n", data[i]) ;
		}
			
		if( P*K < L ){
			printf("Case #%d: Impossible\n", cases) ;
			continue ;
		}
		
		qsort( data, L, sizeof(int), cmp );
		
		ans = 0 ;
		for( i=0 ; i<L ; i++ )
			ans += data[i] * (double)((i/K)+1) ;
			
		printf("Case #%d: %.0f\n", cases, ans) ;		
	}
	
	return 0 ;
}

