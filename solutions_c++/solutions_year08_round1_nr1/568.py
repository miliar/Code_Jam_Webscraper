#include <stdio.h>
#include <stdlib.h>

int n ;
double data1[1024], data2[1024] ;
int nm1, nm2 ;
double ans ;

int cmp1(const void*a, const void*b){
	if( *((double*)a) < *((double*)b) )
		return -1 ;
	return 1 ;
}

int cmp2(const void*a, const void*b){
	if( *((double*)a) > *((double*)b) )
		return -1 ;
	return 1 ;
}

int main(void){

	int t, cases ;
	int i ;
	double ans ;
	
	scanf("%d", &t) ;
	for( cases=1 ; cases<=t ; cases++){
		scanf("%d", &n) ;
		for( i=0 ; i<n ; i++)
			scanf("%lf", &data1[i]);
		for( i=0 ; i<n ; i++)
			scanf("%lf", &data2[i]);
			
		qsort(data1, n, sizeof(double), cmp1) ;
		qsort(data2, n, sizeof(double), cmp2) ;
			
		ans = 0 ;
		for( i=0 ; i<n ; i++){
			ans += data1[i] * data2[i];
		}
		
		printf("Case #%d: %.0f\n", cases, ans) ;		
	}

	return 0 ;
}
