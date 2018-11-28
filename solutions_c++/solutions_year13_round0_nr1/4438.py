#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    int t;
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int k = 0; k < t; k++)
    {
        char a[4][4];
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> a[i][j];
        int mark = false;
        int haspoint = false;
        string ans;
        for (int i = 0; i < 4; i++)
        {
            int t1 = 0, t2 = 0;
            for (int j = 0; j < 4; j++)
                if (a[i][j] == 'X')
                    t1++;
                else if (a[i][j] == 'O')
                    t2++;
                else if (a[i][j] == 'T')
                    t1++,t2++;
                else if (a[i][j] == '.')
                    haspoint = 1;
                else
                    cerr << "WOW";
            if (t1 == 4)
            {
                ans = "X won";
                mark = true;
                break;
            }
            if (t2 == 4)
            {
                ans = "O won";
                mark = true;
                break;
            }
        }
        if (!mark) for (int j = 0; j < 4; j++)
        {
            int t1 = 0, t2 = 0;
            for (int i = 0; i < 4; i++)
                if (a[i][j] == 'X')
                    t1++;
                else if (a[i][j] == 'O')
                    t2++;
                else if (a[i][j] == 'T')
                    t1++,t2++;
                else if (a[i][j] == '.')
                    haspoint = 1;
                else
                    cerr << "WOW";
            if (t1 == 4)
            {
                ans = "X won";
                mark = true;
                break;
            }
            if (t2 == 4)
            {
                ans = "O won";
                mark = true;
                break;
            }
        }
        if (!mark) for (int j = 0; j < 1; j++)
        {
            int t1 = 0, t2 = 0;
            for (int i = 0; i < 4; i++)
                if (a[i][i] == 'X')
                    t1++;
                else if (a[i][i] == 'O')
                    t2++;
                else if (a[i][i] == 'T')
                    t1++,t2++;
                else if (a[i][i] == '.')
                    haspoint = 1;
                else
                    cerr << "WOW";
            if (t1 == 4)
            {
                ans = "X won";
                mark = true;
                break;
            }
            if (t2 == 4)
            {
                ans = "O won";
                mark = true;
                break;
            }
        }
        if (!mark) for (int j = 0; j < 1; j++)
        {
            int t1 = 0, t2 = 0;
            for (int i = 0; i < 4; i++)
                if (a[i][3 - i] == 'X')
                    t1++;
                else if (a[i][3 - i] == 'O')
                    t2++;
                else if (a[i][3 - i] == 'T')
                    t1++,t2++;
                else if (a[i][3 - i] == '.')
                    haspoint = 1;
                else
                    cerr << "WOW";
            if (t1 == 4)
            {
                ans = "X won";
                mark = true;
                break;
            }
            if (t2 == 4)
            {
                ans = "O won";
                mark = true;
                break;
            }
        }
        if (!mark)
            if (!haspoint)
                ans = "Draw";
            else
                ans = "Game has not completed";
        cout << "Case #" << k+1 << ": " << ans << endl;
    }
    return 0;
}
