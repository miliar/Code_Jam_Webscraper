//
//  codejamA.cpp
//  trycpp
//
//  Created by Tarun Goyal on 13/04/13.
//  Copyright (c) 2013 Tarun Goyal. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int main()
{
    FILE *fin = fopen("codejamAinput.txt", "r");
    FILE *fout = fopen("codejamAoutput.txt", "w");
    int t;
    fscanf(fin,"%d",&t);
    for (int I=1; I<=t; I++) {
        char **s = new char*[4];
        int **x = new int*[4];
        bool isComplete = true;
        for (int j=0; j<4; j++) {
            s[j] = new char[6];
            fscanf(fin,"%s",s[j]);
            x[j] = new int[6];
        }
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                if(s[i][j]=='.') {x[i][j] = 0; isComplete = false;}
                else if(s[i][j]=='T') x[i][j] = 3;
                else if(s[i][j]=='X') x[i][j] = 1;
                else if(s[i][j]=='O') x[i][j] = 2;
            }
        }
        int won = 0;
        for (int i=0; i<4; i++) {
            int chk = 3;
            for(int j=0;j<4;j++)
            {
                chk&=x[i][j];
            }
            if (chk) {
                won = chk;
                break;
            }
        }
        if (won) {
            if (won==1) {
                fprintf(fout,"Case #%d: X won\n",I);
            }
            else
            {
                fprintf(fout,"Case #%d: O won\n",I);
            }
            continue;
        }
        for (int i=0; i<4; i++) {
            int chk = 3;
            for(int j=0;j<4;j++)
            {
                chk&=x[j][i];
            }
            if (chk) {
                won = chk;
                break;
            }
        }
        if (won) {
            if (won==1) {
                fprintf(fout,"Case #%d: X won\n",I);
            }
            else
            {
                fprintf(fout,"Case #%d: O won\n",I);
            }
            continue;
        }
        int chk = 3;
        for (int i=0; i<4; i++) {
            chk&=x[i][i];
        }
        if (chk) {
            won = chk;
            if (won==1) {
                fprintf(fout,"Case #%d: X won\n",I);
            }
            else
            {
                fprintf(fout,"Case #%d: O won\n",I);
            }
            continue;
        }
        chk = 3;
        for (int i=0; i<4; i++) {
            chk&=x[i][3-i];
        }
        if (chk) {
            won = chk;
            if (won==1) {
                fprintf(fout,"Case #%d: X won\n",I);
            }
            else
            {
                fprintf(fout,"Case #%d: O won\n",I);
            }
            continue;
        }
        if (isComplete) {
            fprintf(fout,"Case #%d: Draw\n",I);
        }
        else
        {
            fprintf(fout,"Case #%d: Game has not completed\n",I);
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
