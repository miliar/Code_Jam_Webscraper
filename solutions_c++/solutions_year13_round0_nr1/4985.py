#include <iostream>
#include <cmath>

using namespace std;

char Board[4][4];

void Solve(int n, bool MayContinue)
{
    cout << "Case #" << n << ": ";
    for (int i = 0; i < 4; ++i)
    {
        int cntT = 0, cntO = 0, cntX = 0;
        for (int j = 0; j < 4; ++j)
        {
            if (Board[i][j] == 'T')
                ++cntT;
            else if (Board[i][j] == 'O')
                ++cntO;
            else if (Board[i][j] == 'X')
                ++cntX;
        }
        if (cntX == 4 || (cntX == 3 && cntT == 1))
        {
            cout << "X won" << endl;
            return ;
        }
        else if (cntO == 4 || (cntO == 3 && cntT == 1))
        {
            cout << "O won" << endl;
            return ;
        }
    }
    for (int i = 0; i < 4; ++i)
    {
        int cntT = 0, cntO = 0, cntX = 0;
        for (int j = 0; j < 4; ++j)
        {
            if (Board[j][i] == 'T')
                ++cntT;
            else if (Board[j][i] == 'O')
                ++cntO;
            else if (Board[j][i] == 'X')
                ++cntX;
        }
        if (cntX == 4 || (cntX == 3 && cntT == 1))
        {
            cout << "X won" << endl;
            return ;
        }
        else if (cntO == 4 || (cntO == 3 && cntT == 1))
        {
            cout << "O won" << endl;
            return ;
        }
    }
    int cntT = 0, cntO = 0, cntX = 0;
    for (int i = 0; i < 4; ++i)
    {
        if (Board[i][i] == 'T')
            ++cntT;
        else if (Board[i][i] == 'O')
            ++cntO;
        else if (Board[i][i] == 'X')
            ++cntX;
    }
    if (cntX == 4 || (cntX == 3 && cntT == 1))
    {
        cout << "X won" << endl;
        return ;
    }
    else if (cntO == 4 || (cntO == 3 && cntT == 1))
    {
        cout << "O won" << endl;
        return ;
    }
    cntT = 0, cntO = 0, cntX = 0;
    for (int i = 0; i < 4; ++i)
    {
        if (Board[i][3 - i] == 'T')
            ++cntT;
        else if (Board[i][3 - i] == 'O')
            ++cntO;
        else if (Board[i][3 - i] == 'X')
            ++cntX;
    }
    if (cntX == 4 || (cntX == 3 && cntT == 1))
    {
        cout << "X won" << endl;
        return ;
    }
    else if (cntO == 4 || (cntO == 3 && cntT == 1))
    {
        cout << "O won" << endl;
        return ;
    }
    if (MayContinue)
    {
        cout << "Game has not completed" << endl;
        return ;
    }
    else
    {
        cout << "Draw" << endl;
        return ;
    }
}

int main()
{
    freopen("output.txt", "w", stdout);

    int n;
    cin >> n;
    for (int l = 0; l < n; ++l)
    {
        bool MayContinue = false;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
            {
                cin >> Board[i][j];
                if (Board[i][j] == '.')
                    MayContinue = true;
            }
        Solve(l + 1, MayContinue);
    }
    return 0;
}
