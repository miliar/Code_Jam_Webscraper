#include <stdio.h>
#include <string.h>

struct c_big{
	int digit[130] ;

	c_big(){
		reset() ;
	}

	void build(char *number){
		reset() ;
		int len = strlen( number ) ;
		for( int i=0 ; i<len ; i++ )
			digit[i] = number[len-1-i] - '0' ;
	}

	void reset(void){
		memset( digit, 0, sizeof(digit)) ;
	}

	void mult( int *a, int *b ){
		reset() ;

		for( int i=0 ; i<64 ; i++ ){
			int carry = 0 ;
			for( int j=0 ; j<64 ; j++ ){
				if( i+j >= 64 )
					break ;

				carry += digit[i+j] + a[i]*b[j] ;
				digit[i+j] = carry % 10 ;
				carry /= 10 ;
			}
		}
	}

	int cmp( int *b ){
		for( int i=64-1 ; i>=0 ; i-- ){
			if( digit[i] > b[i] )
				return 1 ;
			else if( digit[i] < b[i] )
				return -1 ;
		}
		return 0 ;
	}

	void sub( int *b, int shift ){
		int *a = &digit[shift] ;
		int carry = 0 ;
		int i ;
		for( i=0 ; i<64 ; i++ ){
			carry += a[i] - b[i] ;
			if( carry >= 0 ){
				a[i] = carry ;
				carry = 0 ;
			}
			else{
				a[i] = 10 + carry ;
				carry = -1 ;
			}
		}
	}

	void rem( c_big &div ){
		if( div.zero() )
			return ;
		
		for( int shift=64-1 ; shift>=0 ; shift-- ){
			while( div.cmp(&digit[shift]) <= 0 )
				sub( div.digit, shift ) ;
		}
	}

	int zero(void){
		for( int i=0 ; i<64 ; i++ ){
			if( digit[i] )
				return 0 ;
		}
		return 1 ;
	}
	
	void output(void){
		if( zero() )
			putchar('0') ;
		else{
			int i ;
			for( i=64-1 ; digit[i]==0 ; i-- ) ;		
			for( ; i>=0 ; i-- )
				putchar( digit[i]+'0' ) ;
		}
	}
} ;



c_big gcd( c_big &a, c_big &b){
	c_big p = a ;
	c_big q = b ;
	
	while( 1 ){
		if( p.zero() )
			return q ;
		if( q.zero() )
			return p ;

		p.rem( q ) ;
		q.rem( p ) ;
	}

	p.reset() ;
	return p ;
}

char str[128] ;
int n ;
c_big past[1024] ;
c_big ans_gcd ;

int main(void){
	int t ;
	scanf("%d", &t) ;

	for( int i_cases=1 ; i_cases<=t ; i_cases++ ){
		scanf("%d", &n) ;
		for( int i=0 ; i<n ; i++ ){
			scanf("%s", str) ;
			past[i].build( str ) ;
		}

		int min_i = 0 ;
		for( int i=1 ; i<n ; i++ ){
			if( past[i].cmp( past[min_i].digit ) < 0 )
				min_i = i ;
		}
				
		for( int i=0 ; i<n ; i++ ){
			if( i != min_i )
				past[i].sub( past[min_i].digit, 0 ) ;
		}

		if( min_i == 0 )
			ans_gcd = past[1] ;
		else
			ans_gcd = past[0] ;

		for( int i=0 ; i<n ; i++ ){
			if( i != min_i )
				ans_gcd = gcd( ans_gcd, past[i] ) ;
		}

		past[min_i].rem( ans_gcd ) ;
		if( past[min_i].zero() )
			ans_gcd.reset() ;
		else
			ans_gcd.sub( past[min_i].digit, 0 ) ;

		printf("Case #%d: ", i_cases) ;
		if( ans_gcd.zero() )
			puts("0") ;
		else{
			ans_gcd.output() ;
			putchar('\n') ;
		}
	}

	return 0 ;
}


