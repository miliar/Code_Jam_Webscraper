#include <iostream>
#include <fstream>
#include <ostream>
#include <cmath>
#include <cstdlib>
#include <stdio.h>
#include <string>
using namespace std;

//#include "problems.h"

char winner(char board[][4], int r, int c, int dr, int dc){
	char player = 'T';
	for(int i = 0; i < 4; i++){
		if(board[r][c] == '.'){
			return 'T';
		}
		if(player == 'T'){
			player = board[r][c];
		} else if(board[r][c] == 'T'){
		} else if(board[r][c] != player){
			return 'T';
		}
		r += dr;
		c += dc;
	}
	return player;
}

char checkBoard(char board[][4]){
	for(int i = 0; i < 4; i++){
		char player = winner(board, 0, i, 1, 0);
		if(player != 'T'){
			return player;
		}
	}
	for(int i = 0; i < 4; i++){
		char player = winner(board, i, 0, 0, 1);
		if(player != 'T'){
			return player;
		}
	}
	char player = winner(board, 0, 0, 1, 1);
	if(player != 'T'){
		return player;
	}
	player = winner(board, 0, 3, 1, -1);
	if(player != 'T'){
		return player;
	}
	for(int r = 0; r < 4; r++){
		for(int c = 0; c < 4; c++){
			if(board[r][c] == '.'){
				return '.';
			}
		}
	}
	return 'T';
}

void problem1(char* input, char* output){
	ifstream fin;
	fin.open(input);

	ofstream fout;
	fout.open(output);

	char buf[100];

	int n;
	fin >> n;
	for(int t = 0; t < n; t++){
		char board[4][4];
		for(int i = 0; i < 4; i++){
			string line;
			fin >> line;
			for(int j = 0; j < 4; j++){
				board[i][j] = line[j];
			}
		}
		char result = checkBoard(board);
		string message;
		if(result == 'X'){
			message = "X won";
		} else if(result == 'O'){
			message = "O won";
		} else if(result == 'T'){
			message = "Draw";
		} else {
			message = "Game has not completed";
		}
		sprintf(buf, "Case #%d: %s\n", (t+1), message.c_str());
		fout << buf;
	}

	fin.close();
	fout.close();
}


int main(int argc, char** argv){
	char* input = "A-large.in";
	char* output = "A-large.out";

	problem1(input, output);

	return 0;
}
