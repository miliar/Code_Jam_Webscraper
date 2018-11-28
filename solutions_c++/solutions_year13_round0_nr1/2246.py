#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool eq(char player, char board) {
    return (player == board || board == 'T');
}

bool won(vector<string> b, char p) {
    // check diagonals
    if (eq(p, b[0][0]) && eq(p, b[1][1]) && eq(p, b[2][2]) && eq(p, b[3][3])) {
        return true;
    }
    if (eq(p, b[0][3]) && eq(p, b[1][2]) && eq(p, b[2][1]) && eq(p, b[3][0])) {
        return true;
    }
    // check cols
    for (int i = 0; i < 4; ++i) {
        if (eq(p, b[0][i]) && eq(p, b[1][i]) && eq(p, b[2][i]) && eq(p, b[3][i])) {
            return true;
        }
        if (eq(p, b[i][0]) && eq(p, b[i][1]) && eq(p, b[i][2]) && eq(p, b[i][3])) {
            return true;
        }
    }
    return false;
}

void solve(int ind) {
    // input
    string t;
    getline(cin, t);
    vector<string> board(4);
    for (int i = 0; i < 4; ++i) {
        getline(cin, board[i]);
    }
    // process
    bool hasEmpty = false;
    for (int i = 0; i < 4 && !hasEmpty; ++i) {
        for (int j = 0; j < 4 && !hasEmpty; ++j) {
            if (board[i][j] == '.') {
                hasEmpty = true;
            }
        }
    }
    bool Xwon = won(board, 'X');
    bool Owon = won(board, 'O');
//    cout << Xwon << " " << Owon << " " << hasEmpty << endl;
    string res = "?";
    if (Xwon && !Owon) {
        res = "X won";
    } else {
        if (Owon && !Xwon) {
            res = "O won";
        } else {
            if (!Owon && !Xwon && hasEmpty) {
                res = "Game has not completed";
            } else {
                res = "Draw";
            }
        }
    }
    // output
    cout << "Case #" << ind << ": " << res << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        solve(i);
    }
}