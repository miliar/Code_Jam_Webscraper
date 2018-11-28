#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

string board[4];

bool isMyCell(int r, int c, char player) {
    return board[r][c] == player || board[r][c] == 'T';
}

bool checkForWin(char player) {
    bool flag;

    for (int i = 0; i < 4; i++) {
        flag = true;
        for (int j = 0; j < 4; j++) {
            if (!isMyCell(i, j, player)) {
                flag = false;
            }
        }

        if (flag) {
            return true;
        }
    }

    for (int j = 0; j < 4; j++) {
        flag = true;
        for (int i = 0; i < 4; i++) {
            if (!isMyCell(i, j, player)) {
                flag = false;
            }
        }

        if (flag) {
            return true;
        }
    }

    flag = true;
    for (int i = 0; i < 4; i++) {
        if (!isMyCell(i, i, player)) {
            flag = false;
        }
    }

    if (flag) {
        return true;
    }

    flag = true;
    for (int i = 0; i < 4; i++) {
        if (!isMyCell(i, 3 - i, player)) {
            flag = false;
        }
    }

    if (flag) {
        return true;
    }

    return false;
}

bool isStillInProgress() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == '.') {
                return true;
            }
        }
    }

    return false;
}

string solve() {
    for (int i = 0; i < 4; i++) {
        cin >> board[i];
    }

    if (checkForWin('X')) {
        return "X won";
    }

    if (checkForWin('O')) {
        return "O won";
    }

    if (isStillInProgress()) {
        return "Game has not completed";
    }

    return "Draw";
}

int main() {
    int tests;
    cin >> tests;

    for (int i = 1; i <= tests; i++) {
        cout << "Case #" << i << ": " << solve() << endl;
    }

    return 0;
}

