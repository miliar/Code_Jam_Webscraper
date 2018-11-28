//
//  main.cpp
//  codeJam2013
//
//  Created by Guillaume Derval on 13/04/13.
//  Copyright (c) 2013 Guillaume Derval. All rights reserved.
//

#include <iostream>
#include <fstream>

int main(int argc, const char * argv[])
{
    std::ifstream finput ("/Users/guillaumederval/Dropbox/Q4_INFO_perso/codeJam2013/codeJam2013/A-large.in");
    std::ofstream foutput ("/Users/guillaumederval/Dropbox/Q4_INFO_perso/codeJam2013/codeJam2013/out.out");
    
    std::istream& input = finput;
    std::ostream& output = foutput;
    
    int n;
    input >> n;
    for(int test = 0; test < n; test++)
    {
        char game[4][4];
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                input >> game[j][k];
            }
        }
        
        bool canBeDraw = true;
        char win = '.';
        
        int possibleDiag1 = 3;
        int possibleDiag2 = 3;
        for(int j = 0; j < 4; j++)
        {
            int possibleLine = 3;
            int possibleCol = 3;
            
            if(game[j][j] == '.')
                possibleDiag1 = 0;
            else if(game[j][j] == 'O')
                possibleDiag1 &= 1;
            else if(game[j][j] == 'X')
                possibleDiag1 &= 2;
            
            if(game[j][3-j] == '.')
                possibleDiag2 = 0;
            else if(game[j][3-j] == 'O')
                possibleDiag2 &= 1;
            else if(game[j][3-j] == 'X')
                possibleDiag2 &= 2;
            
            for(int k = 0; k < 4; k++)
            {
                if(game[j][k] == '.')
                {
                    possibleLine = 0;
                    canBeDraw = false;
                }
                else if(game[j][k] == 'O')
                    possibleLine &= 1;
                else if(game[j][k] == 'X')
                    possibleLine &= 2;
                
                if(game[k][j] == '.')
                {
                    possibleCol = 0;
                    canBeDraw = false;
                }
                else if(game[k][j] == 'O')
                    possibleCol &= 1;
                else if(game[k][j] == 'X')
                    possibleCol &= 2;
            }
            
            if(possibleLine)
                win = possibleLine == 1 ? 'O' : 'X';
            if(possibleCol)
                win = possibleCol == 1 ? 'O' : 'X';
        }
        if(possibleDiag1)
            win = possibleDiag1 == 1 ? 'O' : 'X';
        if(possibleDiag2)
            win = possibleDiag2 == 1 ? 'O' : 'X';
        
        output << "Case #" << (test+1) << ": ";
        if(win == '.')
        {
            if(canBeDraw)
                output << "Draw";
            else
                output << "Game has not completed";
        }
        else
            output << win << " won";
        output << std::endl;
    }
    
    finput.close();
    foutput.close();
    return 0;
}

