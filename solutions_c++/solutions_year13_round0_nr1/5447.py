#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

const int N = 4;

int func(vector<vector<char> > &board) {
	int res = 3;
	for (int i = 0; i < N; i++) {
		int cnt = 1;
		char c = 0;
		for (int j = 0; j < N; j++) {
			if ('.' == board[i][j]) {
				res = 4;
				break;	
			}
			if (j > 0 && (board[i][j] == board[i][j-1] || 'T' == board[i][j])) {
				cnt++;
				if (board[i][j] != 'T') {
					c = board[i][j];
				}
			}
		}
		if (cnt == 4) {
			if ('X' == c) {
				return 1;
			}else if ('O' == c) {
				return 2;	
			}
		}
	}

	for (int i = 0; i < N; i++) {
		int cnt = 1;
		char c = 0;
		for (int j = 0; j < N; j++) {
			if ('.' == board[j][i]) {
				res = 4;
				break;	
			}
			if (j > 0 && (board[j][i] == board[j-1][i] || 'T' == board[j][i])) {
				cnt++;
				if (board[j][i] != 'T') {
					c = board[j][i];
				}
			}
		}
		if (cnt == 4) {
			if ('X' == c) {
				return 1;
			}else if ('O' == c) {
				return 2;	
			}
		}
	}	

	int cnt = 1;
	char c = 0;
	for (int i = 0; i < N; i++) {
		if ('.' == board[i][i]) {
			res = 4;
			break;	
		}
		if (i > 0 && (board[i][i] == board[i-1][i-1] || 'T' == board[i][i])) {
			cnt++;
			if (board[i][i] != 'T') {
				c = board[i][i];
			}
		}
	}
	if (cnt == 4) {
		if ('X' == c) {
			return 1;
		}else if ('O' == c) {
			return 2;	
		}
	}
	
	cnt = 1;
	c = 0;
	for (int i = 0; i < N; i++) {
		if ('.' == board[i][N-1-i]) {
			break;	
		}
		if (i > 0 && (board[i][N-1-i] == board[i-1][N-i] || 'T' == board[i][N-1-i])) {
			cnt++;
			if (board[i][N-1-i] != 'T') {
				c = board[i][N-1-i];
			}
		}
	}
	if (cnt == 4) {
		if ('X' == c) {
			return 1;
		}else if ('O' == c) {
			return 2;	
		}
	}				
	return res;						
}

void solve() {
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");
	int T = 0;
	in >> T;
	
	for (int t = 1; t <= T; t++) {
		vector<vector<char> > board(N, vector<char>(N));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				in >> board[i][j];
			}
		}		
		int res = func(board);
		out << "Case #" << t << ": ";
		switch (res) {
			case 1: 
				out << "X won" << endl;
				break;
			case 2:
				out << "O won" << endl;
				break;
			case 3:
				out << "Draw" << endl;
				break;
			case 4:
				out << "Game has not completed" << endl;
				break;
			default:
				break;
		}
	}
	
	in.close();
	out.close();		
}

int main() {
	solve();	
	return 0;	
}
