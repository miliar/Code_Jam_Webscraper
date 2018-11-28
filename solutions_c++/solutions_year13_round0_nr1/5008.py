#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int BOARD_SIZE = 4;
const string X_WON = "X won";
const string Y_WON = "O won";
const string DRAW = "Draw";
const string NOT_COMPLETED = "Game has not completed";
typedef long long int ll;
typedef long double ld;

void analyze(const vector<string>& board, 
        const int i, const int j, 
        int& x, int& y, bool &finished) {
    if (board[i][j] == 'X' || board[i][j] == 'T') {
        x++;
    }
    if (board[i][j] == 'O' || board[i][j] == 'T') {
        y++;
    }
    if (board[i][j] == '.') {
        finished = false;
    }
}

string solve(const vector<string>& board) {
    bool finished = true;
    for (int i = 0; i < BOARD_SIZE; i++) {
        int x = 0;
        int y = 0;
        for (int j = 0; j < BOARD_SIZE; ++j) {
            analyze(board, i, j, x, y, finished);
        }
        if (x == BOARD_SIZE) {
            return X_WON;
        }
        if (y == BOARD_SIZE) {
            return Y_WON;
        }
    }
    for (int i = 0; i < BOARD_SIZE; i++) {
        int x = 0;
        int y = 0;
        for (int j = 0; j < BOARD_SIZE; ++j) {
            analyze(board, j, i, x, y, finished);
        }
        if (x == BOARD_SIZE) {
            return X_WON;
        }
        if (y == BOARD_SIZE) {
            return Y_WON;
        }
    }
    int x = 0;
    int y = 0;
    for (int i = 0; i < BOARD_SIZE; i++) {
        analyze(board, i, i, x, y, finished);
        if (x == BOARD_SIZE) {
            return X_WON;
        }
        if (y == BOARD_SIZE) {
            return Y_WON;
        }
    }
    x = 0;
    y = 0;
    for (int i = 0; i < BOARD_SIZE; i++) {
        analyze(board, i, BOARD_SIZE - i - 1, x, y, finished);
        if (x == BOARD_SIZE) {
            return X_WON;
        }
        if (y == BOARD_SIZE) {
            return Y_WON;
        }
    }
    if (finished) {
        return DRAW;
    }
    return NOT_COMPLETED;
}

int main() {
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        vector<string> board(BOARD_SIZE);
        for(int i = 0; i < BOARD_SIZE; ++i) {
            cin >> board[i];
        }
		cout << "Case #" << testCase << ": " << solve(board) << endl;
	}
}
