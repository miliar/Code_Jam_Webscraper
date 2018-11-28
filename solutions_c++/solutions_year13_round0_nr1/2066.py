#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <array>

using namespace std;

#define LOCAL_EXEC 1


bool
Won (
    char Board[4][4],
    char Who
    )
{
    bool row;
    bool col;
    bool mainDiag = true;
    bool offDiag = true;

    for (int i = 0; i < 4; ++i)
    {
        row = true;
        col = true;
        for (int j = 0; j < 4; ++j)
        {
            if (Board[i][j] != Who && Board[i][j] != 'T')
            {
                row = false;
            }
            if (Board[j][i] != Who && Board[j][i] != 'T')
            {
                col = false;
            }
            if (i == j && Board[i][j] != Who && Board[i][j] != 'T')
            {
                mainDiag = false;
            }
            if ((3 - i) == j && Board[i][j] != Who && Board[i][j] != 'T')
            {
                offDiag = false;
            }
        }

        if (row || col)
        {
            return true;
        }
    }

    if (mainDiag || offDiag)
    {
        return true;
    }

    return false;
}


int
main ()
{
#if (LOCAL_EXEC == 1)
    freopen("D:\\Input.txt", "r", stdin);
    freopen("D:\\Output.txt", "w", stdout);
#endif

    int T;
    scanf("%d", &T);
    getchar();

    for (int i = 1; i <= T; ++i)
    {
        char board[4][4];
        bool complete = true;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                scanf("%c", &board[j][k]);
                if (board[j][k] == '.')
                {
                    complete = false;
                }
            }
            getchar();
        }

        bool xWon = Won(board, 'X');
        bool oWon = xWon ? false : Won(board, 'O');

        printf("Case #%d: ", i);
        if (xWon)
        {
            printf("X won\n");
        }
        else if (oWon)
        {
            printf("O won\n");
        }
        else if (complete)
        {
            printf("Draw\n");
        }
        else
        {
            printf("Game has not completed\n");
        }

        getchar();
    }

    return 0;
}
