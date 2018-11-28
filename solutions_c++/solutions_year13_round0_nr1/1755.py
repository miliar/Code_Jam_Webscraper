#include <iostream>
#include <string>
using namespace std;

const int maxn = 4;
char mat[maxn][maxn + 1];

bool checkDiagonal1(char c) {
    int i;
    bool can;

    can = true;
    for (i = 0; i < maxn; i++) {
        can &= (mat[i][i] == c || mat[i][i] == 'T');
    }

    return can;
}

bool checkDiagonal2(char c) {
    int i;
    bool can;

    can = true;
    for (i = 0; i < maxn; i++) {
        can &= (mat[i][maxn - i - 1] == c || mat[i][maxn - i - 1] == 'T');
    }

    return can;
}

bool checkRow(int i, char c) {
    int j;
    bool can;

    can = true;
    for (j = 0; j < maxn && can; j++) {
        can &= (mat[i][j] == c || mat[i][j] == 'T');
    }

    return can;
}

bool checkCol(int j, char c) {
    int i;
    bool can;

    can = true;
    for (i = 0; i < maxn && can; i++) {
        can &= (mat[i][j] == c || mat[i][j] == 'T');
    }

    return can;
}

bool checkFinished() {
    int i, j;

    for (i = 0; i < maxn; i++) {
        for (j = 0; j < maxn; j++) {
            if (mat[i][j] == '.') {
                return false;
            }
        }
    }

    return true;
}

void print(int tt, string text) {
    cout << "Case #" << tt << ": " << text << endl;
}

void solve(int tt) {
    int i, j;

    for (i = 0; i < maxn; i++) {
        if (checkRow(i, 'X')) {
            print(tt, "X won");
            return;
        }

        if (checkRow(i, 'O')) {
            print(tt, "O won");
            return;
        }
    }

    for (j = 0; j < maxn; j++) {
        if (checkCol(j, 'X')) {
            print(tt, "X won");
            return;
        }

        if (checkCol(j, 'O')) {
            print(tt, "O won");
            return;
        }
    }

    if (checkDiagonal1('X') || checkDiagonal2('X')) {
        print(tt, "X won");
        return;
    }

    if (checkDiagonal1('O') || checkDiagonal2('O')) {
        print(tt, "O won");
        return;
    }

    if (checkFinished()) {
        print(tt, "Draw");
        return;
    }

    print(tt, "Game has not completed");
}

int main() {
    int t, tt, i;

    cin >> t;
    for (tt = 1; tt <= t; tt++) {
        for (i = 0; i < maxn; i++) {
            cin >> mat[i];
        }

        solve(tt);
    }

    return 0;
}

