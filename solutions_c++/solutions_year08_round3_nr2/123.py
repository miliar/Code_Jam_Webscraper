#include <stdio.h>


bool is_ugly(long long n){
	if( n<0 )
		n = -n ;

	if( n % 2 == 0 )
		return true ;
	if( n % 3 == 0 )
		return true ;
	if( n % 5 == 0 )
		return true ;
	if( n % 7 == 0 )
		return true ;
	return false ;
}


long long ans ;
char str[64] ;

void run(int ind, long long sum){
	long long num = 0 ;
	bool minus = true;
	
	if( str[ind] == 0 ){
		if( is_ugly(sum) )
			ans ++ ;
		return ;
	}
	
	if( ind == 0 )
		minus = false ;
		
	for( ; str[ind] ; ind++ ){
		num *= 10 ;
		num += str[ind]-'0' ;
		run(ind+1, sum + num) ;
		if(minus)
			run(ind+1, sum - num) ;
	}
}


int main(void){

	int cases, t ;
	
	scanf("%d", &t) ;
	for( cases=1 ; cases<=t; cases++){
		scanf("%s", str) ;
		
		ans = 0 ;
		run(0,0) ;
		
		printf("Case #%d: %lld\n", cases, ans) ;
	}

	return 0 ;
}
