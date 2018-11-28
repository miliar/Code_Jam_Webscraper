//
//  main.cpp
//  GCJ2013
//
//  Created by wang yan hao on 13-4-13.
//  Copyright (c) 2013年 wang yan hao. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

ifstream in("/Users/wangyanhao/Documents/XcodeProjects/GCJ2013/A-large.in.txt");
ofstream out("/Users/wangyanhao/Documents/XcodeProjects/GCJ2013/A-large.out.txt");

//#define in cin
//#define out cout


int T;
char board[5][5];

int main()
{
    in >> T;
    for (int count = 1; count <= T; count++) {
        bool Xwin = false, Ywin = false, hasEmpty = false;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                in >> board[i][j];
                if (board[i][j] == '.')
                    hasEmpty = true;
            }
        }
        //test win
        for (int i = 0; i < 4; i++) {
            int Xnum = 0, Ynum = 0;
            for (int j = 0; j < 4; j++) {
                if (board[i][j] == 'X' || board[i][j] == 'T')
                    Xnum++;
                if (board[i][j] == 'O' || board[i][j] == 'T')
                    Ynum++;
            }
            if (Xnum == 4) {
                Xwin = true;
                break;
            }
            if (Ynum == 4) {
                Ywin = true;
                break;
            }
            Xnum = 0, Ynum = 0;
            for (int j = 0; j < 4; j++) {
                if (board[j][i] == 'X' || board[j][i] == 'T')
                    Xnum++;
                if (board[j][i] == 'O' || board[j][i] == 'T') {
                    Ynum++;
                }
            }
            if (Xnum == 4) {
                Xwin = true;
                break;
            }
            if (Ynum == 4) {
                Ywin = true;
                break;
            }
            
        }
        int Xnum = 0, Ynum = 0;
        for (int i = 0; i < 4; i++) {
            if (board[i][i] == 'X' || board[i][i] == 'T') {
                Xnum++;
            }
            if (board[i][i] == 'O' || board[i][i] == 'T') {
                Ynum++;
            }
        }
        if (Xnum == 4) {
            Xwin = true;
        }
        if (Ynum == 4) {
            Ywin = true;
        }
        Xnum = 0, Ynum = 0;
        for (int i = 0; i < 4; i++) {
            if (board[i][3-i] == 'X' || board[i][3-i] == 'T') {
                Xnum++;
            }
            if (board[i][3-i] == 'O' || board[i][3-i] == 'T') {
                Ynum++;
            }
        }
        if (Xnum == 4) {
            Xwin = true;
        }
        if (Ynum == 4) {
            Ywin = true;
        }
        out << "Case #" << count << ": ";
        if (Xwin) {
            out << "X won" << endl;
        } else if (Ywin) {
            out << "O won" << endl;
        } else if (hasEmpty) {
            out << "Game has not completed" << endl;
        } else {
            out << "Draw" << endl;
        }
    }
    out.close();
    return 0;
}

