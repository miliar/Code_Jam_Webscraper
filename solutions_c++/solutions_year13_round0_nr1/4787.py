#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cases = 0;
    char a[5][5];
    cin >> T;
    while (T--)
    {
        cases ++;
        bool points = false;
        for (int i = 0 ; i < 4 ; i++)
            for (int j = 0 ; j < 4 ; j++)
            {
                cin >> a[i][j];
                if (a[i][j] == '.')
                    points = true;
            }
        bool Xwin = false , Owin = false;
        for (int i = 0 ; i < 4 ; i++)
        {
            int tot = 0;
            for (int j = 0 ; j < 4 ; j++)
                if (a[i][j] == 'X' || a[i][j] =='T')
                    tot ++;
            if (tot == 4) Xwin = true;
            tot = 0;
            for (int j = 0 ; j < 4 ; j++)
                if (a[j][i] == 'X' || a[j][i] =='T')
                    tot ++;
            if (tot == 4) Xwin = true;
            tot = 0;
            for (int j = 0 ; j < 4 ; j++)
                if (a[i][j] == 'O' || a[i][j] =='T')
                    tot ++;
            if (tot == 4) Owin = true;
            tot = 0;
            for (int j = 0 ; j < 4 ; j++)
                if (a[j][i] == 'O' || a[j][i] =='T')
                    tot ++;
            if (tot == 4) Owin = true;
        }
        int tot = 0;
        for (int i = 0 ; i < 4 ; i++)
            if (a[i][i] == 'X' || a[i][i] =='T')
                tot ++;
        if (tot == 4) Xwin = true;
        tot = 0;
        for (int i = 0 ; i < 4 ; i++)
            if (a[i][i] == 'O' || a[i][i] =='T')
                tot ++;
        if (tot == 4) Owin = true;
        tot = 0;
        for (int i = 0 ; i < 4 ; i++)
            if (a[i][3-i] == 'X' || a[i][3-i] =='T')
                tot ++;
        if (tot == 4) Xwin = true;
        tot = 0;
        for (int i = 0 ; i < 4 ; i++)
            if (a[i][3-i] == 'O' || a[i][3-i] =='T')
                tot ++;
        if (tot == 4) Owin = true;
        cout << "Case #" << cases << ": ";
        if (Xwin)
        {
            cout << "X won" << endl;
        }
        else
        if (Owin)
        {
            cout << "O won" << endl;
        }
        else
        if (points)
        {
            cout << "Game has not completed" << endl;
        }
        else
        {
            cout << "Draw" << endl;
        }
    }
}