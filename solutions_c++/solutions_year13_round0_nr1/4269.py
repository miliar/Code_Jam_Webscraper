#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int SIZE = 4;

string judge(const vector<string>& board) {
	int x, o, t;
	for(int i = 0; i < SIZE; ++i) {
		x = o = t = 0;
		for(int j = 0; j < SIZE; ++j) {
			switch(board[i][j]) {
			case 'X': ++x; break;
			case 'O': ++o; break;
			case 'T': ++t; break;
			}
		}
		if(x + t == SIZE)
			return "X won";
		if(o + t == SIZE)
			return "O won";
	}

	for(int j = 0; j < SIZE; ++j) {
		x = o = t = 0;
		for(int i = 0; i < SIZE; ++i) {
			switch(board[i][j]) {
			case 'X': ++x; break;
			case 'O': ++o; break;
			case 'T': ++t; break;
			}
		}
		if(x + t == SIZE)
			return "X won";
		if(o + t == SIZE)
			return "O won";
	}

	x = o = t = 0;
	for(int i = 0; i < SIZE; ++i) {
		switch(board[i][i]) {
		case 'X': ++x; break;
		case 'O': ++o; break;
		case 'T': ++t; break;
		}
	}
	if(x + t == SIZE)
		return "X won";
	if(o + t == SIZE)
		return "O won";

	x = o = t = 0;
	for(int i = 0; i < SIZE; ++i) {
		switch(board[i][SIZE - i - 1]) {
		case 'X': ++x; break;
		case 'O': ++o; break;
		case 'T': ++t; break;
		}
	}
	if(x + t == SIZE)
		return "X won";

	if(o + t == SIZE)
		return "O won";


	for(int i = 0; i < SIZE; ++i)
		for(int j = 0; j < SIZE; ++j)
			if(board[i][j] == '.')
				return "Game has not completed";

	return "Draw";
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;

	for(int test = 1; test <= t; ++test) {
		vector<string> board(SIZE);
		for(int i = 0; i < SIZE; ++i)
			cin >> board[i];

		cout << "Case #" << test << ": " << judge(board) << endl;
	}

	return EXIT_SUCCESS;
}
