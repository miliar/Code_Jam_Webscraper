/*
 * main.cpp
 *
 *  Created on: 12/04/2013
 *      Author: Eden
 */
#include <iostream>
#include <fstream>
using namespace std;

const int X = 0;
const int O = 1;
const int T = 2;
const int BLANK = 3;

bool check(int arr[4][4], int a) {
	for (int i = 0; i < 4; i++) {
		if (arr[i][i] != a && arr[i][i] != T) {
			break;
		}
		if (i == 3)
			return true;
	}
	for (int i = 0; i < 4; i++) {
		if (arr[i][3 - i] != a && arr[i][3 - i] != T) {
			break;
		}
		if (i == 3)
			return true;
	}
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (arr[i][j] != a && arr[i][j] != T) {
				break;
			}
			if (j == 3)
				return true;
		}

	}
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (arr[j][i] != a && arr[j][i] != T) {
				break;
			}
			if (j == 3)
				return true;
		}

	}
	return false;
}

bool full (int arr[4][4]){
	for (int i = 0;i<4;i++){
		for(int j=0;j<4;j++){
			if (arr[i][j] == BLANK)
				return false;
		}
	}
	return true;
}

int main() {
	ifstream myfile("C:\\users\\eden\\A-large.in");
	ofstream output("C:\\users\\eden\\out.txt");
	if (!myfile || !output) {
		cout << "FAIL";
		return 0;
	}
	int N;
	char temp;
	int board[4][4];
	myfile >> N;
	for (int i = 1; i <= N; i++) {
		output << "Case #" << i << ": ";
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				myfile >> temp;
				switch (temp) {
				case 'X':
					board[j][k] = X;
					break;
				case 'O':
					board[j][k] = O;
					break;
				case 'T':
					board[j][k] = T;
					break;
				default:
					board[j][k] = BLANK;
				}
			}
		}
		if (check(board, X)) {
			output << "X won" << endl;
			continue;
		}
		if (check(board, O)) {
			output << "O won" << endl;
			continue;
		}
		if (full(board)) {
			output << "Draw" << endl;
			continue;
		}
		output << "Game has not completed" << endl;
	}
	myfile.close();
	output.close();
	return 0;
}

