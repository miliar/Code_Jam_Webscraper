#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;

int memo[200][200];
bool rock[200][200];
int endr;
 int endc;

int recurse(int r, int c)
{
    if (rock[r][c]) return 0;
    if (r == endr && c == endc) return 1;
    if (r >= endr) return 0;
    if (c >= endc) return 0;
    
    if (memo[r][c] >= 0) return memo[r][c];
    
    int total = 0;
    total += recurse(r+2, c+1);
    total += recurse(r+1, c+2);
    total = total % 10007;
    memo[r][c] = total;
    return total;
}

int main()
{
    ifstream in("happy.txt");
    ofstream out("sad.txt");
    int cases;
    in >> cases;
    for (int c = 0; c < cases; c++)
    {
        for (int i = 0; i < 200; i++)
        for (int j = 0; j < 200; j++)
        {
            memo[i][j] = -1;
            rock[i][j] = false;
        }
        
        int numrocks;
        in >> endr >> endc >> numrocks;
        for (int i = 0; i < numrocks; i++)
        {
            int row, col;
            in >> row >> col;
            rock[row][col] = true;
        }
        out << "Case #" << (c+1) << ": " << recurse(1,1) << endl;
    }  
    return 0;
}
