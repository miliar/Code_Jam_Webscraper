#include <stdio.h>
#include <iostream>
#include <cstring>
#include <cmath>
int M[51][51];
using namespace std;

int main (void)
{
    int n,caso, i,j,k, ncaso;
    int row, col;
    char c;
    bool ok;
    char s[] = "./\\";
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> ncaso;
    for (caso = 1; caso <= ncaso; caso++)
    {
        cin >> row >>col;
        for (i = 0; i < row; i++)
        {
            for (j = 0; j < col; j++)
            {
                cin >> c;
                if (c == '#')
                    M[i][j] = 5;
                else
                    M[i][j] = 0;
            }
            M[i][col] = 0;
        }
        for (j = 0; j <= col; j++)
        {
            M[row][j] = 0;
        }
//        for (i = 0; i < row; i++)
//        {
//            for (j = 0; j < col; j++)
//                cout << M[i][j];
//            cout << endl;
//        }
        ok = true;
        for (i = 0; i < row && ok; i++)
        {
            for (j = 0; j < col && ok; j++)
            {
                if (M[i][j] == 5)
                {
                    if (!(M[i][j+1] && M[i+1][j] && M[i+1][j+1]))
                        ok = false;
                    M[i][j] = M[i+1][j+1] = 1;
                    M[i][j+1] = M[i+1][j] = 2;
                }
            }
        }
        printf ("Case #%d:\n",caso);
        if (ok)
        {
            for (i = 0; i < row; i++)
            {
                for (j = 0; j < col; j++)
                {
                    cout << s[M[i][j]];
                }
                cout << endl;
            }
        }
        else cout <<"Impossible\n";
    }
    return 0;
}
