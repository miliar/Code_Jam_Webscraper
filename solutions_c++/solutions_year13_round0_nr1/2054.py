#include <iostream>
#include <stdio.h>

using namespace std;
const int MAXN = 5;
const int n = 4;

bool check(char table[][MAXN], char type)
{
    bool res = false;
    int diag1 = 0, diag2 = 0;
    for (int i = 0; i < n; ++i)
    {
        int rows = 0;
        for (int j = 0; j < n; ++j)
            rows += (table[i][j] == type);

        res = res | (rows == 4);
        int cols = 0;
        for (int j = 0; j < n; ++j)
            cols += (table[j][i] == type);
        res = res | (cols == 4);

        diag1 += (table[i][i] == type);
        diag2 += (table[i][n - i - 1] == type);
    }
    res = res | (diag1 == 4) | (diag2 == 4);
    return res;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("tictactoe.out", "w", stdout);
    int nTest;
    cin >> nTest;

    char table[MAXN][MAXN];

    for (int test = 1; test <= nTest; ++test)
    {
        bool finish = true;
        int tx = -1, ty = -1;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
            {
                cin >> table[i][j];
                if (table[i][j] == '.')
                    finish = false;
                else if (table[i][j] == 'T')
                {
                    tx = i;
                    ty = j;
                    table[i][j] = 'X';
                }
            }

        int res = 0;
        if (check(table, 'X'))
            res = 1;

        if (tx >= 0)
            table[tx][ty] = 'O';

        if (check(table, 'O'))
                res = 2;

        if (res == 1)
            cout << "Case #" << test << ": X won";
        else if (res == 2)
            cout << "Case #" << test << ": O won";
        else if (finish)
            cout << "Case #" << test << ": Draw";
        else
            cout << "Case #" << test << ": Game has not completed";
        cout << endl;
    }
    return 0;
}
