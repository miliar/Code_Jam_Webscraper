#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std ;

int main()
{
	int n , T , caseT , i , len , last ;
	int digit[30] ;

	
	freopen( "B-small-attempt2.in" , "r" , stdin ) ;
	freopen( "B-small.out" , "w" , stdout ) ;

	scanf( "%d" , &T ) ; 
	for ( caseT=1 ; caseT<=T ; ++caseT ) 
	{
		scanf( "%d" , &n ) ;
		len=0 ;
		while ( n )
		{
			digit[len++] = n%10 ;
			n/=10 ;
		}
		reverse( digit , digit+len ) ;

		int ret = next_permutation( digit , digit+len ) ;
		if ( ret == 0 ) 
		{
			prev_permutation( digit , digit+len ) ;
			for ( i=len ; i>0 ; --i ) digit[i]=digit[i-1] ;
			digit[0] = 0 ;
			++len ;
			next_permutation( digit , digit+len ) ;
		}
//		for ( i=0 ; i<len ; ++i ) printf( "%d " , digit[i] ) ;
//		putchar( '\n' ) ;
		n = 0 ;
		for ( i=0 ; i<len ; ++i )
			n = n*10+digit[i] ;

		printf( "Case #%d: %d\n" , caseT , n ) ;
	}
	return 0 ;
}