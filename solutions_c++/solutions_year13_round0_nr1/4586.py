# include <cstdio>
# include <iostream>

# define X_WON "X won"
# define O_WON "O won"
# define DRAW "Draw"
# define NOT_OVER "Game has not completed"

const int MAXDIM = 4;

int T;
char board[MAXDIM + 1][MAXDIM];

bool has_won(char c, char joker) {
    for (int i = 0; i < MAXDIM; ++i) {
        bool winning_row = true;
        for (int j = 0; j < MAXDIM; ++j) {
            if (board[i][j] != c && board[i][j] != joker) {
                winning_row = false;
            }
        }
        if (winning_row) return true;
    }

    for (int i = 0; i < MAXDIM; ++i) {
        bool winning_column = true;
        for (int j = 0; j < MAXDIM; ++j) {
            if (board[j][i] != c && board[j][i] != joker) {
                winning_column = false;
            }
        }
        if (winning_column) return true;
    }


    {
        bool winning_diag = true;
        for (int i = 0; i < MAXDIM; ++i) {
            if (board[i][i] != c && board[i][i] != joker) {
                winning_diag = false;
            }
        }
        if (winning_diag) return true;
    }

    {
        bool winning_diag = true;
        for (int i = 0; i < MAXDIM; ++i) {
            if (board[MAXDIM - i - 1][i] != c && board[MAXDIM - i - 1][i] != joker) {
                winning_diag = false;
            }
        }
        if (winning_diag) return true;
    }

    return false;
}

std::string solve() {
    bool x_won = false, o_won = false, finished = true;

    x_won = has_won('X', 'T');
    o_won = has_won('O', 'T');
    for (int i = 0; i < MAXDIM; ++i) {
        for (int j = 0; j < MAXDIM; ++j) {
            if (board[i][j] == '.') finished = false;
        }
    }

    if (finished || x_won || o_won) {
        if (x_won) return X_WON;
        if (o_won) return O_WON;
        return DRAW;
    } else {
        return NOT_OVER;
    }
}

int main(void) {
    std::cin >> T;

    int t = 1;
    while (T--) {
        for (int i = 0; i < MAXDIM; ++i)
            std::cin >> board[i];

        std::cout << "Case #" << t++ << ": " << solve() << std::endl;
    }

    return 0;
}
