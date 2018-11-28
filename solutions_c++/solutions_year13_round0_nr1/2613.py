/**
 * Jerry Ma
 * D.cpp
 */

#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;

int gInt () {
    int i;
    scanf("%d", &i);
    return i;
}

lli gLong () {
    lli i;
    scanf("%lld", &i);
    return i;
}

double gDouble () {
    double i;
    scanf("%lf", &i);
    return i;
}

void quit () {
    fflush(stdout);
    exit(0);
}

char board[6][6];

bool goodArr (char * chars, char a) {
    for (int i = 0; i < 4; i ++) {
        if (chars[i] != a && chars[i] != 'T')
            return false;
    }
    return true;
}

bool good (int y1, int x1, int y2, int x2, int y3, int x3, int y4, int x4, char a) {
    char chars[4] = {board[y1][x1], board[y2][x2], board[y3][x3], board[y4][x4]};
    return goodArr(chars, a);
}

#define xwon printf("X won\n"); return

#define owon printf("O won\n"); return

#define draw printf("Draw\n"); return

#define nc printf("Game has not completed\n"); return

void solve (int nC) {
    printf("Case #%d: ", nC);
    int filled = 0;
    for (int i = 0; i < 4; i ++) {
        scanf("%s", board[i]);
        for (int j = 0; j < 4; j ++)
            filled += (board[i][j] == '.' ? 0 : 1);
    }
    if (good(0, 0, 1, 1, 2, 2, 3, 3, 'X') || good(0, 3, 1, 2, 2, 1, 3, 0, 'X')) {
        xwon;
    }
        if (good(0, 0, 1, 1, 2, 2, 3, 3, 'O') || good(0, 3, 1, 2, 2, 1, 3, 0, 'O')) {
        owon;
    }
    for (int i = 0; i < 4; i ++) {
        if (good(i, 0, i, 1, i, 2, i, 3, 'X') || good(0, i, 1, i, 2, i, 3, i, 'X')) {
            xwon;
        }
        if (good(i, 0, i, 1, i, 2, i, 3, 'O') || good(0, i, 1, i, 2, i, 3, i, 'O')) {
            owon;
        }
    }
            if (filled == 16) {
        draw;
            }
    nc;
}

int main (int argc, char ** argv) {
    int nC = gInt();
    for (int i = 0; i < nC; i ++)
        solve(i + 1);
    quit();
}