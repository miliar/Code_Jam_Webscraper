/*
 * main.cpp
 *
 *  Created on: 2013-04-13
 *      Author: ronanrmo
 */

#include <iostream>
#include <fstream>
#include <string.h>
#include <map>
#include <vector>
#include <cmath>
#include <list>
#include <string>
#include <sstream>

using namespace std;

string check_game(char board[][4]){

	// check rows
	bool drawrows[4];
	for(int i=0; i<4; i++){
		int O = 0, X = 0, T = 0;
		drawrows[i] = false;
		for(int j=0; j<4; j++){
			if(board[i][j] == 'T') T++;
			if(board[i][j] == 'O') O++;
			if(board[i][j] == 'X') X++;
		}
		if((O+T) == 4)
			return string("O won");
		else if((X+T) == 4)
			return string("X won");
		if(O != 0 && X != 0)
			drawrows[i] = true;
	}

	// check columns
	bool drawcols[4];
		for(int j=0; j<4; j++){
			int O = 0, X = 0, T = 0;
			drawcols[j] = false;
		 	for(int i=0; i<4; i++){
				if(board[i][j] == 'T') T++;
				if(board[i][j] == 'O') O++;
				if(board[i][j] == 'X') X++;
			}
			if((O+T) == 4)
				return string("O won");
			else if((X+T) == 4)
				return string("X won");
			if(O != 0 && X != 0)
				drawcols[j] = true;
		}

	// check main diagonal
	int O = 0, X = 0, T = 0;
	bool drawmain = false;
	for(int i=0; i<4; i++){
		if(board[i][i] == 'T') T++;
		if(board[i][i] == 'O') O++;
		if(board[i][i] == 'X') X++;
	}
	if((O + T) == 4)
		return string("O won");
	else if((X + T) == 4)
		return string("X won");
	if(O != 0 && X != 0)
		drawmain = true;

	// check secondary diagonal
	O = 0, X = 0, T = 0;
	bool drawsec = false;
	for(int i=0; i<4; i++){
		if(board[i][3-i] == 'T') T++;
		if(board[i][3-i] == 'O') O++;
		if(board[i][3-i] == 'X') X++;
	}
	if((O + T) == 4)
		return string("O won");
	else if((X + T) == 4)
		return string("X won");
	if(O != 0 && X != 0)
		drawsec = true;

//	if(drawrows[0] == true && drawrows[1] == true && drawrows[2] == true && drawrows[3] == true &&
//	   drawcols[0] == true && drawcols[1] == true && drawcols[2] == true && drawcols[3] == true &&
//	   drawmain && drawsec)
//		return string("Draw");

	int P = 0;
	for(int i=0; i<4; i++){
		drawrows[i] = false;
		for(int j=0; j<4; j++){
			if(board[i][j] == '.') P++;
		}
	}

	if(P != 0)
		return string("Game has not completed");
	else
		return string("Draw");
}

int main(int argc, char **argv)
{
	istream &in  = (argc>1)?*(new ifstream(argv[1])):cin;
	ostream &out = (argc>2)?*(new ofstream(argv[2])):cout;

	int T;
	in >> T;

	char board[4][4];

	for(int t=0; t<T; t++){
		// reading board
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				in >> board[i][j];
			}
		}

		string res = check_game(board);

		out << "Case #" << t+1 << ": " << res << endl;
	}

	return 0;
}


//		for(int i=0; i<4; i++){
//			for(int j=0; j<4; j++){
//				cout << board[i][j] << " ";
//			}
//			cout << std::endl;
//		}
//		cout << std::endl;


