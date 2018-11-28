#include <stdio.h>

char board[4][4];
int dx[4] = {1, 1, 0, -1};
int dy[4] = {0, 1, 1, 1};

bool isValid(int x, int y)
{
    return x >= 0 && x < 4 && y >= 0 && y < 4;
}

bool isWin(char c)
{
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            for (int d = 0; d < 4; ++d)
            {
                if (!isValid(i + 3 * dx[d], j + 3 * dy[d]))
                {
                    continue;
                }

                bool win = 1;
                for (int l = 0; l < 4; ++l)
                {
                    int x = i + l * dx[d], y = j + l * dy[d];
                    if (board[x][y] != c && board[x][y] != 'T')
                    {
                        win = 0;
                        break;
                    }
                }

                if (win)
                {
                    return true;
                }
            }
        }
    }

    return false;
}

bool isEnd()
{
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (board[i][j] == '.')
            {
                return false;
            }
        }
    }

    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                scanf(" %c", &board[i][j]);
            }
        }
        printf("Case #%d: ", cas);
        if (isWin('X'))
        {
            puts("X won");
        }
        else if (isWin('O'))
        {
            puts("O won");
        }
        else if (isEnd())
        {
            puts("Draw");
        }
        else
        {
            puts("Game has not completed");
        }
    }

    return 0;
}
