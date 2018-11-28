/*第一个是1
后面从0开始
跳过1

最终的radix就是进制数

然后转换成long long
*/

#include <stdio.h>
#include <string.h>

int main()
{
	int T , caseT ;
	int i , j , radix , len ;
	__int64 ans , temp ;
	char number[100] ;
	int digit[100] ;

	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;

	scanf( "%d" , &T ) ;
	for ( caseT=1 ; caseT<=T ; ++caseT ) 
	{
		scanf( "%s" , &number ) ;
		memset( digit , -1 , sizeof(digit) ) ;		
		len = strlen( number ) ;
		for ( i=0 ; i<len ; ++i )
			if ( number[i] == number[0] ) 
				digit[i] = 1 ;
		radix = 0 ;
		for ( i=1 ; i<len ; ++i )
			if ( digit[i] != -1 ) continue ;
			else
			{
				for ( j=i ; j<len ; ++j )
					if ( number[j] == number[i] ) 
						digit[j] = radix ;
				if ( radix==0 ) radix=2 ;
				else ++radix ;
			}
		if ( radix<2 ) radix = 2 ;
		ans = 0 ;
		temp = 1 ;
		for ( i=len-1 ; i>=0 ; --i )
		{
			ans = ans+temp*digit[i] ;
			temp*=radix ;
		}
		printf( "Case #%d: %I64d\n" , caseT , ans ) ;

	}

	return 0 ;
}
