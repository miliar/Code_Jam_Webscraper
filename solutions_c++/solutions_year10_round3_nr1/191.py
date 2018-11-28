
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<stack>
#include<queue>

using namespace std ;

int N ;
int answer ;
int a[10000] ; 
int b[10000] ;
int intersect ( int i , int j ) {
	int a1 = a[i] , b1 = b[i] ;
	int a2 = a[j] , b2 = b[j] ; 

	if ( a1 > a2 && b1 > b2 ) { return 0 ; } 
	else if ( a1 > a2 && b1 < b2 ) { return 1 ; } 
	else if ( a1 < a2 && b1 > b2 ) { return 1 ; }
	else { return 0 ; } 
}

int main () {		
	int i, j ;
	int tests ;
	scanf("%d",&tests ) ;
	int numbers = 0 ;
	while ( tests -- ) {
		numbers ++ ;
		answer = 0 ;
		scanf("%d", &N ) ;
		for ( i = 0 ;  i < N; i ++ ) {
			scanf("%d%d",&a[i],&b[i]) ;
		}

		for ( i = 0 ; i < N ; i ++ ) {
			for ( j = i+1 ; j < N ; j ++ ) {
				if ( intersect(i,j) == 1 ) { answer ++ ; }
			}
		}
		
		printf("Case #%d: %d\n",numbers, answer ) ;
	}
	return 0 ;
}
