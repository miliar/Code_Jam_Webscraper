#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;

char g[5][5];
int totX, totO, totD;

void init()
{
    totX = 0;
    totO = 0;
    totD = 0;
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
        {
            cin >> g[i][j];
            if (g[i][j] == 'X')
                totX ++;
            if (g[i][j] == 'O')
                totO ++;
            if (g[i][j] == '.')
                totD ++;
        }
}

string work()
{
    string res = "";
    bool winX = false;
    bool winO = false;
    // check row
    for (int i=1; i<=4; i++)
    {
        int cntX = 0, cntO = 0;
        for (int j=1; j<=4; j++)
        {
            if (g[i][j] == 'X' || g[i][j] == 'T')
                cntX ++;
            if (g[i][j] == 'O' || g[i][j] == 'T')
                cntO ++;
        }
        if (cntX >= 4)
            winX = true;
        if (cntO >= 4)
            winO = true;
    }
    
    // check col
    for (int j=1; j<=4; j++)
    {
        int cntX = 0, cntO = 0;
        for (int i=1; i<=4; i++)
        {
            if (g[i][j] == 'X' || g[i][j] == 'T')
                cntX ++;
            if (g[i][j] == 'O' || g[i][j] == 'T')
                cntO ++;
        }
        if (cntX >= 4)
            winX = true;
        if (cntO >= 4)
            winO = true;
    }
    
    // check diag
    {
        int cntX = 0, cntO = 0;
        for (int i=1; i<=4; i++)
        {
            if (g[i][i] == 'X' || g[i][i] == 'T')
                cntX ++;
            if (g[i][i] == 'O' || g[i][i] == 'T')
                cntO ++;
        }
        if (cntX >= 4)
            winX = true;
        if (cntO >= 4)
            winO = true;
    }
    
    {
        int cntX = 0, cntO = 0;
        for (int i=1; i<=4; i++)
        {
            if (g[i][5-i] == 'X' || g[i][5-i] == 'T')
                cntX ++;
            if (g[i][5-i] == 'O' || g[i][5-i] == 'T')
                cntO ++;
        }
        if (cntX >= 4)
            winX = true;
        if (cntO >= 4)
            winO = true;
    }
    
    if (winX || winO)
    {
        if (totX > totO)
        {
            if (winX)
                res = "X won";
            else if (winO)
                res = "O won";
        }
        else
        {
            if (winO)
                res = "O won";
            else if (winX)
                res = "X won";
        }
    }
    else
    {
        if (totD > 0)
            res = "Game has not completed";
        else
            res = "Draw";
    }
    return res;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int tim=1; tim<=T; tim++)
    {
        init();
        cout << "Case #" << tim << ": " << work() << endl;
    }
    return 0;
}
