#include <stdio.h>
#include <algorithm>
using namespace std ;

#define MAX 1010

int buf[MAX] ;

int gcd(int a, int b){                               
    return a==0 ? b:gcd(b%a,a);
}

int main()
{
	int n , i , j , caseT , case_num ;

	freopen( "B-small-attempt0.in" , "r" , stdin ) ;
	freopen( "B-small.out" , "w" , stdout ) ;
	

	scanf( "%d" , &case_num ) ;
	for ( caseT=1 ; caseT<=case_num ; ++caseT ) 
	{
		scanf ( "%d" , &n ) ;
		for ( i=0 ; i<n ; ++i ) scanf( "%d" , &buf[i] ) ;
		sort( buf , buf+n ) ;
		int ans = buf[1]-buf[0] ;
		for ( i=0 ; i<n ; ++i )
			for ( j=i+1 ; j<n ; ++j ) 
				ans = gcd( ans , buf[j]-buf[i] ) ;
		printf( "Case #%d: %d\n" , caseT , (ans-buf[0]%ans)%ans ) ;
	}
	return 0 ;
}