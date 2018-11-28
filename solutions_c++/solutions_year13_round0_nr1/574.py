#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 8

using namespace std;

const char ans[][128] = {
    "X won",
    "O won",
    "Draw",
    "Game has not completed"
};

char mat[MAX][MAX];

bool checkRow(int k, char x) {
    int i;
    for (i = 0; i < 4; ++i) {
        if (mat[k][i] != x && mat[k][i] != 'T') return false;
    }
    return true;
}

bool checkCol(int k, int x) {
    int i;
    for (i = 0; i < 4; ++i) {
        if (mat[i][k] != x && mat[i][k] != 'T') return false;
    }
    return true;
}

bool checkDiag(int k, int x) {
    int i, j;

    if (!k) {
        for (i = j = 0; i < 4 && j < 4; ++i, ++j) {
            if (mat[i][j] != x && mat[i][j] != 'T') return false;
        }
    } else {
        for (i = 0, j = 3; i < 4 && ~j; ++i, --j) {
            if (mat[i][j] != x && mat[i][j] != 'T') return false;
        }
    }

    return true;
}

int check() {
    int i, j, cnt = 0;

    for (i = 0; i < 4; ++i) {
        if (checkRow(i, 'X')) return 0;
        if (checkCol(i, 'X')) return 0;
    }
    if (checkDiag(0, 'X') || checkDiag(1, 'X')) return 0;

    for (i = 0; i < 4; ++i) {
        if (checkRow(i, 'O')) return 1;
        if (checkCol(i, 'O')) return 1;
    }
    if (checkDiag(0, 'O') || checkDiag(1, 'O')) return 1;

    for (i = 0; i < 4; ++i) {
        for (j = 0; j < 4; ++j) {
            if (mat[i][j] != '.') ++cnt;
        }
    }

    return cnt == 16 ? 2 : 3;
}

int main() {
    int t, ct = 0, i;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        for (i = 0; i < 4; ++i) scanf("%s", mat[i]);
        printf("Case #%d: %s\n", ++ct, ans[check()]);
    }

    return 0;
}
