#include <iostream>
#include <vector>

using std::vector;

/*
	// debug
	std::cout << std::endl;
	for (int row = 0; row < n; row++) {
		for (int col = 0; col < n; col++) {
			std::cout << board_old[row][col];
		}
		std::cout << std::endl;
	}
*/

void rotate(vector<vector<char> > &board_old, int n)
{
	// new empty board
	vector<vector<char> > board_new;
	for (int row = 0; row < n; row++) {
		vector<char> board_new_row;
		for (int col = 0; col < n; col++) {
			board_new_row.push_back('.');
		}
		board_new.push_back(board_new_row);
	}
	// rotate old board into new board
	for (int col_new = 0; col_new < n; col_new++) {
		int row_new = n-1;
		int row_old = n-1-col_new;
		for (int col_old = n-1; col_old >= 0; col_old--) {
			if (board_old[row_old][col_old] != '.') {
				board_new[row_new--][col_new] = board_old[row_old][col_old];
			}
		}
	}
	// copy back
	board_old.clear();
	for (int row = 0; row < n; row++) {
		vector<char> board_row;
		for (int col = 0; col < n; col++) {
			board_row.push_back(board_new[row][col]);
		}
		board_old.push_back(board_row);
	}
}


bool is_win_row(vector<vector<char> > &board, int n, int k, char player)
{
	//std::cout << "e" << std::endl;
	for (int row = 0; row < n; row++) {
		int streak = 0;
		for (int col = 0; col < n; col++) {
			if (board[row][col] == player) {
				if (++streak == k) {
					return true;
				}
			} else {
				streak = 0;
			}
		}
	}
	return false;
}


bool is_win_col(vector<vector<char> > &board, int n, int k, char player)
{
	//std::cout << "f" << std::endl;
	for (int col = 0; col < n; col++) {
		int streak = 0;
		for (int row = 0; row < n; row++) {
			if (board[row][col] == player) {
				if (++streak == k) {
					return true;
				}
			} else {
				streak = 0;
			}
		}
	}
	return false;
}


bool is_win_diag1(vector<vector<char> > &board, int n, int k, char player)
{
	//std::cout << "g" << std::endl;
	for (int row = 0; row < n; row++) {
		int streak = 0;
		for (int col = 0; col < n - row; col++) {
			if (board[row+col][col] == player) {
				if (++streak == k) {
					return true;
				}
			} else {
				streak = 0;
			}
		}
	}
	//std::cout << "h" << std::endl;
	for (int col = 0; col < n; col++) {
		int streak = 0;
		for (int row = 0; row < n - col; row++) {
			if (board[row][col+row] == player) {
				if (++streak == k) {
					return true;
				}
			} else {
				streak = 0;
			}
		}
	}
	return false;
}


bool is_win_diag2(vector<vector<char> > &board, int n, int k, char player)
{
	//std::cout << "i" << std::endl;
	for (int row = 0; row < n; row++) {
		int streak = 0;
		for (int col = n-1; col >= row; col--) {
			if (board[row+(n-1-col)][col] == player) {
				if (++streak == k) {
					return true;
				}
			} else {
				streak = 0;
			}
		}
	}
	//std::cout << "j" << std::endl;
	for (int col = n-1; col >= 0; col--) {
		int streak = 0;
		for (int row = 0; row <= col; row++) {
			if (board[row][col-row] == player) {
				if (++streak == k) {
					return true;
				}
			} else {
				streak = 0;
			}
		}
	}
	return false;
}


bool is_win(vector<vector<char> > &board, int n, int k, char player)
{
	return (is_win_row(board, n, k, player) || is_win_col(board, n, k, player)
		|| is_win_diag1(board, n, k, player) || is_win_diag2(board, n, k, player));
}


int solve(vector<vector<char> > &board, int n, int k)
{	
	int result = 0;
	//std::cout << "a" << std::endl;
	rotate(board, n);
	//std::cout << "b" << std::endl;
	if (is_win(board, n, k, 'R')) result += 1;
	//std::cout << "c" << std::endl;
	if (is_win(board, n, k, 'B')) result += 2;
	//std::cout << "d" << std::endl;
	return result;
}


int main()
{
	int t;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		int n, k;
		vector<vector<char> > board;
		std::cin >> n >> k;
		for (int row = 0; row < n; row++) {
			vector<char> board_row;
			for (int col = 0; col < n; col++) {
				char board_cell;
				std::cin >> board_cell;
				board_row.push_back(board_cell);
			}
			board.push_back(board_row);
		}
		std::cout << "Case #" << i+1 << ": ";
		switch (solve(board, n, k)) {
			case 0: std::cout << "Neither"; break;
			case 1: std::cout << "Red"; break;
			case 2: std::cout << "Blue"; break;
			case 3: std::cout << "Both"; break;
		}
		std::cout << std::endl;
	}
	return 0;
}
	
