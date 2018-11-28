#include <iostream>
#include <stdio.h>

using namespace std;

char b[4][5];

bool sub(char& c, bool& init, int i, int j) {
    if (init) {
        if (b[i][j] != 'T' && b[i][j] != c) {
            return false;
        }
    } else {
        if (b[i][j] != 'T') {
            c = b[i][j];
            init = true;
        }
    }
    return true;
}

char row(int i) {
    char c;
    bool init = false;
    for (int j = 0; j < 4; ++j) {
        if (b[i][j] == '.') {
            return '.';
        }
    }
    for (int j = 0; j < 4; ++j) {
        if (!sub(c, init, i, j)) {
            return '-';
        }
    }
    return c;
}

char col(int i) {
    char c;
    bool init = false;
    for (int j = 0; j < 4; ++j) {
        if (b[j][i] == '.') {
            return '.';
        }
    }
    for (int j = 0; j < 4; ++j) {
        if (!sub(c, init, j, i)) {
            return '-';
        }
    }
    return c;
}

char dia0() {
    char c;
    bool init = false;
    for (int j = 0; j < 4; ++j) {
        if (b[j][j] == '.') {
            return '.';
        }
    }
    for (int j = 0; j < 4; ++j) {
        if (!sub(c, init, j, j)) {
            return '-';
        }
    }
    return c;
}

char dia1() {
    char c;
    bool init = false;
    for (int j = 0; j < 4; ++j) {
        if (b[3 - j][j] == '.') {
            return '.';
        }
    }
    for (int j = 0; j < 4; ++j) {
        if (!sub(c, init, 3 - j, j)) {
            return '-';
        }
    }
    return c;
}

bool solve0(bool& notSolved, char c, int i) {
    if (c == 'X' || c == 'O') {
        printf("Case #%d: %c won\n", i, c);
        return true;
    }
    if (c == '.') {
        notSolved = true;
    }
    return false;
}

void solve(int j) {
    bool notSolved = false;
    char c;
    for (int i = 0; i < 4; ++i) {
        c = row(i);
        if (solve0(notSolved, c, j)) {
            return;
        }
    }
    for (int i = 0; i < 4; ++i) {
        c = col(i);
        if (solve0(notSolved, c, j)) {
            return;
        }
    }
    c = dia0();
    if (solve0(notSolved, c, j)) {
        return;
    }
    c = dia1();
    if (solve0(notSolved, c, j)) {
        return;
    }
    if (notSolved) {
        printf("Case #%d: Game has not completed\n", j);
    } else {
        printf("Case #%d: Draw\n", j);
    }
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        for (int j = 0; j < 4; ++j) {
            scanf("%s", &b[j]);
        }
        solve(i);
    }
    return 0;
}
