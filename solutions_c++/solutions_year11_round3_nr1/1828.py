/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Moritz Schaefer (), mollitz@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <map>
#include <stdio.h>

using namespace std;

void preCalculation()
{}

bool blueFound(char input[][50], int i, int j, int r, int c)
{
    if(i+1 == r || j+1 == c)
        return false;
    if(input[i+1][j] == '#' && 
       input[i+1][j+1] == '#' &&
       input[i][j+1] == '#')
    {
       input[i][j] = input[i+1][j+1] = '/';
       input[i][j+1] = input[i+1][j] = '\\';
       return true;
    }
    else
        return false;
}

string calculate()
{
    char input[50][50];
    int r, c;
    cin >> r >> c;
    for(int i=0; i<r; i++)
    {
        for(int j=0;j<c; j++)
        {
            cin >> input[i][j];
        }
    }

    for(int i=0;i<r;i++)
    {
        for(int j=0; j<c; j++)
        {
            if(input[i][j] == '#')
                if(!blueFound(input, i, j, r, c))
                    return("\nImpossible");
        }
    }
    string out;
    for(int i=0; i<r; i++)
    {
        out.push_back('\n');
        out.append(input[i], c);
    }

    return out;
}


int main(int argc, char *argv[])
{
    int cases;
    cin >> cases;
    preCalculation();
    for(int i = 0; i < cases; i++)
    {
        cout << "Case #" << i+1 << ": " << calculate() << endl;
    }
    return 0;
}
