#include<iostream>

using namespace std;

char board[4][4];

bool check(char c) {
    bool diag1 = true;
    bool diag2 = true;
    for (int i = 0; i < 4; ++i) {
        if (board[i][i] != 'T' && board[i][i] != c) diag1 = false;
        if (board[3-i][i] != 'T' && board[3-i][i] != c) diag2 = false;
        bool row = true;
        bool col = true;
        for (int j = 0; j < 4; ++j) {
            if (board[i][j] != 'T' && board[i][j] != c) row = false;
            if (board[j][i] != 'T' && board[j][i] != c) col = false;
        }
        /*if (row) cout << c << " won on row " << i << endl;
        else if (col) cout << c << " won on col " << i << endl;*/
        if (row || col) return true;
    }
    /*if (diag1) cout << c << " won on positive diagonal" << endl;
    else if (diag2) cout << c << " won on negative diagonal" << endl;*/
    return diag1 || diag2;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int dots = 0;
        cout << "Case #" << t+1 << ": ";
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> board[i][j];
                if (board[i][j] == '.') ++dots;
            }
        }
        if (check('X')) cout << "X won";
        else if (check('O')) cout << "O won";
        else if (dots) cout << "Game has not completed";
        else cout << "Draw";
        cout << endl;
    }
}
