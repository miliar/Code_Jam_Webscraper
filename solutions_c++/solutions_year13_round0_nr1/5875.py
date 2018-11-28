#include <iostream>
#include <cstdio>
using namespace std;

bool canwin(char m[5][5], char who) {
    for (int i = 0; i < 4; ++i) {
        bool win = true;
        for (int j = 0; j < 4; ++j) {
            if (m[i][j] != who) {
                win = false;
                break;
            }
        }
        if (win) {
            return true;
        }
        win = true;
        for (int j = 0; j < 4; ++j) {
            if (m[j][i] != who) {
                win = false;
                break;
            }
        }
        if (win) {
            return true;
        }
    }
    bool win = true;
    for (int i = 0; i < 4; ++i) {
        if (m[i][i] != who) {
            win = false;
            break;
        }
    }
    if (win) {
        return true;
    }
    win = true;
    for (int i = 0; i < 4; ++i) {
        if (m[i][3-i] != who) {
            win = false;
            break;
        }
    }
    return win;
}

bool hasDot(char m[5][5]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (m[i][j] == '.') {
                return true;
            }
        }
    }
    return false;
}

char const * cal() {
    char m[5][5];
    int x = 4, y = 4;
    for (int i = 0; i < 4; ++i) {
        scanf("%s", m[i]);
        for (int j = 0; j < 4; ++j) {
            if (m[i][j] == 'T') {
                x = i, y = j;
            }
        }
    }

    m[x][y] = 'X';
    if (canwin(m, 'X')) {
        return "X won";
    }
    m[x][y] = 'O';
    if (canwin(m, 'O')) {
        return "O won";
    }
    if (hasDot(m)) {
        return "Game has not completed";
    }
    return "Draw";
    
}
int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: %s\n", i, cal());
    }
    return 0;
}
