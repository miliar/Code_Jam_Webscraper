#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<stack>
#include<queue>

using namespace std ;

long long int g[1001] ;
int nextIndex[ 1001 ] ;
long long int cost [ 1001 ] ;

int main ( int argc , char** argv ) {
	int tests , counter = 0 ;;
	int i,j ;
	long long int  R , K, N , sum;
	scanf("%d",&tests ) ;
	while ( tests -- ) {
		counter ++ ;

		scanf("%lld%lld%lld",&R,&K,&N) ; 
		for ( i = 0 ; i < N ; i ++ ) {
			scanf("%lld",&g[i]) ;
		}

		for ( i = 0 ; i < N ; i ++ ) {
			sum = g[i] ;
			cost[i] = g[i] ;
			for ( j = i+1 ;  ; j ++ ) {
				if ( j == N ) { j = 0 ; } 
				if ( j == i ) { 
					nextIndex[i] = i ;
					break ;
				}
				if ( sum + g[j] <= K ) {
					sum += g[j] ;
					cost[i] += g[j] ;
				} else {
					nextIndex[i] = j ;
					break ;
				}
			}
		}

//		for ( i = 0 ; i < N ; i ++ ) {
//			printf("The cost is %lld and the nextIndex = %d\n",cost[i], nextIndex[i] ) ;
//		}

		long long int start = 0 , totalCost = 0  ;
		for ( i = 0 ; i < R ; i ++ ) {
			totalCost += cost[start] ;
			start = nextIndex[start] ;
		}
		printf("Case #%d: %lld\n",counter, totalCost ) ;
	}
	return 0 ;
}
