// Template for CodeJam by _ClearInbox_
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <numeric>
#include <string>
#include <map>
#include <algorithm>

using namespace std;
void HandleCases(ifstream &fin, ofstream &fout, int caseNum);

int main(int argc, char *argv[]) {
	ifstream fin(argv[1]);
	string out(argv[1]);
	out.replace(out.find(".in"), 3, ".out");
	ofstream fout(out.c_str()); // output
	string line;
	getline(fin, line);
	int cases = atoi(line.c_str());
	for (int i = 0; i < cases; i++) {
		HandleCases(fin, fout, i + 1);
	}
	fin.close();
	fout.close();
	return 0;
}

int row, col;
void changeBoard(string board[], int i, int j) {
	if (board[i][j] == '#' && board[i][j+1] == '#'
			&& board[i+1][j] == '#' && board[i+1][j+1] == '#') {
		board[i][j] = '/';
		board[i][j+1] = '\\';
		board[i+1][j] = '\\';
		board[i+1][j+1] = '/';
	}
}

bool getBoard(string board[]) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			changeBoard(board, i, j);
		}
	}
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			if (board[i][j] == '#') {
				return false;
			}
		}
	}
	return true;
}

void HandleCases(ifstream &fin, ofstream &fout, int caseNum) {
	fout << "Case #" << caseNum << ":" << endl;
	cout << "Case #" << caseNum << ":" << endl; // testing
	string temp;
	fin >> row >> col;
	getline(fin, temp);
	string board[row];
	for (int i = 0; i < row; i++) {
		getline(fin, board[i]);
	}
	int total_blue = 0;
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			if (board[i][j] == '#') {
				total_blue++;
			}
		}
	}
	// cout << total_blue;
	if (total_blue % 4 != 0) {
		fout << "Impossible" << endl; 
	} else {
		if (getBoard(board)) {
			for (int i = 0; i < row; i++) {
				fout << board[i] << endl;
			}
		} else {
			fout << "Impossible" << endl;
		}
	}
}
