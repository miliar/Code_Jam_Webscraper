#include <iostream>

void display(char board[4][4]);
char check_horizontal(char board[4][4]);
char check_vertical(char board[4][4]);
char check_diagonal(char board[4][4]);
char check_cross_diagonal(char board[4][4]);

using namespace std;

int main() {
    int T;
    cin >> T;
    char dummy[6];
    gets(dummy);
    for (int t = 0; t < T; t++) {
	
        cout << "Case #" << (t+1) << ":";
        char board[4][4];
        memset(board, '.', 4*4*sizeof(char));

		for (int i = 0; i < 4; i++) {
			gets(dummy);
			for (int j = 0; j < 4;j++) {
				board[i][j] = dummy[j];
			}
		}
		gets(dummy);
		
        char h = check_horizontal(board);
        if ('X' == h) { cout << " X won" << endl; continue; }
        if ('O' == h) { cout << " O won" << endl; continue; }

        char v = check_vertical(board);
        if ('X' == v) { cout << " X won" << endl; continue; }
        if ('O' == v) { cout << " O won" << endl; continue; }

        char d = check_diagonal(board);
        if ('X' == d) { cout << " X won" << endl; continue; }
        if ('O' == d) { cout << " O won" << endl; continue; }

        char c = check_cross_diagonal(board);
        if ('X' == c) { cout << " X won" << endl; continue; }
        if ('O' == c) { cout << " O won" << endl; continue; }

		void* dot = memchr(board, '.',  4*4*sizeof(char));
		if (NULL == dot) 
			cout << " Draw" << endl;
		else
			cout << " Game has not completed" << endl;
	}
}

void display(char board[4][4]) {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4;j++) {
			cout << board[i][j];
		}
		cout << endl;
	}
}

char check_horizontal(char board[4][4]) {
	for (int i = 0; i < 4; i++) {
		bool x_won = true;
		bool o_won = true;
		for (int j = 0; j < 4;j++) {
			if ('X' == board[i][j] || 'T' == board[i][j]) {
			} else x_won = false;
			if ('O' == board[i][j] || 'T' == board[i][j]) {
			} else o_won = false;
		}
		if (x_won) return 'X';
		if (o_won) return 'O';
	}
	return '.';
}

char check_vertical(char board[4][4]) {
	for (int j = 0; j < 4; j++) {
		bool x_won = true;
		bool o_won = true;
		for (int i = 0; i < 4;i++) {
			if ('X' == board[i][j] || 'T' == board[i][j]) {
			} else x_won = false;
			if ('O' == board[i][j] || 'T' == board[i][j]) {
			} else o_won = false;
		}
		if (x_won) return 'X';
		if (o_won) return 'O';
	}
	return '.';
}

char check_diagonal(char board[4][4]) {
	bool x_won = true;
	bool o_won = true;
	for (int i = 0; i < 4; i++) {
		if ('X' == board[i][i] || 'T' == board[i][i]) {
		} else x_won = false;
		if ('O' == board[i][i] || 'T' == board[i][i]) {
		} else o_won = false;
	}
	if (x_won) return 'X';
	if (o_won) return 'O';
	return '.';
}

char check_cross_diagonal(char board[4][4]) {
	bool x_won = true;
	bool o_won = true;
	for (int i = 0; i < 4; i++) {
		if ('X' == board[i][3-i] || 'T' == board[i][3-i]) {
		} else x_won = false;
		if ('O' == board[i][3-i] || 'T' == board[i][3-i]) {
		} else o_won = false;
	}
	if (x_won) return 'X';
	if (o_won) return 'O';
	return '.';
}
