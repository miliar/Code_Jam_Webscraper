/*
 * Round1A10_A.cpp
 *
 *  Created on: May 22, 2010
 *      Author: Jad
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <stack>
#include <gmp.h>
using namespace std;

#define RED "Red"
#define BLUE "Blue"
#define BOTH "Both"
#define NEITHER "Neither"

#define SIZE 51

ifstream fin("GCJ2010/in");
ofstream fout("GCJ2010/out");

int N,K;
char board[SIZE][SIZE];


vector<char> compressRow(int row) {
	vector<char> compressed;
	for(int i=N-1; i>=0; i--)
		if(board[row][i]!='.')
			compressed.push_back(board[row][i]);

	while((int)compressed.size()<N)
		compressed.push_back('.');

	return compressed;
}


void rotate() {
	vector<char> rows[SIZE];
	for(int i=0; i<N; i++)
		rows[i] = compressRow(i);

	for(int i=0; i<N; i++) {
		for(int j=0; j<N; j++) {
			board[N-1-j][N-1-i] = rows[i][j];
		}
	}
}


void update(char piece, int &state, int &cnt, bool &red, bool &blue) {
	if(piece=='.')
		state=cnt=0;
	else if(piece=='R') {
		if(state!=1) {
			state=1;
			cnt=1;
		}
		else
			cnt++;
	}
	else {
		if(state!=2) {
			state=2;
			cnt=1;
		}
		else
			cnt++;
	}

	if(cnt==K && state==1)
		red=true;
	else if(cnt==K && state==2)
		blue=true;
}


string checkKWin() {
	bool red=false, blue=false;

	//check rows
	for(int i=0; i<N; i++) {
		int state=0, cnt=0;
		for(int j=0; j<N; j++) {
			update(board[i][j], state, cnt, red, blue);
		}
	}

	//check columns
	for(int j=0; j<N; j++) {
		int state=0, cnt=0;
		for(int i=0; i<N; i++) {
			update(board[i][j], state, cnt, red, blue);
		}
	}

	//check diagonals
	for(int i=0; i<N; i++) {
		int state=0, cnt=0;
		for(int j=0; j<=i; j++) {
			update(board[i-j][j], state, cnt, red, blue);
		}
		state=cnt=0;
		for(int j=0; i+j<N; j++) {
			update(board[i+j][j], state, cnt, red, blue);
		}
		state=cnt=0;
		for(int j=0; j<=i; j++) {
			update(board[i-j][N-1-j], state, cnt, red, blue);
		}
		state=cnt=0;
		for(int j=0; i+j<N; j++) {
			update(board[i+j][N-1-j], state, cnt, red, blue);
		}
	}

	if(!red && !blue)
		return NEITHER;
	else if(!red && blue)
		return BLUE;
	else if(red && !blue)
		return RED;
	else
		return BOTH;
}

void print() {
	fout<<endl;
	for(int i=0; i<N; i++) {
		fout<<"  ";
		for(int j=0; j<N; j++)
			fout<<board[i][j];
		fout<<endl;
	}
	fout<<endl;
}


int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		fin>>N>>K;
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				fin>>board[i][j];

		rotate();
//		print();
		string result = checkKWin();

		fout<<"Case #"<<t<<": "<<result<<endl;
	}

	return 0;
}
