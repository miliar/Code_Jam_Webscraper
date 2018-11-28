#include <stdio.h>
#include <stdlib.h>

#include <vector>


// P : ( 1, 100 )
// T : ( 1, 20 ) / ( 1, 100 )
// N : ( 1, 10 ) / ( 1, 100 )


#define Turn_o 0
#define Turn_b 1

using namespace std;

int process( vector< int > btnSeq_o, int index_o, int curPos_o, 
		  vector< int > btnSeq_b, int index_b, int curPos_b, 
		  vector< int > turns, int index_t, 
		  int n );


void main(){

	// file open
	FILE *fpInput = fopen( "input.txt", "r" );
	FILE *fpOutput = fopen( "output.txt", "w+" );

	if( fpInput == NULL ) return;
	if( fpOutput== NULL ) return;


	// get T, N
	int T;
	int N;

	vector< int > btnSeq_o;
	vector< int > btnSeq_b;
	vector< int > turns;

	int index_o = 0;
	int index_b = 0;

	int curPos_o = 1;
	int curPos_b = 1;

	int index_t = 0;


	// T
	fscanf( fpInput, "%d", &T );

	int i, j, n;
	char c;

	for( i= 0; i< T; i++ ){

		btnSeq_o.clear();
		btnSeq_b.clear();
		turns.clear();

		fscanf( fpInput, "%d", &N );

		for( j= 0; j< N; j++ ){

			fscanf( fpInput, " %c", &c );
			fscanf( fpInput, " %d", &n );

			if( c == 'O' ){

				btnSeq_o.push_back( n );
				turns.push_back( Turn_o );
			}
			else if( c == 'B' ){

				btnSeq_b.push_back( n );
				turns.push_back( Turn_b );
			}
			else
				return;
		}

		
		index_o = index_b = 0;
		curPos_o = curPos_b = 1;
		index_t = 0;
		n = 0;

		fprintf( fpOutput, "Case #%d: %d\n", i+1, process( btnSeq_o, index_o, curPos_o, btnSeq_b, index_b, curPos_b, turns, index_t, n ) );
	}

	fclose( fpInput );
	fclose( fpOutput );
}




int process( vector< int > btnSeq_o, int index_o, int curPos_o, 
		  vector< int > btnSeq_b, int index_b, int curPos_b, 
		  vector< int > turns, int index_t, int n ){

	int curTurn = turns[ index_t ];
	
	//printf( "\nnew turn\n" );

	// o 로봇

	if( index_o < btnSeq_o.size() ){ 

		if( curPos_o == btnSeq_o[ index_o ] ){

			// 자기 순서면 버튼을 누르고 / 아니라면 머무른다
			if( curTurn == Turn_o ){

				index_o += 1;
				index_t += 1;
				//printf( "o : press\n" );
			}
		}
		else if( curPos_o < btnSeq_o[ index_o ] ){

			curPos_o += 1;
			//printf( "o : go\n" );
		}
		else if( curPos_o > btnSeq_o[ index_o ] ){

			curPos_o -= 1;
		}
	}

	// b 로봇

	if( index_b < btnSeq_b.size() ){ 

		if( curPos_b == btnSeq_b[ index_b ] ){

			// 자기 순서면 버튼을 누르고 / 아니라면 머무른다
			if( curTurn == Turn_b ){

				index_b += 1;
				index_t += 1;
				//printf( "b : press\n" );
			}
		}
		else if( curPos_b < btnSeq_b[ index_b ] ){

			curPos_b += 1;
			//printf( "b : go\n" );
		}
		else if( curPos_b > btnSeq_b[ index_b ] ){

			curPos_b -= 1;
		}
	}

	
	// 종료

	if( ( index_o >= btnSeq_o.size() ) && ( index_b >= btnSeq_b.size() ) ){

		return n+1;
	}

	return process( btnSeq_o, index_o, curPos_o, btnSeq_b, index_b, curPos_b, turns, index_t, n+1 );
}