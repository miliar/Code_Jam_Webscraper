//tonynater - Google Code Jam 2013

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <ctype.h>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define sz(x) ((int) x.size())

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

const double pi = 3.141592653589793;
const double tau = 6.283185307179586;
const double epsilon = 1e-6;

int T;

string board[4];

pii Tpos;
void findTpos()
{
    Tpos = pii(-1,-1);
    
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(board[i][j] == 'T')
                Tpos = pii(i,j);
}

bool win(char c)
{
    if(Tpos.first != -1) board[Tpos.first][Tpos.second] = c;
    
    for(int i = 0; i < 4; i++)
        if(c == board[i][0] &&
           board[i][0] == board[i][1] &&
           board[i][1] == board[i][2] &&
           board[i][2] == board[i][3])
            return true;
    
    for(int i = 0; i < 4; i++)
        if(c == board[0][i] &&
           board[0][i] == board[1][i] &&
           board[1][i] == board[2][i] &&
           board[2][i] == board[3][i])
            return true;
    
    if(c == board[0][0] &&
       board[0][0] == board[1][1] &&
       board[1][1] == board[2][2] &&
       board[2][2] == board[3][3])
        return true;
    
    if(c == board[0][3] &&
       board[0][3] == board[1][2] &&
       board[1][2] == board[2][1] &&
       board[2][1] == board[3][0])
        return true;
    
    return false;
}

bool isFilled()
{
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(board[i][j] == '.')
                return false;
    
    return true;
}

int main (int argc, const char * argv[])
{
    freopen("/Users/tonynater/Downloads/A-large.in", "r", stdin);
    freopen("/Users/tonynater/Tony/Computer/Xcode_repos/Miscellaneous/codejam2013/output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
        
    cin >> T;
        
    for(int t = 1; t <= T; t++)
    {
        cin >> board[0] >> board[1] >> board[2] >> board[3];
        
        findTpos();
        
        cout << "Case #" << t << ": ";
        
        if(win('X')) cout << "X won\n";
        else if(win('O')) cout << "O won\n";
        else if(isFilled()) cout << "Draw\n";
        else cout << "Game has not completed\n";
    }
        
    return 0;
}