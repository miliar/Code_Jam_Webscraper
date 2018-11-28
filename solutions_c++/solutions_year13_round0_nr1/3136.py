#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;

int main(){
	int N, case_num;
	char board[4][4];
	cin >> N;
	for (case_num = 1; case_num <= N; ++case_num){
		// Read into board
		while (getchar() != '\n');
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				board[i][j]=getchar();
			}
			while (getchar() != '\n');
		}

		// Find if there is empty spot
		bool found_dot = false;
		for (int i = 0; (i < 4) && !found_dot; i++){
			for (int j = 0; (j < 4) && !found_dot; j++){
				if (board[i][j] == '.') found_dot = true;
			}
		}

		// Check 10 possible arrangements for winner
		bool x_win = false, o_win = false;
		// First check 4 rows
		for (int i = 0; (i < 4) && !x_win && !o_win; i++){
			bool row_x_win = true, row_o_win = true;
			for (int j = 0; j < 4; j++){
				if (row_x_win)
					row_x_win &= (board[i][j] == 'X') || (board[i][j] == 'T');
				if (row_o_win)
					row_o_win &= (board[i][j] == 'O') || (board[i][j] == 'T');
			}
			x_win = row_x_win;
			o_win = row_o_win;
		}

		// Then check 4 cols
		for (int j = 0; (j < 4) && !x_win && !o_win; j++){
			bool col_x_win = true, col_o_win = true;
			for (int i = 0; i < 4; i++){
				if (col_x_win)
					col_x_win &= (board[i][j] == 'X') || (board[i][j] == 'T');
				if (col_o_win)
					col_o_win &= (board[i][j] == 'O') || (board[i][j] == 'T');
			}
			x_win = col_x_win;
			o_win = col_o_win;
		}

		// Last check 2 diagonals
		if (!x_win && !o_win){
			bool diag_x_win = true, diag_o_win = true;
			for (int i = 0; i < 4; i++){
				if (diag_x_win)
					diag_x_win &= (board[i][i] == 'X') || (board[i][i] == 'T');
				if (diag_o_win)
					diag_o_win &= (board[i][i] == 'O') || (board[i][i] == 'T');
			}
			x_win = diag_x_win;
			o_win = diag_o_win;
		}
		if (!x_win && !o_win){
			bool diag_x_win = true, diag_o_win = true;
			for (int i = 0; i < 4; i++){
				if (diag_x_win)
					diag_x_win &= (board[i][3-i] == 'X') || (board[i][3-i] == 'T');
				if (diag_o_win)
					diag_o_win &= (board[i][3-i] == 'O') || (board[i][3-i] == 'T');
			}
			x_win = diag_x_win;
			o_win = diag_o_win;
		}

		// Output Results
		cout << "Case #" << case_num << ": ";
		if (x_win)
			cout << "X won" << endl;
		else if (o_win)
			cout << "O won" << endl;
		else if (found_dot)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}
	return 0;
}

