//
//  main.cpp
//  Codeforces
//
//  Created by Taygrim on 20.03.13.
//  Copyright (c) 2013 Taygrim. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

void check(char c, bool &Xwon, bool &Owon, bool &completed)
{
    switch(c)
    {
        case '.':
        {
            Xwon = false;
            Owon = false;
            completed = false;
            break;
        }
        case 'O':
        {
            Xwon = false;
            break;
        }
        case 'X':
        {
            Owon = false;
            break;
        }
    }
}

int main()
{
    ifstream cin("A-large.in.txt");
    ofstream cout("output.txt");
    long t;
    cin>>t;
    for(long qq=0; qq<t; qq++)
    {
        string field[4];
        for(long i=0; i<4; i++)
            cin>>field[i];
        
        bool completed = true;
        bool Xwon = false;
        bool Owon = false;
        
        for(long q=0; q<2; q++)
            for(long i=0; i<4; i++)
                if(Xwon || Owon)
                    break;
                else
                {
                    Xwon = true;
                    Owon = true;
                    for(long j=0; j<4; j++)
                        check( (q == 0 ? field[i][j] : field[j][i]), Xwon, Owon, completed);
                }
        
        if(!(Xwon || Owon))
        {
            Xwon = true;
            Owon = true;
            for(long i=0; i<4; i++)
                check( field[i][i], Xwon, Owon, completed);
        }
        
        if(!(Xwon || Owon))
        {
            Xwon = true;
            Owon = true;
            for(long i=0; i<4; i++)
                check( field[4-i-1][i], Xwon, Owon, completed);
        }
        
        if(Xwon)
            cout<<"Case #"<<qq+1<<": X won\n";
        if(Owon)
            cout<<"Case #"<<qq+1<<": O won\n";
        if(!(Xwon || Owon) && completed)
            cout<<"Case #"<<qq+1<<": Draw\n";
        if(!(Xwon || Owon) && !completed)
            cout<<"Case #"<<qq+1<<": Game has not completed\n";
    }
}






