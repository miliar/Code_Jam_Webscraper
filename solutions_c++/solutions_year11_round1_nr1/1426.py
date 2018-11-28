#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std ;

int mcd( int A, int B ) {
	if( B==0 )
		return A ;
	return mcd( B, A%B ) ;
}

void caso( int T ) {
	int N, d, g ;
	
	cin >> N >> d >> g ;
	printf("Case #%d: ",T ) ;
	
	if(  g%100==0  )  {
		if( d==g )
			printf("Possible\n" ) ;
		else
			printf("Broken\n" ) ;
		return ;
	}
	
	g = 100/mcd( d, 100 ) ;
	
	if( g<=N )
		printf("Possible\n" ) ;
	else
		printf("Broken\n" ) ;
		
	return ;
}

int main() {
	int T, i ;
	
	cin >> T ;
	
	for( i=1; i<=T; i++ )	
		caso( i ) ;
	
	return 0 ;
}
