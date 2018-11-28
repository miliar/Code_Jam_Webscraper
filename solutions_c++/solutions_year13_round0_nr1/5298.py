#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	int N, M;
	cin >> T;
	int t = 1;
	while (t <= T){
		N = M = 4;
		vector<vector<char> > board(N, vector<char> (M));
		int dots = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				cin >> board[i][j];
				if (board[i][j] == '.') dots++;
			}
		}
		bool sol = false;
		char wins;
		for (int i = 0; i < N and not sol; ++i) {
			wins = board[i][0];
			for (int j = 1; j < M and wins != '.'; ++j) {
				if (wins == 'T') wins = board[i][j];
				else if (board[i][j] == '.') wins = '.';
				else if (board[i][j] != 'T' and wins != board[i][j]) wins = '.';
			}
			if (wins == 'X' or wins == 'O') sol = true;			
		}
		
		for (int i = 0; i < M and not sol; ++i) {
			wins = board[0][i];
			for (int j = 1; j < N and wins != '.'; ++j) {
				if (wins == 'T') wins = board[j][i];
				else if (board[j][i] == '.') wins = '.';
				else if (board[j][i] != 'T' and wins != board[j][i]) wins = '.';
			}
			if (wins == 'X' or wins == 'O') sol = true;			
		}
		
		if (not sol) {
			wins = board[0][0];
			for (int i = 1; i < N and not sol; ++i) {
				if (wins == 'T') wins = board[i][i];
				else if (board[i][i] == '.') wins = '.';
				else if (board[i][i] != 'T' and wins != board[i][i]) wins = '.';
				
			}
			if (wins == 'X' or wins == 'O') sol = true;	
		}
		if (not sol) {
			wins = board[N-1][0];
			for (int i = 1; i < N and not sol; ++i) {
				if (wins == 'T') wins = board[N-i-1][i];
				else if (board[N-i-1][i] == '.') wins = '.';
				else if (board[N-i-1][i] != 'T' and wins != board[N-i-1][i]) wins = '.';
				
			}
			if (wins == 'X' or wins == 'O') sol = true;	
		}
		

		cout << "Case #" << t << ": " ;
		if (sol) cout << wins << " won" << endl;
		else if (dots == 0) cout << "Draw" << endl;
		else cout << "Game has not completed" << endl;

		t++;
	}
    return 0;
}

