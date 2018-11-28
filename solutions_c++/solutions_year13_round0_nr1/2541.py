#include <stdio.h>

int game_state(char field[4][5])
{
    bool draw = true;
    bool f;
    for (int i = 0; i != 4; i++)
    {
        // check X horizontal
        f = true;
        for (int j = 0; f && (j != 4); j++)
        {
            if ((field[i][j] != 'T') && (field[i][j] != 'X'))
            {
                f = false;
            }
            if (field[i][j] == '.')
            {
                draw = false;
            }
        }
        if (f)
        {
            return 1;
        }
        // check X vertical
        f = true;
        for (int j = 0; f && (j != 4); j++)
        {
            if ((field[j][i] != 'T') && (field[j][i] != 'X'))
            {
                f = false;
            }
        }
        if (f)
        {
            return 1;
        }
        // check O horizontal
        f = true;
        for (int j = 0; f && (j != 4); j++)
        {
            if ((field[i][j] != 'T') && (field[i][j] != 'O'))
            {
                f = false;
            }
        }
        if (f)
        {
            return 2;
        }
        // check O vertical
        f = true;
        for (int j = 0; f && (j != 4); j++)
        {
            if ((field[j][i] != 'T') && (field[j][i] != 'O'))
            {
                f = false;
            }
        }
        if (f)
        {
            return 2;
        }
    }
    // check X main diagonal
    f = true;
    for (int i = 0; f && (i != 4); i++)
    {
        if ((field[i][i] != 'X') && (field[i][i] != 'T'))
        {
            f = false;
        }
    }
    if (f)
    {
        return 1;
    }
    // check X secondary diagonal
    f = true;
    for (int i = 0; f && (i != 4); i++)
    {
        if ((field[3 - i][i] != 'X') && (field[3 - i][i] != 'T'))
        {
            f = false;
        }
    }
    if (f)
    {
        return 1;
    }
    // check O main diagonal
    f = true;
    for (int i = 0; f && (i != 4); i++)
    {
        if ((field[i][i] != 'O') && (field[i][i] != 'T'))
        {
            f = false;
        }
    }
    if (f)
    {
        return 2;
    }
    // check O secondary diagonal
    f = true;
    for (int i = 0; f && (i != 4); i++)
    {
        if ((field[3 - i][i] != 'O') && (field[3 - i][i] != 'T'))
        {
            f = false;
        }
    }
    if (f)
    {
        return 2;
    }
    //
    if (draw)
    {
        return 0;
    }
    else
    {
        return 3;
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d\n", &t);
    char field[4][5];
    for (int i = 0; i != t; i++)
    {
        for (int j = 0; j != 4; j++)
        {
            scanf("%s\n", field[j]);
        }
        scanf("\n");
        printf("Case #%d: ", i + 1);
        int state = game_state(field);
        switch (state)
        {
        case 0:
            printf("Draw\n");
            break;
        case 1:
            printf("X won\n");
            break;
        case 2:
            printf("O won\n");
            break;
        case 3:
            printf("Game has not completed\n");
            break;
        }
    }
    return 0;
}