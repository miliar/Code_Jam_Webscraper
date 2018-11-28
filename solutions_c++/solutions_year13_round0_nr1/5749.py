#define G2013_QUALIFICATION_A 1
#if G2013_QUALIFICATION_A == 1

#ifndef GIN
	#define GIN "A-small-attempt0.in" 
	#define GOUT "A-small-attempt0.out"
#endif


#ifndef GIN
	#define GIN "input.txt" 
	#define GOUT "output.txt"
#endif



#define myfile(B) ("E:\\CodeJam\\A\\"##B)

#include <SDKDDKVer.h>
#include <stdio.h>
#include <tchar.h>
#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <queue>
using namespace std;

ifstream g_infile;
ofstream g_outfile;
#define read(x) {g_infile >> x;}
#define readtoendl() {string x; g_infile >> x;}
#define readline(x) {std::getline(g_infile, x);}
#define write(x) {g_outfile << x;}
#define result_head(x) {g_outfile << "Case #"; g_outfile << x;  g_outfile << ": ";}
#define result_endl() {g_outfile << std::endl;}

char board[4][4];
#define ISCH(a, b) (a == b || a == 'T')

enum DIR {RIGHT, DOWN, RIGHTBOTTOM, LEFTBOTTOM};

bool g_not_done = false;

bool check(int i, int j, DIR dir, char judgechar) {
	int row = i; 
	int col = j;
	
	if (i < 0 || j < 0 || i > 3 || j > 3) return true;

	if (board[i][j] == '.') g_not_done = true;

	switch(dir) {
		case RIGHT: col++; break;
		case DOWN: row++; break;
		case RIGHTBOTTOM: col++; row++; break;
		case LEFTBOTTOM: col--; row++; break;
	}

	if (ISCH(board[i][j], judgechar) &&
		check(row, col, dir, judgechar)) {
		return true;
	} else {
		return false;
	}
}

bool won(char party) {
	bool w = false;
	int row, col;

	for (row = 0; row < 4; ++row) {
		w = check(row, 0, RIGHT, party);
		if (w) 
			return true;
	}

	for (col = 0; col < 4; ++col) {
		w = check(0, col, DOWN, party);
		if (w) 
			return true;
	}

	w = check(0, 0, RIGHTBOTTOM, party);
	if (w)
		return true;

	w = check(0, 3, LEFTBOTTOM, party);
	if (w) return true;

	return false;
}

void alg() {
	char c;
	int N; 

	read(N); 
	for (int i = 1; i <= N; ++i) {
		// load the board
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				read(c);
				board[j][k] = c;
			}
		}

		// print the board for debug
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				printf("%c", board[j][k]);
			}
			printf("\r\n");
		}
		printf("\r\n");

		bool o = false, x = false;
		g_not_done = false;
		for (int j = 0; j < 4; ++j) {
			o = won('O');
			if (o) break;
			x = won('X');
			if (x) break;
		}

		string result = "Draw";
		if (o) result = "O won";
		else if (x) result = "X won";
		else if (g_not_done) result = "Game has not completed";

		result_head(i);
		write(result);
		result_endl();
	}
}

int main(int argc, _TCHAR* argv[])
{
	g_infile.open(myfile(GIN), ifstream::in);
	g_outfile.open(myfile(GOUT), ifstream::out);

	alg();

	g_outfile.close();
	g_infile.close();
	return 0;
}

#endif