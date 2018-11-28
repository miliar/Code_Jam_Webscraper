#include <iostream>

#define TTTT_X_WON 		(1)
#define TTTT_O_WON 		(2)
#define TTTT_DRAW 		(3)
#define TTTT_NOTOVER	(4)

#define TTTT_DOT		(0)
#define TTTT_X			(1)
#define TTTT_O			(2)
#define TTTT_T			(10)

using namespace std;

int tttt_parseboard(int board[4][4])
{
	int row, col;
	char c;
	for(row=0; row < 4; row++) {
		for ( col=0; col < 4; col++ ) {
			cin>>c;
			
			switch(c) {
				case 'X':
					board[row][col] = TTTT_X;
					break;
				case 'O':
					board[row][col] = TTTT_O;
					break;
				case '.':
					board[row][col] = TTTT_DOT;
					break;
				case 'T':
					board[row][col] = TTTT_T;
					break;
			}


		}
	}

	return 0;
}


int tttt_state(int board[4][4])
{
	int mul;
	bool notOver = false;

	// Check diagonal wise if somebody won
	mul = board[0][0] * board [1][1] * board [2][2] * board[3][3];
	if( 0 == mul ) notOver = true; 
	if ( 1 == mul || 10 == mul ) return TTTT_X_WON;
	if ( 16 == mul || 80 == mul ) return TTTT_O_WON;

	// Not conclusive. Check the other diagonal
	mul = board[0][3] * board [1][2] * board [2][1] * board[3][0];
	if( 0 == mul ) notOver = true; 
	if ( 1 == mul || 10 == mul ) return TTTT_X_WON;
	if ( 16 == mul || 80 == mul ) return TTTT_O_WON;

	// Check the row wise
	for(int row=0; row < 4; row++) {
		mul = board[row][0] * board [row][1] * board [row][2] * board[row][3];
		if( 0 == mul ) notOver = true; 
		if ( 1 == mul || 10 == mul ) return TTTT_X_WON;
		if ( 16 == mul || 80 == mul ) return TTTT_O_WON;
	}

	// Check col wise if somebody won
	for(int col =0; col < 4; col ++) {
		mul = board[0][col] * board [1][col] * board [2][col] * board[3][col];
		if( 0 == mul ) notOver = true; 
		if ( 1 == mul || 10 == mul ) return TTTT_X_WON;
		if ( 16 == mul || 80 == mul ) return TTTT_O_WON;
	}

	return notOver? TTTT_NOTOVER:TTTT_DRAW;
}

int tttt_status(int caseN, int state)
{
	cout << " Case #" << caseN;
	
	switch(state) {
		case TTTT_X_WON :
			cout << ": X won" << endl;
			break;
		case TTTT_O_WON:
			cout << ": O won" << endl;
			break;
		case TTTT_DRAW:
			cout << ": Draw" << endl;
			break;
		case TTTT_NOTOVER:
			cout << ": Game has not completed" << endl;
			break;
		default:
			cerr << ": ERROR: Unknown state" << endl;
	}
	return 0;
}

int main()
{
	int board[4][4];
	int n, state;
	cin>>n;

	for(int i = 0; i < n; ++i) {
		tttt_parseboard(board);
		state = tttt_state(board);
		tttt_status(i+1, state);
	}

	return 0;
}

