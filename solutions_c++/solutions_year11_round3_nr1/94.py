///PROBLEM NAME
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <ctype.h>

#define FILE_IN "alarge.in"
#define FILE_OUT "output.txt"
#define MAX 55

using namespace std;

int t, r, c;
int a[MAX][MAX];

bool cover(int x, int y)
{
    a[x][y] = 2;
    if (y+1<c && a[x][y+1] == 1) a[x][y+1] = 3;
    else return false;
    if (x+1<r && a[x+1][y] == 1) a[x+1][y] = 4;
    else return false;
    if (a[x+1][y+1] == 1) a[x+1][y+1] = 5;
    else return false;
    return true;
}

int solve(ostream &fout)
{

    for (int i=0; i<r; i++)
    {
        for (int j=0; j<c; j++)
        {
            cout << a[i][j];
        }
        cout << endl;
    }

    for (int i=0; i<r; i++)
    {
        for (int j=0; j<c; j++)
        {
            if (a[i][j] == 1)
            {
                if (!cover(i,j))
                {
                    fout << "Impossible\n";
                    return 0;
                }
            }
        }
    }

    for (int i=0; i<r; i++)
    {
        for (int j=0; j<c; j++)
        {
            cout << a[i][j];
        }
        cout << endl;
    }


    for (int i=0; i<r; i++)
    {
        for (int j=0; j<c; j++)
        {
            switch(a[i][j])
            {
                case 0:
                    fout << '.';
                    break;
                case 2:
                case 5:
                    fout << '/';
                    break;
                case 3:
                case 4: fout << '\\';
            }
        }
        fout << endl;
    }
}

int main()
{
    ifstream cin(FILE_IN);
    ofstream fout(FILE_OUT);

    cin >> t;
    for (int tcase = 1; tcase <= t; tcase++)
    {
        cin >> r >> c;
        cout << r << " " << c << endl;
        //system("pause");
        char x;
        for (int i=0; i<r; i++)
        {
            for (int j=0; j<c; j++)
            {
                cin >> x;
                if (x == '.') a[i][j] = 0;
                else a[i][j] = 1;
            }
        }

        fout << "Case #" << tcase << ":\n";
        solve(fout);
    }

    fout.close();
    cin.close();
}
