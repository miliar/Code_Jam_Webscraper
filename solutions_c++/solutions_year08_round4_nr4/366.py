#include <stdio.h>
#include <string.h>

int n ;
char used[8] ;
char S[60000] ;

int per[8] ;
int ans ;

void test(){
	int i, j, sum=0 ;
	char last ;
	
	last = 0 ;
	for( i=0 ; S[i] ; i+=n){
		for( j=0 ; j<n ; j++){
			if( S[i+per[j]] != last ){
				sum ++ ;
				last = S[i+per[j]] ;
				
				if( sum == ans )
					return ;
			}
		}
	}
	
	if( ans > sum )
		ans = sum ;
}

void gen_per(int ind){
	int i ;
	
	if( ind == n ){
		test() ;
		return ;
	}
		
	for( i=0 ; i<n ; i++){
		if( !used[i] ){
			used[i] = 1 ;
			per[ind] = i ;
			
			gen_per(ind+1) ;
			
			used[i] = 0 ;			
		}
	}
}

int main(void){

	int c, cases ;
	
	scanf("%d", &c) ;
	for( cases=1 ; cases<=c ; cases++){
		scanf("%d", &n) ;
		scanf("%s", S) ;
		
		ans = 0x7FFFFFFF ;
		
		gen_per(0) ;
		
		printf("Case #%d: %d\n", cases, ans) ;		
	}

	return 0 ;
}
