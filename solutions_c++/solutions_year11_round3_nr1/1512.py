#include <iostream>
#include <stdio.h>

using namespace std;

void printResult(int, int, int);

char pic[55][55];
int main()
{
   // freopen("large.txt", "r", stdin);
   // freopen("out.txt", "w", stdout);

    int numCase, row, column;

    cin >> numCase;

    for (int i = 1; i <= numCase; ++i)
    {
        cin >> row >> column;

        for (int j = 0; j < row; ++j)
        {
            for (int k = 0; k < column; ++k)
            {
                cin >> pic[j][k];
            }
        }

        printResult(i, row, column);
    }

    return 0;
}

void printResult(int numCase, int row, int column)
{
    cout << "Case #" << numCase << ":" << endl;
    bool flag = 0;
    //replace tiles
    for (int i = 0; i < row; ++i)
    {
        for (int j = 0; j < column; ++j)
        {
            if (pic[i][j] == '#')
            {
                if (i == row - 1 || j == column - 1){
                    cout << "Impossible" << endl;
                    flag = 1;
                    break;
                }
                if (pic[i][j+1] == '#' && pic[i+1][j] == '#' && pic[i+1][j+1] == '#')
                {
                    pic[i][j] = '/';
                    pic[i][j+1] = '\\';
                    pic[i+1][j] = '\\';
                    pic[i+1][j+1] = '/';
                }
                else
                {
                    cout << "Impossible" << endl;
                    flag = 1;
                    break;
                }
            }
        }
        if (flag == 1)break;
    }
    //print tiles
    if (flag == 0)
    {
        for (int i = 0; i < row; ++i)
        {
            for (int j = 0; j < column; ++j)
            {
                cout << pic[i][j];
            }
            cout << endl;
        }
    }
}
