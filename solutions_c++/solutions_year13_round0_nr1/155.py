#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int SIZE = 4;
const char WILDCARD = 'T';

bool isFull(const vector<string>& board) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == '.') {
                return false;
            }
        }
    }
    return true;
}

bool isWinner(const vector<string>& board, char player) {
    for (int i = 0; i < SIZE; i++) {
        bool win = true;
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] != player && board[i][j] != WILDCARD) {
                win = false;
                break;
            }
        }
        if (win) {
            return true;
        }
    }
    for (int i = 0; i < SIZE; i++) {
        bool win = true;
        for (int j = 0; j < SIZE; j++) {
            if (board[j][i] != player && board[j][i] != WILDCARD) {
                win = false;
                break;
            }
        }
        if (win) {
            return true;
        }
    }
    bool win;
    win = true;
    for (int i = 0; i < SIZE; i++) {
        if (board[i][i] != player && board[i][i] != WILDCARD) {
            win = false;
            break;
        }
    }
    if (win) {
        return true;
    }
    win = true;
    for (int i = 0; i < SIZE; i++) {
        if (board[i][SIZE-1-i] != player && board[i][SIZE-1-i] != WILDCARD) {
            win = false;
            break;
        }
    }
    if (win) {
        return true;
    }
    return false;
}

int main() {

    int tc;

    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        vector<string> board(SIZE);
        for (int i = 0; i < SIZE; i++) {
            cin >> board[i];
        }
        cout << "Case #" << t << ": ";
        if (isWinner(board, 'X')) {
            cout << "X won";
        } else if (isWinner(board, 'O')) {
            cout << "O won";
        } else if (isFull(board)) {
            cout << "Draw";
        } else {
            cout << "Game has not completed";
        }
        cout << endl;
    }

    return 0;
}

