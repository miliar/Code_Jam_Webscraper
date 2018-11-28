#include <iostream>
#include <cstdio>

using namespace std;

int T;

char board[4][4];

void exec(int cas)
{
    //Rows
    for (int i = 0; i < 4; i++)
    {
        char focus = 'T';
        bool win = true;
        for (int j = 0; j < 4; j++)
        {
            char cur = board[i][j];
            if (cur == '.')
            {
                win = false;
                break;
            }
            if (cur == 'T') continue;
            if (focus == 'T')
            {
                focus = cur;
                continue;
            }
            if (focus != cur)
            {
                win = false;
                break;
            }
        }
        if (win)
        {
            printf("Case #%d: %c won\n", cas, focus);
            return;
        }
    }

    for (int j = 0; j < 4; j++)
    {
        char focus = 'T';
        bool win = true;
        for (int i = 0; i < 4; i++)
        {
            char cur = board[i][j];
            if (cur == '.')
            {
                win = false;
                break;
            }
            if (cur == 'T') continue;
            if (focus == 'T')
            {
                focus = cur;
                continue;
            }
            if (focus != cur)
            {
                win = false;
                break;
            }
        }
        if (win)
        {
            printf("Case #%d: %c won\n", cas, focus);
            return;
        }
    }

    char focus = 'T';
    bool win = true;

    for (int i = 0; i < 4; i++)
    {
        char cur = board[i][i];
            if (cur == '.')
            {
                win = false;
                break;
            }
            if (cur == 'T') continue;
            if (focus == 'T')
            {
                focus = cur;
                continue;
            }
            if (focus != cur)
            {
                win = false;
                break;
            }
    }
    if (win)
        {
            printf("Case #%d: %c won\n", cas, focus);
            return;
        }

    focus = 'T';
    win = true;

    for (int i = 0; i < 4; i++)
    {
        char cur = board[i][3-i];
        if (cur == '.')
            {
                win = false;
                break;
            }
            if (cur == 'T') continue;
            if (focus == 'T')
            {
                focus = cur;
                continue;
            }
            if (focus != cur)
            {
                win = false;
                break;
            }
    }
    if (win)
        {
            printf("Case #%d: %c won\n", cas, focus);
            return;
        }




    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (board[i][j] == '.')
            {
                printf("Case #%d: Game has not completed\n", cas);
                return;
            }
        }
    }
    printf("Case #%d: Draw\n", cas);

    //Columns

}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    cin >> T;

    for (int cas = 1; cas <= T; cas++)
    {
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cin >> board[i][j];
                //cout << board[i][j];
            }
        }
        exec(cas);
        cin.ignore(50, '\n');
    }

    return 0;
}
