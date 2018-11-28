#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{
    char g[5][5];
    int n;
    cin >> n;
    int t = 0;
    ofstream fout;
    fout.open("out.out", ios::out);
    while (t < n)
    {
        ++t;
        bool rx[4] = {true, true, true, true};
        bool cx[4] = {true, true, true, true};
        bool ro[4] = {true, true, true, true};
        bool co[4] = {true, true, true, true};
        bool xd[2] = {true, true};
        bool od[2] = {true, true};
        bool dot = false;
        for (int i = 0; i < 4; ++i)
        {
            cin >> g[i];
            for (int j = 0; j < 4; ++j)
            {
                if (g[i][j] == '.')
                    dot = true;
                if (g[i][j] == 'X' || g[i][j] == '.')
                {
                    ro[i] = false;
                    co[j] = false;
                }
                if (g[i][j] == 'O' || g[i][j] == '.')
                {
                    rx[i] = false;
                    cx[j] = false;
                }
                if (i == j)
                {
                    if (g[i][j] == 'X' || g[i][j] == '.')
                    {
                        od[0] = false;
                    }
                    if (g[i][j] == 'O' || g[i][j] == '.')
                    {
                        xd[0] = false;
                    }
                }
                if (i + j == 3)
                {
                    if (g[i][j] == 'X' || g[i][j] == '.')
                    {
                        od[1] = false;
                    }
                    if (g[i][j] == 'O' || g[i][j] == '.')
                    {
                        xd[1] = false;
                    }
                }
            }
        }
        bool x, o;
        x = o = false;
        for (int i = 0; i < 4; ++i)
        {
            if (rx[i] || cx[i] || xd[0] || xd[1])
                x = true;
            if (ro[i] || co[i] || od[0] || od[1])
                o = true;
        }
        if (x)
        {
            fout << "Case #" << t << ": X won" << endl;
        }
        else if (o)
        {
            fout << "Case #" << t << ": O won" << endl;
        }
        else if (dot)
        {
            fout << "Case #" << t << ": Game has not completed" << endl;
        }
        else
        {
            fout << "Case #" << t << ": Draw" << endl;
        }
    }
    return 0;
}
