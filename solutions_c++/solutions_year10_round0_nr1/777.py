#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<stack>
#include<queue>

using namespace std ;

int main ( int argc , char** argv ) {
	long long int N, K ;
	long long int tests, counter = 0, temp ;
	scanf("%lld",&tests ) ;
	counter = 0 ;
	long long int value[32] = { 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647 } ;
	while ( tests -- ) {
		counter ++ ;
		scanf("%lld%lld",&N,&K) ;
		temp = (K&value[N]) ;
		if ( temp == value[N] ) { printf("Case #%lld: ON\n",counter ) ; }
		else { printf("Case #%lld: OFF\n",counter) ; } 

	}
	return 0 ;
}
