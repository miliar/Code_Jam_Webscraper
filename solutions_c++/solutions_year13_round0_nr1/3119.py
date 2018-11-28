//
//  main.cpp
//  CodeJam
//
//  Created by Wade Norris on 4/12/13.
//  Copyright (c) 2013 norris. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool checkVerticle(char input[4][4], int i, char c)
{
    for(int j=0; j<4; j++)
    {
        if(input[i][j] != c && input[i][j] != 'T')
            return false;
    }
    
    return true;
}

bool checkHorizontal(char input[4][4], int i, char c)
{
    for(int j=0; j<4; j++)
    {
        if(input[j][i] != c && input[j][i] != 'T')
            return false;
    }
    
    return true;
}

bool checkDiagonal(char input[4][4], char c)
{
    for(int j=0; j<4; j++)
    {
        if(input[j][j] != c && input[j][j] != 'T')
            return false;
    }
    
    return true;
}

bool checkOtherDiagonal(char input[4][4], char c)
{
    for(int j=0, i=3; j<4; j++, i--)
    {
        if(input[i][j] != c && input[i][j] != 'T')
            return false;
    }
    
    return true;
}

bool notOver(char input[4][4])
{
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if(input[i][j] == '.')
                return true;
        }
    }
    
    return false;
}

int main (int argc, char* argv[]) {
    string line;
    ifstream myfile (argv[1]);

    if (!myfile.is_open())
    {
        cout << "Error opening file!" << endl;
        return 0;
    }
    
    getline (myfile,line);
    
    int numTestCases = atoi(line.c_str());
    
    for(int i=0; i<numTestCases; i++)
    {
        char input[4][4];
        
        getline (myfile,line);
        input[0][0] = line[0];
        input[1][0] = line[1];
        input[2][0] = line[2];
        input[3][0] = line[3];
        
        getline (myfile,line);
        input[0][1] = line[0];
        input[1][1] = line[1];
        input[2][1] = line[2];
        input[3][1] = line[3];
        
        getline (myfile,line);
        input[0][2] = line[0];
        input[1][2] = line[1];
        input[2][2] = line[2];
        input[3][2] = line[3];
        
        getline (myfile,line);
        input[0][3] = line[0];
        input[1][3] = line[1];
        input[2][3] = line[2];
        input[3][3] = line[3];
        
        if(  checkVerticle(input, 0, 'X')
          || checkVerticle(input, 1, 'X')
          || checkVerticle(input, 2, 'X')
          || checkVerticle(input, 3, 'X')
           || checkHorizontal(input, 0, 'X')
           || checkHorizontal(input, 1, 'X')
           || checkHorizontal(input, 2, 'X')
           || checkHorizontal(input, 3, 'X')
           || checkDiagonal(input, 'X')
           || checkOtherDiagonal(input, 'X'))
        {
            cout << "Case #" << i+1 << ": X won" << endl;
        }
        
        else if(  checkVerticle(input, 0, 'O')
           || checkVerticle(input, 1, 'O')
           || checkVerticle(input, 2, 'O')
           || checkVerticle(input, 3, 'O')
           || checkHorizontal(input, 0, 'O')
           || checkHorizontal(input, 1, 'O')
           || checkHorizontal(input, 2, 'O')
           || checkHorizontal(input, 3, 'O')
           || checkDiagonal(input, 'O')
           || checkOtherDiagonal(input, 'O'))
        {
            cout << "Case #" << i+1 << ": O won" << endl;
        }
        
        else if( notOver(input))
        {
            cout << "Case #" << i+1 << ": Game has not completed" << endl;
        }
        else
        {
            cout << "Case #" << i+1 << ": Draw" << endl;
        }
        
        getline (myfile,line);
    }
    
    myfile.close();

    return 0;
}


