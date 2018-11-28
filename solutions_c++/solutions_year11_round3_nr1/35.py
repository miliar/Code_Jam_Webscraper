
#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool ok(int row, int col, vector<string> &board) {
	if (row < 0 || row >= board.size())
		return false;
	if (col < 0 || col >= board[0].size())
		return false;
	return board[row][col] == '#';
}


int main() {
	int testsCount;
	cin >> testsCount;
	for (int test = 0; test < testsCount; ++test) {
		int height, width;
		cin >> height >> width;
		vector<string> board(height);
		for (int row = 0; row < height; ++row) {
			cin >> board[row];
		}
		bool possible = true;
		for (int row = 0; row < height; ++row)
			for (int col = 0; col < width; ++col) {
				if (ok(row, col, board)) {
					if (!ok(row + 1, col, board) || !ok(row, col + 1, board) || !ok(row + 1, col + 1, board)) {
						possible = false;
					} else {
						board[row][col] = '/';
						board[row][col + 1] = '\\';
						board[row + 1][col] = '\\';
						board[row + 1][col + 1] = '/';
					}
					
				}
			}
		printf("Case #%d:\n", test + 1);
		if (possible) {
			for (int row = 0; row < height; ++row)
				cout << board[row] << endl;
		} else {
			cout << "Impossible" << endl;
		}
	}
	return 0;
}