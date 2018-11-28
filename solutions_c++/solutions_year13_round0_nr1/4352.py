#include <iostream>
#include <string>

using namespace std;

bool playerWin(char player, string a[])
{
    int gor[4][256] = {0};
    int ver[4][256] = {0};
    int d[2][256] = {0};
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        {
            gor[i][a[i][j]]++;
            ver[j][a[i][j]]++;
            if (i == j) d[0][a[i][j]]++;
            if (i == 3 - j) d[1][a[i][j]]++;
        }
    if (d[0][player] + d[0]['T'] == 4) return true;
    if (d[1][player] + d[1]['T'] == 4) return true;
    for (int i = 0; i < 4; ++i)
    {
        if (gor[i][player] + gor[i]['T'] == 4) return true;
        if (ver[i][player] + ver[i]['T'] == 4) return true;
    }
    return false;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        string a[4];
        for (int i = 0; i < 4; ++i)
            cin >> a[i];
        int c[256] = {0};
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                c[a[i][j]]++;
        if (playerWin('O', a))
        {
            cout << "Case #" << t << ": O won" << endl;
            continue;
        }
        if (playerWin('X', a))
        {
            cout << "Case #" << t << ": X won" << endl;
            continue;
        }
        if (c['.'] == 0)
            cout << "Case #" << t << ": Draw" << endl;
        else
            cout << "Case #" << t << ": Game has not completed" << endl;
    }
    return 0;
}