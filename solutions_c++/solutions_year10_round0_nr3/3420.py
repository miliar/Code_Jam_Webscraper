#include <stdio.h>
#include <string.h>

const int MAXN = 1010 ;

int f[MAXN] ; // original queue
int g[MAXN] ; // next starting point
int h[MAXN] ; // profit this round
bool cal[MAXN] ; // if this point is caculated

int main(){
	int T ;
	int R , k , N ;
	int i , j ;
	int loop_start , loop ;
	__int64 loop_profit;
	int cs = 0 ;
	__int64 ans ;

	//remember ? 
	freopen("C-large.in" , "r" , stdin) ;
	freopen("out.txt" , "w" , stdout) ;

	scanf("%d" , &T) ;
	while ( T -- ){
		scanf("%d%d%d" , &R , &k , &N) ;
		for ( i = 0 ; i < N ; i ++ ){
			scanf("%d" , &f[i]) ;
		}
		memset(cal , false , sizeof(cal)) ;
		
		// caculate profits from each point
		i = 0 ;
		while ( !cal[i] ){
			int tmp1 = 0 , tmp2 = 0 ; 
			for ( j = 0 ; j < N ; j ++ ){
				tmp1 += f[(i + j) % N] ;
				if ( tmp1 > k ){
					break ;
				}else{
					tmp2 = tmp1 ;
				}
			}
			g[i] = (i + j) % N ;
			h[i] = tmp2 ;
			cal[i] = true ;
			i = g[i] ;
		}

		ans = 0 ;

		// profit at head
		loop_start = i ;
		for ( i = 0 ; i != loop_start && R > 0 ; ){
			ans += h[i] ;
			R -- ;
			i = g[i] ;
		}

		// profit in a loop
		loop = 1 ;
		loop_profit = h[i] ;
		for ( ; g[i] != loop_start ; ){
			loop ++ ;
			loop_profit += h[g[i]] ;
			i = g[i] ;
		}
		ans += R / loop * loop_profit ;
		
		// profit at tail
		R %= loop ;
		i = loop_start ;
		for ( j = 0 ; j < R ; j ++ ){
			ans += h[i] ;
			i = g[i] ;
		}
		printf("Case #%d: %I64d\n" , ++cs , ans) ;
	}
	
	return 0 ;
}