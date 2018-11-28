
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<stack>
#include<queue>

using namespace std ;

int N, M ;
int answer ;
int mat[1000][1000] ;
int diffSize [ 1000] ; 

void fillMat ( int row , char* input ) {
	int j = 0 ; 
	for ( int i = 0 ; i < N/4 ; i ++  ) {
		switch( input[i] ) {
			case '0' :
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				break ;
			case '1' :
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				break ;
			case '2' :
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				break ;
			case '3' :
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				break ;
			case '4' :
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				break ;
			case '5' :
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				break ;
			case '6' :
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				break ;
			case '7' :
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				break ;
			case '8' :
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				break ;
			case '9' :
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				break ;
			case 'A' :
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				break ;
			case 'B' :
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				break ;
			case  'C' :
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 0 ; 
				break ;
			case 'D' :
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				mat[row][j++] = 1 ; 
				break ;
			case 'E' :
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 0 ; 
				break ;
			case 'F' :
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				mat[row][j++] = 1 ; 
				break ;
		}
	}
}


int isSquare ( int i , int j , int s ) {
	int state ;
	for ( int k = 0 ; k < s ; k ++ ) {
		state = 1-mat[i+k][j] ;
		if ( mat[i+k][j] == -1 ) { return 0 ; } 
		for ( int l = 0 ; l < s ; l ++ ) {
			if ( mat[i+k][l+j] == -1 ) { return 0 ; } 
			if ( mat[i+k][l+j] == state ) { return 0 ; } 
			state = 1 - state ; 
		}
	}

	state = 1-mat[i][j] ;
	for ( int k = 0 ; k < s ; k ++ ) {
		if ( mat[i+k][j] == -1 ) { return 0 ; } 
		if ( state == mat[i+k][j] ) { return 0 ; } 
		state = 1 - state ; 
	}
	return 1 ;
}

void makeInvalid ( int i , int j , int s ) {
	for ( int k = 0 ; k < s ; k ++ ) {
		for ( int l = 0 ; l < s ; l ++ ) {
			mat[i+k][l+j] = -1 ;
		}
	}
	return ;
}

int main () {		
	int i, j ;
	int tests ;
	char input [10000] ;
	scanf("%d",&tests ) ;
	int numbers = 0 ;
	while ( tests -- ) {
		numbers ++ ;
		scanf("%d%d",&M, &N ) ;
		for ( i = 0 ; i < M ;  i ++ ) {
			scanf("%s",input) ; 
			fillMat(i, input ) ; 
		}

		int maxSize = M > N ? N : M ; 

		for ( i = 1 ; i <= maxSize ; i ++ ) {
			diffSize[i] = 0 ;
		}
		
		for ( int s = maxSize ; s > 0 ; s -- ) {
			for ( i = 0 ; i <= M-s ; i ++ ) {
				for ( j = 0 ; j <= N-s ; j ++ ) {
					if ( isSquare(i,j,s) == 1 ) {
						diffSize [s] ++ ; 
						makeInvalid(i,j,s) ; 
					}
				}
			}
		}

		answer = 0 ;
		for ( i = maxSize ; i > 0 ; i -- ) {
			if ( diffSize[i] != 0 ) { answer ++ ; } 
		}
		
		printf("Case #%d: %d\n",numbers, answer ) ;
		for ( i = maxSize ; i > 0 ; i -- ) {
			if ( diffSize[i] != 0 ) {
				printf("%d %d\n",i,diffSize[i] ) ;
			}
		}
	}
	return 0 ;
}
