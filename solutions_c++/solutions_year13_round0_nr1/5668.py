#include <cassert>
#include <cstdlib>

#include <iostream>
#include <fstream>

using namespace std;


enum GAME_STATE {
    O_WIN,
    X_WIN,
    INCOMPLETE,
    DRAW
};


inline GAME_STATE winType(const char token) {
    switch (token) {
        case 'O':
            return O_WIN;
            break;
        case 'X':
            return X_WIN;
            break;
        default:
            assert(false && "Unknown win");
            return DRAW;
    }
}


GAME_STATE getGameState(const char board[4][4]) {
    // Rows
    for (int i = 0; i < 4; ++i) {
        const char token = ('T' == board[i][0] ? board[i][1] : board[i][0]);
        if ('.' == token) {
            continue;
        }
        for (int j = 0; j < 4; ++j) {
            if (board[i][j] != token && 'T' != board[i][j]) {
                ++i;
                goto NEXT_ROW;
            }
        }

        return winType(token);

NEXT_ROW:;
    }

    
    // Columns
    for (int i = 0; i < 4; ++i) {
        const char token = ('T' == board[0][i] ? board[1][i] : board[0][i]);
        if ('.' == token) {
            continue;
        }
        for (int j = 0; j < 4; ++j) {
            if (board[j][i] != token && board[j][i] != 'T') {
                goto NEXT_COLUMN;
            }
        }

        return winType(token);

NEXT_COLUMN:;
    }

    // Diagonals
    {
        const char token = ('T' == board[0][0] ? board[1][1] : board[0][0]);
        if ('.' == token) {
            goto NEXT_DIAGONAL;
        }
        for (int i = 0; i < 4; ++i) {
            if (token != board[i][i] && 'T' != board[i][i]) {
                goto NEXT_DIAGONAL;
            }
        }
        return winType(token);
    }
NEXT_DIAGONAL:
    {
        const char token = ('T' == board[0][3] ? board[1][2] : board[0][3]);
        if ('.' == token) {
            goto CHECK_FOR_DRAW;
        }
        for (int i = 0; i < 4; ++i) {
            if (token != board[i][3 - i] && 'T' != board[i][3 - i]) {
                goto CHECK_FOR_DRAW;
            }
        }
        return winType(token);
    }

CHECK_FOR_DRAW:

    // Draw and incomplete
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if ('.' == board[i][j]) {
                return INCOMPLETE;
            }
        }
    }

    return DRAW;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <input>" << endl;
        exit(EXIT_FAILURE);
    }
    ifstream fin(argv[1]);
    if (!fin) {
        cerr << "Unable to open file " << argv[1] << endl;
        exit(EXIT_FAILURE);
    }

    istream& in = fin;
    ostream& out = cout;

    int inputSize;
    in >> inputSize;


    char board[4][4];

    for (int i = 0; i < inputSize; ++i) {
        out << "Case #" << i + 1 << ": ";

        for (int j = 0; j < 4; ++j) {
            for (int k = 0; k < 4; ++k) {
                in >> board[j][k];
            }
        }

        switch (getGameState(board)) {
            case O_WIN:
                cout << "O won" << endl;
                break;
            case X_WIN:
                cout << "X won" << endl;
                break;
            case INCOMPLETE:
                cout << "Game has not completed" << endl;
                break;
            case DRAW:
                cout << "Draw" << endl;
                break;
            default:
                assert(false && "Unexpected case");
                break;
        }
    }
    exit(EXIT_SUCCESS);
}
