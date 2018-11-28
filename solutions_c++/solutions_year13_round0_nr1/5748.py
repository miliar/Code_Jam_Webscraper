//
//  main.cpp
//  Tic_Tac_Toe_Tomek
//
//  Created by Jinchao Ye on 4/13/13.
//  Copyright (c) 2013 Jinchao Ye. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int T;
char game[4][4];
const long long size_limit = 100000000000000;
char tmp[size_limit];

void checkGameState(ofstream & fout, int t)
{
    bool finished = true;
    for(int r = 0; r < 4; r++)
    {
        int c = 0;
        char kind = 'T';
        for(c = 0; c < 4; c++)
        {
            if(game[r][c]=='.')
            {
                finished = false;
                break;
            }
            else if(game[r][c]=='T')
            {
                continue;
            }
            else if(kind=='T')
            {
                kind = game[r][c];
            }
            else
            {
                if(game[r][c] != kind)
                    break;
                else
                    continue;
            }
        }
        if(c == 4)
        {
            fout<<"Case #"<<t<<": "<<kind<<" won\n";
            return;
        }
    }
    for(int r = 0; r < 4; r++)
    {
        int c = 0;
        char kind = 'T';
        for(c = 0; c < 4; c++)
        {
            if(game[c][r]=='.')
            {
                finished = false;
                break;
            }
            else if(game[c][r]=='T')
            {
                continue;
            }
            else if(kind=='T')
            {
                kind = game[c][r];
            }
            else
            {
                if(game[c][r] != kind)
                    break;
                else
                    continue;
            }
        }
        if(c == 4)
        {
            fout<<"Case #"<<t<<": "<<kind<<" won\n";
            return;
        }
    }
    char kind = 'T';
    int i = 0;
    for(i = 0; i < 4; i++)
    {
        if(game[i][i]=='.')
        {
            finished = false;
            break;
        }
        else if(game[i][i]=='T')
            continue;
        else if(kind=='T')
        {
            kind = game[i][i];
        }
        else
        {
            if(game[i][i] != kind)
                break;
            else
                continue;
        }
    }
    if(i==4)
    {
        fout<<"Case #"<<t<<": "<<kind<<" won\n";
        return;
    }
    kind = 'T';
    for(i = 0; i < 4; i++)
    {
        if(game[i][3-i]=='.')
        {
            finished = false;
            break;
        }
        else if(game[i][3-i]=='T')
            continue;
        else if(kind=='T')
        {
            kind = game[i][3-i];
        }
        else
        {
            if(game[i][3-i] != kind)
                break;
            else
                continue;
        }
    }
    if(i==4)
    {
        fout<<"Case #"<<t<<": "<<kind<<" won\n";
        return;
    }
    if(finished)
    {
        fout<<"Case #"<<t<<": "<<"Draw\n";
        return;
    }
    else
    {
        fout<<"Case #"<<t<<": "<<"Game has not completed\n";
        return;
    }
}

int main(int argc, const char * argv[])
{
    ifstream fin("/Users/jcye/Desktop/A.txt");
    ofstream fout("/Users/jcye/Desktop/A_result.txt");
    fin>>T;
    fin.getline(tmp, size_limit);
    for(int i = 0; i < T; i++)
    {
        for(int row = 0; row < 4; row++)
        {
            for(int col = 0; col < 4; col++)
            {
                fin>>game[row][col];
            }
            fin.getline(tmp, size_limit);
        }
        checkGameState(fout, i+1);
        fin.getline(tmp, size_limit);
    }
    fin.close();
    fout.close();
    return 0;
}

