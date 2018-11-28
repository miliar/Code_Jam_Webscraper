#include <iostream>

using namespace std;

int main() {
    int time, n;
    cin >> n;
    char map[4][10];
    int result;

    for (time = 1; time <= n; time++)
    {
        for (int i = 0; i < 4; i++)
        {
            cin >> map[i];
        }

        cout << "Case #" << time << ": ";
        // check x --------------------------------------------------------------------
        bool win;
        for (int i = 0; i < 4; i++)
        {
            win = true;
            // check row
            for (int j = 0; j < 4; j++)
            {
                if (map[i][j] != 'X' && map[i][j] != 'T')
                {
                    win = false;
                    break;
                }
            }
            if (win) break;

            win = true;
            // check column
            for (int j = 0; j < 4; j++)
            {
                if (map[j][i] != 'X' && map[j][i] != 'T')
                {
                    win = false;
                    break;
                }
            }
            if (win) break;
        }
        if (win) { cout << "X won" << endl; continue; }

        // check diagonal
        win = true;
        for (int i = 0; i < 4; i++)
        {
            if (map[i][i] != 'X' && map[i][i] != 'T')
            {
                win = false;
                break;
            }
        }
        if (win) { cout << "X won" << endl; continue; }
        win = true;
        for (int i = 0; i < 4; i++)
        {
            if (map[i][3-i] != 'X' && map[i][3-i] != 'T')
            {
                win = false;
                break;
            }
        }
        if (win) { cout << "X won" << endl; continue; }

        // check o --------------------------------------------------------------------
        for (int i = 0; i < 4; i++)
        {
            win = true;
            // check row
            for (int j = 0; j < 4; j++)
            {
                if (map[i][j] != 'O' && map[i][j] != 'T')
                {
                    win = false;
                    break;
                }
            }
            if (win) break;

            win = true;
            // check column
            for (int j = 0; j < 4; j++)
            {
                if (map[j][i] != 'O' && map[j][i] != 'T')
                {
                    win = false;
                    break;
                }
            }
            if (win) break;
        }
        if (win) { cout << "O won" << endl; continue; }

        // check diagonal
        win = true;
        for (int i = 0; i < 4; i++)
        {
            if (map[i][i] != 'O' && map[i][i] != 'T')
            {
                win = false;
                break;
            }
        }
        if (win) { cout << "O won" << endl; continue; }
        win = true;
        for (int i = 0; i < 4; i++)
        {
            if (map[i][3-i] != 'O' && map[i][3-i] != 'T')
            {
                win = false;
                break;
            }
        }
        if (win) { cout << "O won" << endl; continue; }

        // check draw -----------------------------------------------------------------
        win = true;
        for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
        {
             if (map[i][j] == '.')
             {
                 win = false;
                 break;
             }
        }
        if (win) { cout << "Draw" << endl; continue; }

        cout << "Game has not completed" << endl;
    }
    return 0;
}

