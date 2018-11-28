#include <stdio.h>

#define SIZE 10

int equal(char a, char b)
{
    if (a == b || b == 'T')
        return 1;

    return 0;
}

int check_draw(char board[][SIZE])
{
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            if (board[i][j] == '.')
                return 0;

    return 1;
}

int check(char player, char board[][SIZE])
{
    for (int i = 0; i < 4; ++i)
    {
        if (equal(player, board[i][0]) &&
            equal(player, board[i][1]) &&
            equal(player, board[i][2]) &&
            equal(player, board[i][3]))
        {
            return 1;
        }

        if (equal(player, board[0][i]) &&
            equal(player, board[1][i]) &&
            equal(player, board[2][i]) &&
            equal(player, board[3][i]))
        {
            return 1;
        }
    }

    if (equal(player, board[0][0]) &&
        equal(player, board[1][1]) &&
        equal(player, board[2][2]) &&
        equal(player, board[3][3]))
    {
        return 1;
    }

    if (equal(player, board[0][3]) &&
        equal(player, board[1][2]) &&
        equal(player, board[2][1]) &&
        equal(player, board[3][0]))
    {
        return 1;
    }
    
    return 0;
}

void run(char board[][SIZE])
{
    if (check('X', board))
    {
        printf("X won\n");
    }
    else if (check('O', board))
    {
        printf("O won\n");
    }
    else if (check_draw(board))
    {
        printf("Draw\n");
    }
    else
    {
        printf("Game has not completed\n");
    }
}

int main()
{
    int num_case;
    char board[5][SIZE];

    scanf("%d\n", &num_case);

    for (int i = 1; i <= num_case; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            scanf("%s", board[j]);
        }

#if 0
        for(int j = 0; j < 4; ++j)
        {
            printf("! %s !\n", board[j]);
        }
#endif

        printf("Case #%d: ", i);
        run(board);
    }

    return 0;
}
