#include <stdio.h>
#include <string.h>

int n, m ;
long long X, Y, Z ;
long long sign[1024] ;
long long A[1024] ;
int count[1024] ;
int ans ;


int main(void){

	int cases, t; 
	int i, j ;
	
	scanf("%d", &t) ;
	for( cases=1 ; cases <= t ; cases++){
		scanf("%d%d%lld%lld%lld", &n, &m, &X, &Y, &Z) ;
		
		for( i=0 ; i<m ; i++ )
			scanf("%lld", &A[i]) ;
		for( i=0 ; i<n ; i++){
			sign[i] = A[i%m] ;
			A[i%m] = (X * A[i%m] + Y * (i+1)) % Z ;
			//printf("sign[%d] : %lld\n", i, sign[i]) ;
		}
		
		memset(count, 0, sizeof(count) ) ;
		ans = 0 ;
		for( i=0 ; i<n ; i++){
			count[i] = 1 ;
			for( j=0 ; j<i ; j++){
				if( sign[j] < sign[i] ){
					count[i] += count[j] ;
					count[i] %= 1000000007 ;
				}
			}
			ans += count[i] ;
			ans %= 1000000007 ;
		}
		
		printf("Case #%d: %d\n", cases, ans) ;
	}

	return 0 ;
}
