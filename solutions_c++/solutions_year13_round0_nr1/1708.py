#include <iostream>
using namespace std;

const char TILE_EMPTY = '.';
const char TILE_WILDCARD = 'T';

char board[4][4];
int toCheck[][4] = {{0, 0, 0, 1}, {1, 0, 0, 1}, {2, 0, 0, 1}, {3, 0, 0, 1}, {0, 0, 1, 0}, {0, 1, 1, 0}, {0, 2, 1, 0}, {0, 3, 1, 0}, {0, 0, 1, 1}, {0, 3, 1, -1}};

inline bool areSame(char a, char b) {
	return a == b || a == TILE_WILDCARD || b == TILE_WILDCARD;
}

inline bool checkLine(int r0, int c0, int rDelta, int cDelta) {
	return board[r0][c0] != TILE_EMPTY && board[r0 + rDelta][c0 + cDelta] != TILE_EMPTY &&
			areSame(board[r0][c0], board[r0 + rDelta][c0 + cDelta]) &&
			areSame(board[r0 + rDelta][c0 + cDelta], board[r0 + 2*rDelta][c0 + 2*cDelta]) &&
			areSame(board[r0 + 2*rDelta][c0 + 2*cDelta], board[r0 + 3*rDelta][c0 + 3*cDelta]) &&
			areSame(board[r0][c0], board[r0 + 3*rDelta][c0 + 3*cDelta]);
}

inline void checkBoard(bool notCompleted) {
	for (int i = 0, len = sizeof(toCheck) / sizeof(*toCheck); i < len; i++) {
		int *next = toCheck[i];
		if (checkLine(next[0], next[1], next[2], next[3])) {
			char winner = board[next[0]][next[1]] == TILE_WILDCARD ? board[next[0] + next[2]][next[1] + next[3]] : board[next[0]][next[1]];
			
			cout << winner << " won" << endl;
			return;
		}
	}
	
	if (notCompleted) {
		cout << "Game has not completed" << endl;
	} else {
		cout << "Draw" << endl;
	}
}

int main(void) {
	int numCases;
	
	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		bool notCompleted = false;
	
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> board[i][j];
				
				if (board[i][j] == TILE_EMPTY) {
					notCompleted = true;
				}
			}
		}
		
		cout << "Case #" << numCase << ": ";
		checkBoard(notCompleted);
	}
}
