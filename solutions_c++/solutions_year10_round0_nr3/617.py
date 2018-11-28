#include <stdio.h>

int r, k, n ;
int g[1024] ;

int main(void){
	int t ;

	scanf("%d", &t) ;
	for( int i_cases=1 ; i_cases<=t ; i_cases++ ){
		scanf("%d%d%d", &r, &k, &n ) ;
		for( int i=0 ; i<n ; i++ )
			scanf("%d", &g[i]) ;

		long long ans = 0 ;
		int head = 0 ;
		int rr = 0 ;

		for( ; rr<r ; rr++ ){
			int kk = 0 ;
			for( int i=0 ; i<n; i++){
				if( kk + g[head] > k )
					break ;
				else{
					kk += g[head] ;
					ans += g[head] ;
					head = (head+1)%n ;
				}
			}

			if( head == 0 ){
				rr++ ;
				break ;
			}
		}

		if( rr < r ){
			int times = r/rr ;
			ans *= times ;
			rr *= times ;
		}

		for( ; rr<r ; rr++ ){
			int kk = 0 ;
			for( int i=0 ; i<n; i++){
				if( kk + g[head] > k )
					break ;
				else{
					kk += g[head] ;
					ans += g[head] ;
					head = (head+1)%n ;
				}
			}

			if( head == 0 ){
				rr++ ;
				break ;
			}
		}

		printf("Case #%d: %lld\n", i_cases, ans) ;
	}

	return 0 ;
}

