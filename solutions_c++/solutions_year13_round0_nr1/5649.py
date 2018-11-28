/*
 * main.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: steven
 */
#include <fstream>
#include <iostream>
using namespace std;

int main() {
	ifstream f;
	ofstream o;
	o.open("/home/steven/workspace/cj/outA");
	f.open("/home/steven/workspace/cj/inA");
	//input stuff
	int cases;
	if (!f.good()) return -1;
	f >> cases;
	char board[4][4];
	int *ans = new int[cases];
	for (int i = 0; i < cases; i++) {
		ans[i] = 10;
	}
	for (int step = 0; step < cases; step++) {
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				f >> board[i][j];
			}
		}
		//find answer
		for (int i = 0; i < 4; i++) {
			if (board[i][0]=='X') {
				//check neg diagonal
				if (i==0&&((board[1][1]=='X')||(board[1][1]=='T'))) {
					if (board[2][2]=='X'||board[2][2]=='T')
						if (board[3][3]=='X'||board[3][3]=='T') ans[step] = 0;
				} else
				//check pos diagonal
				if (i==3&&((board[2][1]=='X')||(board[2][1]=='T'))) {
					if (board[1][2]=='X'||board[1][2]=='T')
						if (board[0][3]=='X'||board[0][3]=='T') ans[step] = 0;
				} else
				//check column
				if ((board[i][1]=='X')||board[i][1]=='T')
					if (board[i][2]=='X'||board[i][2]=='T')
						if (board[i][3]=='X'||board[i][3]=='T') ans[step] = 0;
			} else if (board[i][0]=='O') {
				//check neg diagonal
				if (i==0&&((board[1][1]=='O')||(board[1][1]=='T'))) {
					if (board[2][2]=='O'||board[2][2]=='T')
						if (board[3][3]=='O'||board[3][3]=='T') ans[step] = 1;
				} else
				//check pos diagonal
				if (i==3&&((board[2][1]=='O')||(board[2][1]=='T'))) {
					if (board[1][2]=='O'||board[1][2]=='T')
						if (board[0][3]=='O'||board[0][3]=='T') ans[step] = 1;
				} else
				//check column
				if ((board[i][1]=='O')||board[i][1]=='T')
					if (board[i][2]=='O'||board[i][2]=='T')
						if (board[i][3]=='O'||board[i][3]=='T') ans[step] = 1;
			} else if (board[i][0]=='T') {
				//check neg diagonal X
				if (i==0&&((board[1][1]=='X'))) {
					if (board[2][2]=='X')
						if (board[3][3]=='X') ans[step] = 0;
				} else
				//check pos diagonal X
				if (i==3&&((board[2][1]=='X'))) {
					if (board[1][2]=='X')
						if (board[0][3]=='X') ans[step] = 0;
				} else
				//check column X
				if ((board[i][1]=='X'))
					if (board[i][2]=='X')
						if (board[i][3]=='X') ans[step] = 0;
				//check neg diagonal O
				if (i==0&&((board[1][1]=='O'))) {
					if (board[2][2]=='O')
						if (board[3][3]=='O') ans[step] = 1;
				} else
				//check pos diagonal
				if (i==3&&((board[2][1]=='O'))) {
					if (board[1][2]=='O')
						if (board[0][3]=='O') ans[step] = 1;
				} else
				//check column
				if ((board[i][1]=='O'))
					if (board[i][2]=='O')
						if (board[i][3]=='O') ans[step] = 1;
			}
		}
	for (int j = 0; j < 4; j++) {
		if (board[0][j]=='X') {
			if (board[1][j]=='X'||board[1][j]=='T')
				if (board[2][j]=='X'||board[2][j]=='T')
					if (board[3][j]=='X'||board[3][j]=='T') ans[step]=0;
		} else
		if (board[0][j]=='O') {
			if (board[1][j]=='O'||board[1][j]=='T')
				if (board[2][j]=='O'||board[2][j]=='T')
					if (board[3][j]=='O'||board[3][j]=='T') ans[step]=1;
		} else
		if (board[0][j]=='T') {
			if (board[1][j]=='X')
				if (board[2][j]=='X')
					if (board[3][j]=='X') ans[step]=0;
			if (board[1][j]=='O')
				if (board[2][j]=='O')
					if (board[3][j]=='O') ans[step]=1;
		}
	}
		if (ans[step]!=0&&ans[step]!=1) {
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					if (board[i][j]=='.') ans[step]=2;
				}
			}
		}
	}


	//output stuff
	for (int i = 0; i < cases; i++) {
		o << "Case #" << i+1 << ": ";
		switch (ans[i]) {
		case 0:
			o << "X won" << endl;
			break;
		case 1:
			o << "O won" << endl;
			break;
		case 2:
			o << "Game has not completed" << endl;
			break;
		default:
			o << "Draw" << endl;
			break;
		}
	}
	delete[] ans;
	o.close();
	f.close();
}

