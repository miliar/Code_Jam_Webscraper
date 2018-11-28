#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <sstream>
#include <iomanip>
using namespace std;

int rows, cols;

int memo[2][4][4][100000];

bool canWin(bool alice, int kr, int kc, int happy);
bool isok(int r, int c, int happy)
{
     if (r < 0 || r >= rows) return false;
     if (c < 0 || c >= cols) return false;
     if (happy & (1 << (4*r + c))) return false;
     return true;
}

bool proc(bool alice, int r, int c, int happy)
{
     if (!isok(r,c,happy)) return false;
     if (canWin(!alice, r, c, (happy | (1 << (4*r + c)))))
        return false;
     return true;
}
     
bool canWin(bool alice, int kr, int kc, int happy)
{
     if (memo[alice][kr][kc][happy] >= 0)
        return (bool)memo[alice][kr][kc][happy];
     
     bool can = false;
     can = can || proc(alice, kr+1, kc+1, happy) ||
         proc(alice, kr+1, kc, happy) ||
         proc(alice, kr, kc+1, happy) ||
         proc(alice, kr-1, kc-1, happy) ||
         proc(alice, kr-1, kc, happy) ||
         proc(alice, kr, kc-1, happy) ||
         proc(alice, kr+1, kc-1, happy) ||
         proc(alice, kr-1, kc+1, happy);
    
    if (can)
        memo[alice][kr][kc][happy] = 1;
    else
        memo[alice][kr][kc][happy] = 0;
    return can;
}

int main()
{
    ifstream in("happy.txt");
    ofstream out("sad.txt");
    int cases;
    in >> cases;     
    
    
    for (int c = 0; c < cases; c++)
    {
    
        for (int z = 0; z < 2; z++)
        for (int x = 0; x < 4; x++)
        for (int y = 0; y < 4; y++)
        for (int w = 0; w < 100000; w++)
            memo[z][x][y][w] = -1;
        
        int startr = 0;
        int startc = 0;
        
            int happy = 0;
        
        in >> rows >> cols;
        for (int i = 0; i < rows; i++)
        {
            string str;
            in >> str;
            for (int j = 0; j < cols; j++)
            {
                if (str[j] == 'K')
                {
                   startr = i;
                   startc = j;
                }
                if (str[j] != '.')
                   happy = (happy | (1 << (4*i + j)));
            }
        }
        bool can = canWin(true, startr, startc, happy);
        //system("PAUSE");
        if (!can)
           out << "Case #" << (c+1) << ": B" << endl;
        else
            out << "Case #" << (c+1) << ": A" << endl;
    }
    return 0;
}
