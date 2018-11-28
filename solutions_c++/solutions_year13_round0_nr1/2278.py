#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int check_win(char board[10][10], char player) {
    // check horizontal
    for (int i = 0; i < 4; ++i) {
        bool ok = true;
        for (int j = 0; j < 4; ++j) {
            ok = ok && (board[i][j] == player || board[i][j] == 'T');
        }
        if (ok) {
            return true;
        }
    }
    // check vertical
    for (int j = 0; j < 4; ++j) {
        bool ok = true;
        for (int i = 0; i < 4; ++i) {
            ok = ok && (board[i][j] == player || board[i][j] == 'T');
        }
        if (ok) {
            return true;
        }
    }
    // check diagonal
    bool ok1 = true, ok2 = true;
    for (int i = 0; i < 4; ++i) {
        ok1 = ok1 && (board[i][i] == player || board[i][i] == 'T');
        ok2 = ok2 && (board[i][3-i] == player || board[i][3-i] == 'T');
    }
    return ok1 || ok2;
}

int main() {
    char board[10][10];
    int tests;

    scanf("%d", &tests);
    for (int test = 0; test < tests; ++test) {
        for (int i = 0; i < 4; ++i) {
            scanf("%s", board[i]);
        }
        bool has_empty = false;
        for (int i = 0; i < 4; ++i) {
            if (strchr(board[i], '.')) {
                has_empty = true;
                break;
            }
        }
        int x_win = check_win(board, 'X');
        int y_win = check_win(board, 'O');

        printf("Case #%d: ", test + 1);
        if (x_win) {
            printf("X won\n");
        } else if (y_win) {
            printf("O won\n");
        } else if (has_empty) {
            printf("Game has not completed\n");
        } else {
            printf("Draw\n");
        }
    }
    return 0;
}

