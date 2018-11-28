//============================================================================
// Name        : TicTacTomek.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {
	ifstream infile;
	infile.open(argv[1]);
	int ncases;
	infile >> ncases;

	for (int i=0; i<ncases; ++i) {
		char board[4][4];
		bool complete = true;
		for (int j=0; j<4; ++j) {
			for (int k=0; k<4; ++k) {
				char nextchar;
				infile >> nextchar;
				if (nextchar == '.') {
					complete = false;
				}
				board[j][k] = nextchar;;
			}
		}
		bool xwon = false;
		bool ywon = false;
		bool fail = false;
		char player;
		for (int j=0; j<4; ++j) {
			fail = false;
			player = board[j][0];
			if (player == 'T') { player = board[j][1]; }
			for (int k=0; k<4; ++k) {
				if (board[j][k] != player && board[j][k] != 'T') {
					fail = true;
				}
			}
			if (!fail && player=='X') {
				xwon = true;
			}
			else if (!fail && player=='O') {
				ywon = true;
			}
		}
		for (int j=0; j<4; ++j) {
			fail = false;
			player = board[0][j];
			if (player == 'T') { player = board[1][j]; }
			for (int k=0; k<4; ++k) {
				if (board[k][j] != player && board[k][j] != 'T') {
					fail = true;
				}
			}
			if (!fail && player=='X') {
				xwon = true;
			}
			else if (!fail && player=='O') {
				ywon = true;
			}
		}
		fail = false;
		player = board[0][0];
		if (player == 'T') { player = board[1][1]; }
		for (int j=0; j<4; ++j) {
			if (board[j][j] != player && board[j][j] != 'T') {
				fail = true;
			}
		}
		if (!fail && player=='X') {
			xwon = true;
		}
		else if (!fail && player=='O') {
			ywon = true;
		}

		fail = false;
		player = board[0][3];
		if (player == 'T') { player = board[1][2]; }
		for (int j=0; j<4; ++j) {
			if (board[j][3-j] != player && board[j][3-j] != 'T') {
				fail = true;
			}
		}
		if (!fail && player=='X') {
			xwon = true;
		}
		else if (!fail && player=='O') {
			ywon = true;
		}

		if (xwon && !ywon) {
			cout << "Case #" << i+1 << ": X won" << endl;
		}
		else if (ywon && !xwon) {
			cout << "Case #" << i+1 << ": O won" << endl;
		}
		else if (complete) {
			cout << "Case #" << i+1 << ": Draw" << endl;
		}
		else {
			cout << "Case #" << i+1 << ": Game has not completed" << endl;
		}
	}
}
