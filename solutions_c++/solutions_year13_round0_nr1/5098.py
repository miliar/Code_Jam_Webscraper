#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
#define REP(i, n) for (int i = 0; i < n; ++i)
#define TR(i, x) for (typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define PB push_back
#define MP make_pair
typedef long long ll;

char board[4][4];

string solve(char board[][4]) {
	for (int r = 0; r < 4; ++r) {
		int xNum = 0, oNum = 0, tNum = 0;
		for (int c = 0; c < 4; ++c) {
			xNum += board[r][c] == 'X';
			oNum += board[r][c] == 'O';
			tNum += board[r][c] == 'T';
		}
		if (xNum + tNum == 4)
			return "X won";
		if (oNum + tNum == 4)
			return "O won";
	}
	for (int c = 0; c < 4; ++c) {
		int xNum = 0, oNum = 0, tNum = 0;
		for (int r = 0; r < 4; ++r) {
			xNum += board[r][c] == 'X';
			oNum += board[r][c] == 'O';
			tNum += board[r][c] == 'T';
		}
		if (xNum + tNum == 4)
			return "X won";
		if (oNum + tNum == 4)
			return "O won";
	}
	int xNum = 0, oNum = 0, tNum = 0;
	for (int i = 0; i < 4; ++i) {
		xNum += board[i][i] == 'X';
		oNum += board[i][i] == 'O';
		tNum += board[i][i] == 'T';
	}
	if (xNum + tNum == 4)
		return "X won";
	if (oNum + tNum == 4)
		return "O won";

	xNum = 0, oNum = 0, tNum = 0;
	for (int i = 0; i < 4; ++i) {
		xNum += board[i][3-i] == 'X';
		oNum += board[i][3-i] == 'O';
		tNum += board[i][3-i] == 'T';
	}
	if (xNum + tNum == 4)
		return "X won";
	if (oNum + tNum == 4)
		return "O won";

	for (int r = 0; r < 4; ++r)
		for (int c = 0; c < 4; ++c)
		if (board[r][c] == '.')
			return "Game has not completed";

	return "Draw";
}
int main() {
	int test;
	cin >> test;
	for (int cas = 1; cas <= test; ++cas) {
		for (int i = 0; i < 4; ++i)
			scanf("%s",board[i]);

		printf("Case #%d: %s\n",cas, solve(board).c_str());
	}
}

