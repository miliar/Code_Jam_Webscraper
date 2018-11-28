#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int numX(string s) {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (s[i] == 'X' || s[i] == 'T')
			count++;
	}
	return count;
}

int numO(string s) {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (s[i] == 'O' || s[i] == 'T')
			count++;
	}
	return count;
}

int numXV(string s[], int col) {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (s[i][col] == 'X' || s[i][col] == 'T')
			count++;
	}
	return count;
}

int numOV(string s[], int col) {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (s[i][col] == 'O' || s[i][col] == 'T')
			count++;
	}
	return count;
}

int numXD(string s[]) {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (s[i][i] == 'X' || s[i][i] == 'T')
			count++;
	}
	return count;
}

int numOD(string s[]) {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (s[i][i] == 'O' || s[i][i] == 'T')
			count++;
	}
	return count;
}

int numXD2(string s[]) {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (s[i][3-i] == 'X' || s[i][3-i] == 'T')
			count++;
	}
	return count;
}

int numOD2(string s[]) {
	int count = 0;
	for (int i = 0; i < 4; i++) {
		if (s[i][3-i] == 'O' || s[i][3-i] == 'T')
			count++;
	}
	return count;
}

string process(string board[]) {
	bool emptySpace = false;
	for (int k = 0; k < 4; k++) {
		string t = board[k];
		int numx = numX(t);
		int numo = numO(t);
		if (numx == 4) {
			return "X won";
		}
		else if (numo == 4) {
			return "O won";
		}
		else if (!emptySpace && numx + numo < 4) {
			emptySpace = true;
		}
	}

	for (int j = 0; j < 4; j++) {
		int numx = numXV(board, j);
		int numo = numOV(board, j);
		if (numx == 4) {
			return "X won";
		}
		else if (numo == 4) {
			return "O won";
		}
	}

	if (numXD(board) == 4) {
		return "X won";
	}

	if (numXD2(board) == 4) {
		return "X won";
	}

	if (numOD(board) == 4) {
		return "O won";
	}

	if (numOD2(board) == 4) {
		return "O won";
	}

	if (emptySpace)
		return "Game has not completed";

	return "Draw";
}


int main() {


	int t;
	cin >> t;

	string board[4];

	for (int i = 0; i < t; i++)
	{
		for (int j = 0; j < 4; j++) {
			cin >> board[j];
		}

		cout << "Case #";
		cout << i + 1;
		cout << ": ";
		cout << process(board);
		cout << endl;

		cin;
	}

    return 0;
}
