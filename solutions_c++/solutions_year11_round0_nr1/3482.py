#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <iostream>

int o[102] ;
int b[102] ;


using namespace std ;

int ABS ( int x ) {
	if ( x  > 0 ) {
		return x ;
	}
	return -1*x ;
}

queue<char> nextColor ;
queue<int> blueNext ;
queue<int> orangeNext ;

int main () {
	int n ;
	char ch ;
	int button ;
	int Kases ; 
	int moves ; 
	int tempSteps ;
	int orange, blue, steps ;
	int next_orange, next_blue ;
	char next_color ;
	cin >> Kases ;
	for ( int kases = 0 ; kases < Kases ; kases ++ ) {
		cin >> n ;
		for ( int i = 0 ; i < n ; i ++ ) {
			scanf(" %c %d",&ch,&button) ;
			nextColor.push(ch) ;
			if ( ch == 'O' ) {
				orangeNext.push(button);
			} else {
				blueNext.push(button) ;
			}
		}

		moves = 0 ;
		orange = 1 ; 
		blue = 1 ;
		next_orange = orangeNext.size() != 0 ? orangeNext.front() : -1 ; 
		if ( next_orange != -1 ) { orangeNext.pop() ; }
		next_blue = blueNext.size() != 0 ? blueNext.front() : -1 ; 
		if ( next_blue != -1 ) { blueNext.pop() ; } 
		next_color = nextColor.front() ; 
		nextColor.pop() ;
		while ( next_orange != -1 && next_blue != -1 ) {
			if ( next_color == 'O' ) {
				steps = ABS((orange-next_orange)) + 1 ;	
				orange = next_orange ;
				next_orange = orangeNext.size() != 0 ? orangeNext.front() : -1 ; 
				if ( next_orange != -1 ) { orangeNext.pop() ; }
				tempSteps = ABS((blue-next_blue)) ;
				if ( tempSteps <= steps ) {
					blue = next_blue ;
				} else if ( blue > next_blue ) {
					blue -= steps ;
				} else if ( blue < next_blue ) {
					blue += steps ;
				}
			} else {
				steps = ABS((blue-next_blue)) + 1 ;	
				blue = next_blue ;
				next_blue = blueNext.size() != 0 ? blueNext.front() : -1 ; 
				if ( next_blue != -1 ) { blueNext.pop() ; } 
				tempSteps = ABS((orange-next_orange)) ;
				if ( tempSteps <= steps ) {
					orange = next_orange ;
				} else if ( orange > next_orange ) {
					orange -= steps ;
				} else if ( orange < next_orange ) {
					orange += steps ;
				}
			}
			moves += steps ;
			next_color = nextColor.front() ; 
			nextColor.pop() ;
		}

		while ( next_orange != -1 ) {
			moves += ( ABS((orange-next_orange)) + 1 )  ;	
			orange = next_orange ;
			next_orange = orangeNext.size() != 0 ? orangeNext.front() : -1 ; 
			if ( next_orange != -1 ) { orangeNext.pop() ; }
			nextColor.pop() ;
		}

		while ( next_blue != -1 ) {
			moves += ( ABS((blue-next_blue)) + 1 )  ;	
			blue = next_blue ;
			next_blue = blueNext.size() != 0 ? blueNext.front() : -1 ; 
			if ( next_blue != -1 ) { blueNext.pop() ; } 
			nextColor.pop() ;
		}
		nextColor.push(0) ;

		printf("Case #%d: %d\n", kases+1, moves ) ;

	}
	return 0 ;
}
