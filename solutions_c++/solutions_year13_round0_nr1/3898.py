#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <iostream>
 
using namespace std;

string grid[5];

bool won(char p, int i, int j, int di, int dj)
{
    for(int k=0; k<4; k++)
        if(grid[i+k*di][j+k*dj] != p && grid[i+k*di][j+k*dj] != 'T')
            return false;
    return true;
}

int main()
{
    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        cout << "Case #" << t << ": ";
        bool filled = true;
        for(int i=0; i<4; i++)
        {
            cin >> grid[i];
            for(int j=0; j<4; j++)
                if(grid[i][j] == '.')
                    filled = false;
        }
        bool xwon = false, owon = false;
        if(won('X',0,0,1,1) || won('X',0,3,1,-1))
            xwon = true;
        if(won('O',0,0,1,1) || won('O',0,3,1,-1))
            owon = true;
        for(int k=0; k<4; k++)
        {
            if(won('X',k,0,0,1) || won('X',0,k,1,0))
                xwon = true;
            if(won('O',k,0,0,1) || won('O',0,k,1,0))
                owon = true;
        }
        if(xwon)
            cout << "X won" << endl;
        else if(owon)
            cout << "O won" << endl;
        else if(filled)
            cout << "Draw" << endl;
        else
            cout << "Game has not completed" << endl;
    }
}
