#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool searchForLine(const vector<string>& board, int winSize, int x, int y, char p) {
	if(board[x][y] != p) return false;

	const int boardSize = board.size();
	int k;

	if(x + winSize - 1 < boardSize) {
		for(k = 1; k < winSize; k++)
			if(board[x + k][y] != p) break;
		if(k == winSize) return true;
	}

	if(y + winSize - 1 < boardSize) {
		for(k = 1; k < winSize; k++) {
			if(board[x][y + k] != p) break;
		}
		if(k == winSize) return true;
	}

	if((x + winSize - 1 < boardSize) && (y + winSize - 1 < boardSize)) {
		for(k = 1; k < winSize; k++) 
			if(board[x + k][y + k] != p) break;
		
		if(k == winSize) return true;
	}

	if((x - winSize + 1 >= 0) && (y + winSize - 1 < boardSize)) {
		for(k = 1; k < winSize; k++) 
			if(board[x - k][y + k] != p) break;
		
		if(k == winSize) return true;
	}

	return false;
}

string determineWinner(const vector<string>& board, int winSize) {
	const int boardSize = board.size();
	bool rWins = false, bWins = false;
	
	for(int i = 0; i < boardSize; i++) {
		for(int j = 0; j < boardSize; j++) {
			if(board[i][j] == '.') continue;
			if(!rWins) 
			       	rWins = searchForLine(board, winSize, i, j, 'R');
			if(!bWins) 
				bWins = searchForLine(board, winSize, i, j, 'B');
		}
	}

	if(rWins && bWins) {
		return "Both";
	} else if(!rWins && !bWins) {
		return "Neither";
	} else {
		return rWins ? "Red" : "Blue";
	}
}

int main() {
	int cases;
	cin >> cases;
	for(int c = 1; c <= cases; c++) {
		int boardSize, winSize;
		cin >> boardSize >> winSize;
		
		vector<string> board(boardSize);
		string inputLine;
		for(int i = 0; i < boardSize; i++) {
			do {
				getline(cin, inputLine);
			} while(inputLine.empty());
			for(int j = boardSize - 1, k = boardSize; j >= 0; j--) {
				if(inputLine[j] != '.') {
					swap(inputLine[--k], inputLine[j]);
				}
			}
			board[i] = inputLine;
			cerr << inputLine << endl;
		}

		cout << "Case #" << c << ": " << determineWinner(board, winSize) << endl;
	}
	return 0;
}
