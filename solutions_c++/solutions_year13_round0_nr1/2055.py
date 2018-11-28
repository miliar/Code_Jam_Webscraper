#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

bool isTurnLeft(char game[4][5]) {
    for (int i = 0;i < 4; i++) {
        for (int j = 0;j < 4; j++) {
            if (game[i][j] == '.')
                return true;
        }
    }
    return false;
}

bool isStrike(char game[4][5], int x, int y, int xInc, int yInc, char token) {
    for (int i = 0; i < 4; i++) {
        if (!(game[x][y] == token || game[x][y] == 'T')) {
            return false;
        }
        x += xInc;
        y += yInc;
    }
    return true;
}

int main () {
    int t, i, testcase = 1;
    char game[4][5];
    scanf("%d", &t);
    while (testcase <= t) {
        printf("Case #%d: ", testcase++);
        rep(i,4) {
            scanf(" %s", game[i]);
        }
        if (isStrike(game, 0, 0, 0, 1, 'X') || isStrike(game, 1, 0, 0, 1, 'X') || isStrike(game, 2, 0, 0, 1, 'X') || isStrike(game, 3, 0, 0, 1, 'X') || 
                isStrike(game, 0, 0, 1, 0, 'X') || isStrike(game, 0, 1, 1, 0, 'X') || isStrike(game, 0, 2, 1, 0, 'X') || isStrike(game, 0, 3, 1, 0, 'X') || 
                isStrike(game, 0, 0, 1, 1, 'X') || isStrike(game, 0, 3, 1, -1, 'X')) {
            printf("X won\n");
        } else if (isStrike(game, 0, 0, 0, 1, 'O') || isStrike(game, 1, 0, 0, 1, 'O') || isStrike(game, 2, 0, 0, 1, 'O') || isStrike(game, 3, 0, 0, 1, 'O') || 
                isStrike(game, 0, 0, 1, 0, 'O') || isStrike(game, 0, 1, 1, 0, 'O') || isStrike(game, 0, 2, 1, 0, 'O') || isStrike(game, 0, 3, 1, 0, 'O') || 
                isStrike(game, 0, 0, 1, 1, 'O') || isStrike(game, 0, 3, 1, -1, 'O')) {
            printf("O won\n");
        } else if (isTurnLeft(game)) {
            printf("Game has not completed\n");
        } else {
            printf("Draw\n");
        }
    }
    return 0;
}
