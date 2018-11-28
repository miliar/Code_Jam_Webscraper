/*
ID: cyanophycean314
*/
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <sstream>
#include <algorithm>
using namespace std;

string checkState(char brd[][4]) {
	//return "hi";
	//Check Horizontal
	int total = 0;
	bool tomek = false;
	for (int i = 0; i < 4; i++) {
		total = 0;
		tomek = false;
		for (int j = 0; j < 4; j++) {
			if (brd[i][j] == 'O')
				total++;
			if (brd[i][j] == 'X')
				total--;
			if (brd[i][j] == 'T')
				tomek = true;
		}
		if (total == 4 || (tomek && total == 3))
			return "O won";
		if (total == -4 || (tomek && total == -3))
			return "X won";
	}
	
	//Check vertical
	for (int i = 0; i < 4; i++) {
		total = 0;
		tomek = false;
		for (int j = 0; j < 4; j++) {
			if (brd[j][i] == 'O')
				total++;
			if (brd[j][i] == 'X')
				total--;
			if (brd[j][i] == 'T')
				tomek = true;
		}
		if (total == 4 || (tomek && total == 3))
			return "O won";
		if (total == -4 || (tomek && total == -3))
			return "X won";
	}
	
	//Check Diagonal 1
	total = 0;
	tomek = false;
	for (int i = 0; i < 4; i++) {
		if (brd[i][i] == 'O')
			total++;
		if (brd[i][i] == 'X')
			total--;
		if (brd[i][i] == 'T')
			tomek = true;
	}
	if (total == 4 || (tomek && total == 3))
		return "O won";
	if (total == -4 || (tomek && total == -3))
		return "X won";
	
	//Check Diagonal 2
	total = 0;
	tomek = false;
	for (int i = 0; i < 4; i++) {
		if (brd[i][3-i] == 'O')
			total++;
		if (brd[i][3-i] == 'X')
			total--;
		if (brd[i][3-i] == 'T')
			tomek = true;
	}
	if (total == 4 || (tomek && total == 3))
		return "O won";
	if (total == -4 || (tomek && total == -3))
		return "X won";
	
	total = 0;
	tomek = false;
	//Everything has been checked. If open space, game is not done.
	//If no open space, it's a draw.
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (brd[i][j] == '.')
				return "Game has not completed";
		}
	}
	//Well, I guess it's a draw
	return "Draw";
}

int main() {
	ifstream fin("tomek.in");
	ofstream fout("tomek.out");
	
	int N;
	fin >> N;
	
	for (int count = 0; count < N; count++) {
		char board[4][4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++)
				fin >> board[i][j];
		}
		
		fout << "Case #" << (count + 1) << ": " << checkState(board) << endl;
	}
	return 0;
}
