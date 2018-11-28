
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<stack>
#include<queue>

using namespace std ;

int N , M ;
int noMadeDir = 0 ;
int newMadeDir = 0 ;
char madeDir[10000000][111] ; 

void fillInInput ( char* input ) {
	int i ;
	if ( input[0] == 0 ) { return ; } 

	// Search for this dir 
	for ( i = 0 ; i < noMadeDir ; i ++ ) {
		if ( strcmp( input, madeDir[i] ) == 0 ) {
			return ; 
		}
	} 
	
	// This Dir is not created 
	strcpy ( madeDir[noMadeDir], input ) ;
	noMadeDir ++ ; 
	newMadeDir ++ ;

	// get parent path 
	int l = strlen ( input ) ;
	l -- ;
	while ( input[l] != '/' ) { input[l] = 0 ; l -- ; }
	input[l] = 0 ;
	fillInInput(input) ;
	return ;

}

void printMadeDir ( void ) {
	printf("These were made\n") ;
	for ( int i = 0 ; i < noMadeDir ; i ++ ) {
		printf("%s\n",madeDir[i] ) ;
	}
}


int main () {		
	int i, j ;
	int number = 0 ;
	int tests ;
	char input [111] ; 
	scanf("%d",&tests ) ;
	while ( tests -- ) {
		number ++ ;
		scanf(" %d%d ", &N, &M ) ;
		madeDir[0][0] = '/' ; madeDir[0][1] = '\0' ; 
		noMadeDir = 1 ;
		for ( i = 1 ; i <= N ; i ++ ) {
			scanf(" %s ",madeDir[i] ) ;
			noMadeDir ++ ;
		}
		newMadeDir = 0 ;
		
		for ( i = 0 ; i < M ; i ++ ) {
			scanf(" %s ",input) ;
			fillInInput( input ) ; 
		}
			
		printf("Case #%d: %d\n",number,newMadeDir ) ;	
			
	}
	return 0 ;
}
