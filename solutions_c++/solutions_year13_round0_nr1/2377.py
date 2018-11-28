//
//  main.cpp
//  tictac
//
//  Created by John Scholes on 13/04/2013.
//  Copyright (c) 2013 John Scholes. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[])
{
    int N; cin >> N;
    for(int N1=1; N1<=N; N1++) {
        int row, col, Xwin, Owin, dots, i, j;
        char c[4][4];
        Xwin=0; Owin=0; dots=0;
        for(row=0; row<4; row++)
            for(col=0; col<4; col++)
                cin >> c[row][col];
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                if(c[i][j]=='.') dots=1;
        for(i=0; i<4; i++) {
            if((c[i][0]=='X' || c[i][0]=='T') &&
               (c[i][1]=='X' || c[i][1]=='T') &&
               (c[i][2]=='X' || c[i][2]=='T') &&
               (c[i][3]=='X' || c[i][3]=='T')) {
                Xwin=1;
                break;
            }
            if((c[0][i]=='X' || c[0][i]=='T') &&
               (c[1][i]=='X' || c[1][i]=='T') &&
               (c[2][i]=='X' || c[2][i]=='T') &&
               (c[3][i]=='X' || c[3][i]=='T')) {
                Xwin=1;
                break;
            }
            if((c[i][0]=='O' || c[i][0]=='T') &&
               (c[i][1]=='O' || c[i][1]=='T') &&
               (c[i][2]=='O' || c[i][2]=='T') &&
               (c[i][3]=='O' || c[i][3]=='T')) {
                Owin=1;
                break;
            }
            if((c[0][i]=='O' || c[0][i]=='T') &&
               (c[1][i]=='O' || c[1][i]=='T') &&
               (c[2][i]=='O' || c[2][i]=='T') &&
               (c[3][i]=='O' || c[3][i]=='T')) {
                Owin=1;
                break;
            }
        }
        if((c[0][0]=='X' || c[0][0]=='T') &&
           (c[1][1]=='X' || c[1][1]=='T') &&
           (c[2][2]=='X' || c[2][2]=='T') &&
           (c[3][3]=='X' || c[3][3]=='T')) Xwin=1;
        if((c[0][0]=='O' || c[0][0]=='T') &&
           (c[1][1]=='O' || c[1][1]=='T') &&
           (c[2][2]=='O' || c[2][2]=='T') &&
           (c[3][3]=='O' || c[3][3]=='T')) Owin=1;
        if((c[0][3]=='X' || c[0][3]=='T') &&
           (c[1][2]=='X' || c[1][2]=='T') &&
           (c[2][1]=='X' || c[2][1]=='T') &&
           (c[3][0]=='X' || c[3][0]=='T')) Xwin=1;
        if((c[0][3]=='O' || c[0][3]=='T') &&
           (c[1][2]=='O' || c[1][2]=='T') &&
           (c[2][1]=='O' || c[2][1]=='T') &&
           (c[3][0]=='O' || c[3][0]=='T')) Owin=1;
        cout << "Case #" << N1 << ": ";
        if(Xwin) cout << "X won\n";
        else if (Owin) cout << "O won\n";
        else if (dots==0) cout << "Draw\n";
        else cout << "Game has not completed\n";
    }
    return 0;
}

