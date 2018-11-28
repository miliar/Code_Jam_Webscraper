/*
 * =====================================================================================
 *
 *       Filename:  A.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/13/2013 02:01:35 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Lei Zhang (antiAgainst), antiagainst@gmail.com
 *   Organization:  University of Waterloo
 *
 * =====================================================================================
 */
#include <iostream>

using namespace std;

int check(char board[4][4]) {
	int nx, no, nt;
	int i, j;
	bool full = true;
	for (i = 0; i < 4; i++) {
		nx = no = nt = 0;
		for (j = 0; j < 4; j++) {
			if (board[i][j] == 'X')
				nx++;
			else if (board[i][j] == 'O')
				no++;
			else if (board[i][j] == 'T')
				nt++;
			else full = false;
		}
		if (nx == 4 || nx == 3 && nt == 1) return 1;
		if (no == 4 || no == 3 && nt == 1) return 2;
	}
	for (j = 0; j < 4; j++) {
		nx = no = nt = 0;
		for (i = 0; i < 4; i++) {
			if (board[i][j] == 'X')
				nx++;
			else if (board[i][j] == 'O')
				no++;
			else if (board[i][j] == 'T')
				nt++;
			else full = false;
		}
		if (nx == 4 || nx == 3 && nt == 1) return 1;
		if (no == 4 || no == 3 && nt == 1) return 2;
	}
	nx = no = nt = 0;
	for (i = 0; i < 4; i++) {
		if (board[i][i] == 'X')
			nx++;
		else if (board[i][i] == 'O')
			no++;
		else if (board[i][i] == 'T')
			nt++;
		else full = false;
	}
	if (nx == 4 || nx == 3 && nt == 1) return 1;
	if (no == 4 || no == 3 && nt == 1) return 2;
	nx = no = nt = 0;
	for (i = 0; i < 4; i++) {
		if (board[i][3 - i] == 'X')
			nx++;
		else if (board[i][3 - i] == 'O')
			no++;
		else if (board[i][3 - i] == 'T')
			nt++;
		else full = false;
	}
	if (nx == 4 || nx == 3 && nt == 1) return 1;
	if (no == 4 || no == 3 && nt == 1) return 2;
	if (full) return 3;
	return 4;
}

int main() {
	int tc, res;
	char board[4][4];

	cin >> tc;
	for (int ti = 0; ti < tc; ti++) {
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> board[i][j];
		res = check(board);
		cout << "Case #" << ti + 1 << ": ";
		if (res == 1) cout << "X won";
		else if (res == 2) cout << "O won";
		else if (res == 3) cout << "Draw";
		else if (res == 4) cout << "Game has not completed";
		cout << endl;
	}
}

