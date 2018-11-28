/*
  Google Code Jam 2013
  Problem A
  Coded by Michael Oliver
*/
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<string> vs;

int main() {
	int num_cases;
	char board[4][5];
	cin >> num_cases;
	for (int i=1; i <= num_cases; i++) {
		for (int j=0; j < 4; j++) {
			cin >> board[j];
		}
		bool x_wins = false, o_wins = false, complete = true;
		// Check rows
		for (int j=0; j < 4; j++) { // For each row
			int x_count = 0, o_count = 0, t_count = 0;
			for (int k=0; k < 4; k++) { // For each column
				if (board[j][k] == 'X') {
					x_count++;
				} else if (board[j][k] == 'O') {
					o_count++;
				} else if (board[j][k] == 'T') {
					t_count++;
				} else {
					complete = false;
				}
			}
			if (x_count == 4 || (x_count == 3 && t_count == 1)) {
				x_wins = true;
			} else if (o_count == 4 || (o_count == 3 && t_count == 1)) {
				o_wins = true;
			}
			if (x_wins || o_wins) break;
		}
		if (x_wins) {
			cout << "Case #" << i << ": X won" << endl;
			continue;
		} else if (o_wins) {
			cout << "Case #" << i << ": O won" << endl;
			continue;
		}
		
		// Check columns
		for (int j=0; j < 4; j++) { // For each column
			int x_count = 0, o_count = 0, t_count = 0;
			for (int k=0; k < 4; k++) { // For each row
				if (board[k][j] == 'X') {
					x_count++;
				} else if (board[k][j] == 'O') {
					o_count++;
				} else if (board[k][j] == 'T') {
					t_count++;
				} else {
					complete = false;
				}
			}
			if (x_count == 4 || (x_count == 3 && t_count == 1)) {
				x_wins = true;
			} else if (o_count == 4 || (o_count == 3 && t_count == 1)) {
				o_wins = true;
			}
			if (x_wins || o_wins) break;
		}
		if (x_wins) {
			cout << "Case #" << i << ": X won" << endl;
			continue;
		} else if (o_wins) {
			cout << "Case #" << i << ": O won" << endl;
			continue;
		}

		// Check diagonal lr
		int x_count = 0, o_count = 0, t_count = 0;
		for (int j=0; j < 4; j++) { // For each column/row
			if (board[j][j] == 'X') {
				x_count++;
			} else if (board[j][j] == 'O') {
				o_count++;
			} else if (board[j][j] == 'T') {
				t_count++;
			} else {
				complete = false;
			}
			if (x_wins || o_wins) break;
		}
		if (x_count == 4 || (x_count == 3 && t_count == 1)) {
			cout << "Case #" << i << ": X won" << endl;
			continue;
		} else if (o_count == 4 || (o_count == 3 && t_count == 1)) {
			cout << "Case #" << i << ": O won" << endl;
			continue;
		}
		
		// Check diagonal rl
		x_count = 0;
		o_count = 0;
		t_count = 0;
		for (int j=0; j < 4; j++) { // For each column/row
			if (board[j][3-j] == 'X') {
				x_count++;
			} else if (board[j][3-j] == 'O') {
				o_count++;
			} else if (board[j][3-j] == 'T') {
				t_count++;
			} else {
				complete = false;
			}
			if (x_wins || o_wins) break;
		}
		if (x_count == 4 || (x_count == 3 && t_count == 1)) {
			cout << "Case #" << i << ": X won" << endl;
			continue;
		} else if (o_count == 4 || (o_count == 3 && t_count == 1)) {
			cout << "Case #" << i << ": O won" << endl;
			continue;
		}
		
		if (complete) {
			cout << "Case #" << i << ": Draw" << endl;
		} else {
			cout << "Case #" << i << ": Game has not completed" << endl;
		}
	}
	return 0;
}
