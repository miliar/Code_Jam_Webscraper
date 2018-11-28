#include <iostream>
#include <vector>

using namespace std;

bool print(char c)
{
    if (c == 'X') {
        cout << "X won\n";
        return true;
    } else if (c == 'O') {
        cout << "O won\n";
        return true;
    }

    return false;
}

bool check_rows(const vector<string>& board)
{
    for (int i = 0; i < 4; ++i) {
        char c = board[i][0];

        bool good = true;
        for (int j = 1; j < 4; ++j)
            if (board[i][j] != c && board[i][j] != 'T') {
                good = false;
                break;
            }

        if (good) {
            if (print(c))
                return true;
        }
    }

    return false;
}

bool check_cols(const vector<string>& board)
{
    for (int i = 0; i < 4; ++i) {
        char c = board[0][i];

        bool good = true;
        for (int j = 1; j < 4; ++j)
            if (board[j][i] != c && board[j][i] != 'T') {
                good = false;
                break;
            }

        if (good) {
            if (print(c))
                return true;
        }
    }

    return false;
}

bool check_diags(const vector<string>& board)
{
    char c = board[0][0];
    bool good = true;
    for (int i = 1; i < 4; ++i)
        if (board[i][i] != c && board[i][i] != 'T') {
            good = false;
            break;
        }

    if (good) {
        if (print(c))
            return true;
    }

    c = board[0][3];
    good = true;
    for (int i = 1; i < 4; ++i)
        if (board[i][3 - i] != c && board[i][3 - i] != 'T') {
            good = false;
            break;
        }

    if (good) {
        if (print(c))
            return true;
    }

    return false;
}

bool filled(const vector<string>& board)
{
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (board[i][j] == '.')
                return false;

    return true;
}

int main()
{
    int T;
    cin >> T;

    for (int k = 1; k <= T; ++k) {
        vector<string> board(4);

        for (int i = 0; i < 4; ++i) 
            cin >> board[i];

        cout << "Case #" << k << ": ";

        bool won = check_rows(board);
        if (!won)
            won |= check_cols(board);
        if (!won)
            won |= check_diags(board);

        if (!won) {
            if (filled(board))
                cout << "Draw\n";
            else
                cout << "Game has not completed\n";
        }
        cin.ignore();
    }

    return 0;
}
