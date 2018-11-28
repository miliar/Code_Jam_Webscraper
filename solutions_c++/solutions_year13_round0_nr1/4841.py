
// qualA.cpp

#include <iostream>
#include <string>
using namespace std;

bool check(string board[], char player)
{
    bool win;

    // row
    for (int i = 0; i < 4; ++i) {
        win = true;
        for (int j = 0; j < 4; ++j) {
            if (board[i][j] != 'T' && board[i][j] != player)
                { win = false; }
        }
        if (win) return true;
    }
    // col
    for (int j = 0; j < 4; ++j) {
        win = true;
        for (int i = 0; i < 4; ++i) {
            if (board[i][j] != 'T' && board[i][j] != player)
                { win = false; }
        }
        if (win) return true;
    }
    // major diag
    win = true;
    for (int r=0, c=0; r < 4; ++r, ++c) {
        if (board[r][c] != 'T' && board[r][c] != player) {
            win = false;
        }
    }
    if (win) return true;
    // minor diag
    win = true;
    for (int r=0, c=3; r < 4; ++r, --c) {
        if (board[r][c] != 'T' && board[r][c] != player) {
            win = false;
        }
    }
    if (win) return true;

    return false;
}

void solve(int tcase)
{
    cout << "Case #" << tcase << ": ";
    string board[4];
    for (int i = 0; i < 4; ++i) {
        cin >> board[i];
    }
    bool Xwin, Owin;
    Xwin = check(board, 'X');
    Owin = check(board, 'O');
    if (Xwin) { cout << "X won" << endl; return; }
    if (Owin) { cout << "O won" << endl; return; }

    bool done = true;
    for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; ++j)
        if (board[i][j] == '.')
            done = false;
    if (done) cout << "Draw" << endl;
    else cout << "Game has not completed" << endl;
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; ++t)
        solve(t);
}
