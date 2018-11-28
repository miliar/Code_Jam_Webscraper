#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <iomanip>
using namespace std;

typedef long long LL;

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

char board[4][4];
int ti, tj;

void findT() {
    ti = -1, tj = -1;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == 'T')
                ti = i, tj = j;
        }
    }
}

void changeT(char a='T') {
    if (ti != -1)
        board[ti][tj] = a;
}

bool didHeWin(char a) {
    changeT(a);
    bool ret = false;
    for (int i = 0; i < 4; i++) {
        bool present = true;
        for (int j = 0; j < 4; j++) {
            if (board[i][j] != a) present = false;
        }
        if (present) ret = true;
    }
    for (int i = 0; i < 4; i++) {
        bool present = true;
        for (int j = 0; j < 4; j++) {
            if (board[j][i] != a) present = false;
        }
        if (present) ret = true;
    }
    if (board[0][0] == a && board[1][1] == a && board[2][2] == a && board[3][3] == a) ret =  true;
    if (board[0][3] == a && board[1][2] == a && board[2][1] == a && board[3][0] == a) ret =  true;
    changeT();
    return ret;
}

bool draw() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == '.') return false;
        }
    }
    return true;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ",tt);
        for (int i = 0; i < 4; i++) {
            scanf("%s", &board[i]);
        }
        findT();
        if (didHeWin('X')) {
            printf("X won");
        } else if (didHeWin(('O'))) {
            printf("O won");
        } else if (draw()){
            printf("Draw");
        } else {
            printf("Game has not completed");
        }
        printf("\n");
    }
	return 0;
}
