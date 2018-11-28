#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

string result[4];

int T;
string g[4];

int check()
{
    bool full = true;
    for (int i = 0; i < 4; i++)
    {
        if (!full) break;
        for (int j = 0; j < 4; j++)
            if (g[i][j] == '.')
            {
                full = false;
                break;
            }
    }
    
    for (int i = 0; i < 4; i++)
    {
        char ch = g[i][0];
        bool ok = true;
        if (ch == '.') continue;
        for (int j = 1; j < 4; j++)
        {
            if (g[i][j] == '.')
            {
                ok = false;
                break;
            }
            if (g[i][j] == 'T')
                continue;
            if (ch == 'T')
            {
                ch = g[i][j];
                continue;
            }
            if (ch != g[i][j])
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            if (ch == 'X') return 0;
            else return 1;
        }
    }
    
    for (int j = 0; j < 4; j++)
    {
        char ch = g[0][j];
        bool ok = true;
        if (ch == '.') continue;
        for (int i = 1; i < 4; i++)
        {
            if (g[i][j] == '.')
            {
                ok = false;
                break;
            }
            if (g[i][j] == 'T')
                continue;
            if (ch == 'T')
            {
                ch = g[i][j];
                continue;
            }
            if (ch != g[i][j])
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            if (ch == 'X') return 0;
            else return 1;
        }
    }
    
    char ch = g[0][0];
    if (ch != '.')
    {
        bool ok = true;
        for (int  i = 0, j = 0; i < 4, j < 4; i++, j++)
        {
            if (g[i][j] == '.')
            {
                ok = false;
                break;
            }
            if (g[i][j] == 'T')
                continue;
            if (ch == 'T')
            {
                ch = g[i][j];
                continue;
            }
            if (ch != g[i][j])
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            if (ch == 'X') return 0;
            else return 1;
        }
    }
    
    ch = g[0][3];
    if (ch != '.')
    {
        bool ok = true;
        for (int  i = 0, j = 3; i < 4, j >= 0; i++, j--)
        {
            if (g[i][j] == '.')
            {
                ok = false;
                break;
            }
            if (g[i][j] == 'T')
                continue;
            if (ch == 'T')
            {
                ch = g[i][j];
                continue;
            }
            if (ch != g[i][j])
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            if (ch == 'X') return 0;
            else return 1;
        }
    }
    
    if (full) return 2; else return 3;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    result[0] = "X won";
    result[1] = "O won";
    result[2] = "Draw";
    result[3] = "Game has not completed";
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++)
    {
        char s[10];
        for (int i = 0; i < 4; i++)
        {
            scanf("%s\n", s);
            g[i] = s;
        }
     //   for (int i = 0; i < 4; i++)
       //     cout << g[i] << endl;
       // scanf("%s", s);
        cout << "Case #" << t << ": " << result[check()] << endl;
    }
    return 0;
}
