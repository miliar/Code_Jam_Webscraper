#include <cassert>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define RESULT_DRAW       0
#define RESULT_UNFINISHED 1
#define RESULT_X          2
#define RESULT_O          3

using namespace std;

int winner(const vector <string> &board, int i, int j, int di, int dj) {
    bool X = false;
    bool O = false;
    bool empty = false;

    while (0 <= i && i < 4 && 0 <= j && j < 4) {
        switch (board[i][j]) {
            case 'X': X = true; break;
            case 'O': O = true; break;
            case '.': empty = true; break;
            case 'T': break;
            default: assert(0);
        }
        i += di;
        j += dj;
    }

    if (empty) {
        return RESULT_UNFINISHED;
    }
    if (X == O) {
        return RESULT_DRAW;
    }
    return X ? RESULT_X : RESULT_O;
}

#define CHECK_WINNER(i, j, di, dj)                \
{                                                 \
    int temp = winner(board, i, j, di, dj);       \
    if (temp != -1) {                             \
        result = max(result, temp);               \
    }                                             \
}

int main() {
    int T = 1;
    int t;

    cin >> t;
    while (t--) {
        vector <string> board(4);
        int result = RESULT_DRAW;
        bool ended = true;

        for (int i=0; i < 4; ++i) {
            cin >> board[i];
        }

        CHECK_WINNER(0, 0, 1, 1);
        CHECK_WINNER(0, 3, 1, -1);

        for (int k=0; k < 4; ++k) {
            CHECK_WINNER(0, k, 1, 0);
            CHECK_WINNER(k, 0, 0, 1);
            for (int j=0; j < 4; ++j) {
                if (board[k][j] == '.') {
                    result = max(result, RESULT_UNFINISHED);
                }
            }
        }

        cout << "Case #" << T++ << ": ";
        switch (result) {
            case RESULT_DRAW:
                cout << "Draw";
                break;

            case RESULT_UNFINISHED:
                cout << "Game has not completed";
                break;

            case RESULT_O:
                cout << "O won";
                break;

            case RESULT_X:
                cout << "X won";
                break;

            default:
                assert(0);
                break;
        }
        cout << endl;
    }

    return 0;
}
