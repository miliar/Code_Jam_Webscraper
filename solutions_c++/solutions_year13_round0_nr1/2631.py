#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

char mat[5][5];

int main()
{
    freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int n, cases = 1, win;
    scanf("%d", &n);
    while (n--)
    {
        win = -1;
        scanf("%s%s%s%s", mat[0], mat[1], mat[2], mat[3]);

        // row
        for (int i = 0; i < 4; i++)
        {
            int ok = 1;
            for (int j = 0; j < 4; j++)
            {
                if (!(mat[i][j] == 'X' || mat[i][j] == 'T'))
                {
                    ok = 0;
                    break;
                }
            }
            if (ok)
            {
                win = 0;
                break;
            }

            ok = 1;
            for (int j = 0; j < 4; j++)
            {
                if (!(mat[i][j] == 'O' || mat[i][j] == 'T'))
                {
                    ok = 0;
                    break;
                }
            }
            if (ok)
            {
                win = 1;
                break;
            }
        }

        // col
        if (win == -1)
        for (int i = 0; i < 4; i++)
        {
            int ok = 1;
            for (int j = 0; j < 4; j++)
            {
                if (!(mat[j][i] == 'X' || mat[j][i] == 'T'))
                {
                    ok = 0;
                    break;
                }
            }
            if (ok)
            {
                win = 0;
                break;
            }

            ok = 1;
            for (int j = 0; j < 4; j++)
            {
                if (!(mat[j][i] == 'O' || mat[j][i] == 'T'))
                {
                    ok = 0;
                    break;
                }
            }
            if (ok)
            {
                win = 1;
                break;
            }
        }

        // other
        if (win == -1)
        {
            int ok = 1;
            for (int i = 0; i < 4; i++)
            {
                if (!(mat[i][i] == 'X' || mat[i][i] == 'T'))
                {
                    ok = 0;
                    break;
                }
            }
            if (ok)
                win = 0;

            if (win == -1)
            {
                ok = 1;
                for (int i = 0; i < 4; i++)
                {
                    if (!(mat[i][i] == 'O' || mat[i][i] == 'T'))
                    {
                        ok = 0;
                        break;
                    }
                }
                if (ok)
                    win = 1;
            }
        }

        if (win == -1)
        {
            int ok = 1;
            for (int i = 0; i < 4; i++)
            {
                if (!(mat[i][3 - i] == 'X' || mat[i][3 - i] == 'T'))
                {
                    ok = 0;
                    break;
                }
            }
            if (ok)
                win = 0;

            if (win == -1)
            {
                ok = 1;
                for (int i = 0; i < 4; i++)
                {
                    if (!(mat[i][3 - i] == 'O' || mat[i][3 - i] == 'T'))
                    {
                        ok = 0;
                        break;
                    }
                }
                if (ok)
                    win = 1;
            }
        }

        printf("Case #%d: ", cases++);

        if (win == -1)
        {
            int finish = 1;
            for (int i = 0; i < 4 && finish; i++)
            {
                for (int j = i; j < 4; j++)
                {
                    if (mat[i][j] == '.' || mat[j][i] == '.')
                    {
                        finish = 0;
                        break;
                    }
                }
            }
            printf("%s\n", finish ? "Draw" : "Game has not completed");
        }
        else
            printf("%s won\n", win ? "O" : "X");

    }
    return 0;
}
