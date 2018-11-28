#include "stdio.h"
#include "string.h"
#include "algorithm"

using namespace std ;

#define		MIN(a,b)	(a) < (b) ? (a) : (b)

void Solve()
{
	int i,v,sum,size,tmp,Min ;

	scanf( "%d" , & size ) ;
	scanf( "%d" , & sum ) , Min = tmp = sum ;
	for( i = 1 ; i < size ; ++i )
	{
		scanf( "%d" , & v ) , sum += v , Min = MIN( Min , v ) , tmp ^= v ;		
	}
	! tmp ? printf( "%d\n" , sum-Min ) :printf( "NO\n" ) ;
} 

int main()
{
	freopen( "C-large.in" , "r" , stdin ) ;
	freopen( "C-large.out" , "w" , stdout ) ;

	int i, cas ;
	
	for( scanf( "%d" , & cas ) , i = 1 ; i <= cas ; ++i )
	{
		printf( "Case #%d: ",i ) ;
		Solve() ;
	}
	return 0 ;
}