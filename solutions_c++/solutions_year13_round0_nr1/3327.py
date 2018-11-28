//
//  main.cpp
//  t1
//
//  Created by Jasper Jia on 13-4-13.
//  Copyright (c) 2013年 Jasper Jia. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[])
{
    int n;
    //int c[4][4];
    char ch;
    int markR[4];
    int markC[4];
    int markDiag[3];
    int kDiag;
    int count;
    ifstream fin("/Volumes/Documents/t1/t1/A-large.in");
    ofstream fout("/Volumes/Documents/t1/t1/A-large.out");
    fin >> n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<4; j++) markR[j] = markC[j] = 0;
        markDiag[0]=markDiag[1]=markDiag[2]=0;
        count = 0;
        for (int row=0; row<4; row++) {
            for (int col=0; col<4; col++) {
                fin>>ch;
                if(row == col) kDiag = 1;
                else if(row + col == 3) kDiag = 2;
                else kDiag = 0;
                switch (ch) {
                    case 'X':
                        markR[row] += 10;
                        markC[col] += 10;
                        markDiag[kDiag] += 10;
                        count++;
                        break;
                    case 'O':
                        markR[row] += 100;
                        markC[col] += 100;
                        markDiag[kDiag] += 100;
                        count++;
                        break;
                    case 'T':
                        markR[row] += 1;
                        markC[col] += 1;
                        markDiag[kDiag] += 1;
                        count++;
                        break;
                    default:
                        break;
                }
            }
        }
        
        int temp;
        bool unfinished = true;
        for (int row=0; row<4 && unfinished; row++) {
            temp = markR[row];
            if( temp == 31 || temp == 40) {fout<<"Case #"<<i+1<<": "<<"X won\n"; unfinished = false;}
            else if(temp == 301 || temp == 400) {fout<<"Case #"<<i+1<<": "<<"O won\n"; unfinished = false;}
        }
        for (int col=0; col<4 && unfinished; col++) {
            temp = markC[col];
            if( temp == 31 || temp == 40) {fout<<"Case #"<<i+1<<": "<<"X won\n"; unfinished = false;}
            else if(temp == 301 || temp == 400) {fout<<"Case #"<<i+1<<": "<<"O won\n"; unfinished = false;}
        }
        for (int j=1; j<=2 && unfinished; j++) {
            temp = markDiag[j];
            if( temp == 31 || temp == 40) {fout<<"Case #"<<i+1<<": "<<"X won\n"; unfinished = false;}
            else if(temp == 301 || temp == 400) {fout<<"Case #"<<i+1<<": "<<"O won\n"; unfinished = false;}
        }
        if(unfinished && count == 16) fout<<"Case #"<<i+1<<": "<<"Draw\n";
        else if(unfinished) fout<<"Case #"<<i+1<<": "<<"Game has not completed\n";
    }
    return 0;
}

