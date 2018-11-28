/* 
 * File:   main.cpp
 * Author: Yiting
 *
 * Created on April 13, 2013, 8:52 AM
 */

#include <cstdlib>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;
int n;
char board[4][5];

char checkWin() {
    int i, j;
    char tmp;
    //check each row
    for (i = 0; i < 4; i++) {
        tmp = board[i][0];
        if (tmp == 'T') tmp = board[i][1];
        int row = 0;
        for (j = 0; j < 4; j++) {
            if (tmp == '.') break;
            if (board[i][j] == tmp || board[i][j] == 'T')
                row++;
        }
        if (row == 4) return tmp;
    }
    //check column
    for (j = 0; j < 4; j++) {
        tmp = board[0][j];
        if (tmp == 'T') tmp = board[1][j];
        int column = 0;
        for (i = 0; i < 4; i++) {
            if (tmp == '.') break;
            if (board[i][j] == tmp || board[i][j] == 'T')
                column++;
        }
        if (column == 4) return tmp;
    }
    //check diagonal 1
    tmp = board[0][0];
    if (tmp == 'T') tmp = board[1][1];
    int diagonal = 0;
    for (i = 1; i < 4; i++) {
        if (tmp == '.') goto next;
        if (board[i][i] == tmp || board[i][i] == 'T')
            diagonal++;
    }
    if (diagonal == 3) return tmp;
    //check diagonal 2
next:
    tmp = board[0][3];
    if (tmp == 'T') tmp = board[1][2];
    if ((board[1][2] == tmp || board[1][2] == 'T') &&
            (board[2][1] == tmp || board[2][1] == 'T') &&
            (board[3][0] == tmp || board[3][0] == 'T'))
        return tmp;

    return 'N';
}

bool checkfull() {
    int i, j;
    for (i = 0; i < 4; i++)
        for (j = 0; j < 4; j++)
            if (board[i][j] == '.')
                return false;
    return true;
}

int solve() {
    char r = checkWin();
    if (r == 'X') return 1;
    if (r == 'O') return 2;
    if (checkfull()) {
        return 3;
    }
    return 4;
}

void output() {
    int i, j;
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++)
            printf("%c", board[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    int i, c;
    FILE *fin = fopen("test.in", "rb");
    FILE *fout = fopen("test.out", "wb");
    fscanf(fin, "%d", &n);
    for (c = 1; c <= n; c++) {
        for (i = 0; i < 4; i++) {
            fscanf(fin, "%s", board[i]);
        }
        int s = solve();
        if (s == 1)
            fprintf(fout, "Case #%d: X won\n", c);
        if (s == 2)
            fprintf(fout, "Case #%d: O won\n", c);
        if (s == 3)
            fprintf(fout, "Case #%d: Draw\n", c);
        if (s == 4)
            fprintf(fout, "Case #%d: Game has not completed\n", c);
    }
    return 0;
}

