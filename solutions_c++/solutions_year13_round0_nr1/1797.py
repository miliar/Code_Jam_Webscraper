#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <limits>
#include <string>

using namespace std;

char b[4][4];
bool wins_x;
bool wins_o;
bool full;

void check_row(int i)
{
    wins_x = true;
    wins_o = true;
    for (int j = 0; j < 4; ++j)
    {
        if (b[i][j] == '.')
        {
            wins_x = false;
            wins_o = false;
        }
        else if (b[i][j] == 'X')
        {
            wins_o = false;
        }
        else if (b[i][j] == 'O')
        {
            wins_x = false;
        }
    }
}

void check_col(int i)
{
    wins_x = true;
    wins_o = true;
    for (int j = 0; j < 4; ++j)
    {
        if (b[j][i] == '.')
        {
            wins_x = false;
            wins_o = false;
        }
        else if (b[j][i] == 'X')
        {
            wins_o = false;
        }
        else if (b[j][i] == 'O')
        {
            wins_x = false;
        }
    }
}

void check_diag_a()
{
    wins_x = true;
    wins_o = true;
    for (int j = 0; j < 4; ++j)
    {
        if (b[j][j] == '.')
        {
            wins_x = false;
            wins_o = false;
        }
        else if (b[j][j] == 'X')
        {
            wins_o = false;
        }
        else if (b[j][j] == 'O')
        {
            wins_x = false;
        }
    }
}

void check_diag_b()
{
    wins_x = true;
    wins_o = true;
    for (int j = 0; j < 4; ++j)
    {
        if (b[3-j][j] == '.')
        {
            wins_x = false;
            wins_o = false;
        }
        else if (b[3-j][j] == 'X')
        {
            wins_o = false;
        }
        else if (b[3-j][j] == 'O')
        {
            wins_x = false;
        }
    }
}

string winner()
{
    for (int i = 0; i < 4; ++i)
    {
        check_col(i);
        if (wins_x)
        {
            return "X won";
        }
        else if (wins_o)
        {
            return "O won";
        }
        check_row(i);
        if (wins_x)
        {
            return "X won";
        }
        else if (wins_o)
        {
            return "O won";
        }
    }
    check_diag_a();
    if (wins_x)
    {
        return "X won";
    }
    else if (wins_o)
    {
        return "O won";
    }
    check_diag_b();
    if (wins_x)
    {
        return "X won";
    }
    else if (wins_o)
    {
        return "O won";
    }
    if (full)
    {
        return "Draw";
    }
    return "Game has not completed";
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T;
    fin >> T;
    for (int i = 1; i <= T; ++i)
    {
        full = true;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                fin >> b[j][k];
                if (b[j][k] == '.')
                {
                    full = false;
                }
            }
        }
        fout << "Case #" << i << ": " << winner() << endl;
    }
    return 0;
}
