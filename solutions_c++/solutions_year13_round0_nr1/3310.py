#include <cstdio>

char lines[4][4];
int T, realT;
char dummy[4];

int main()
{
    freopen("tictactoe.in", "r", stdin);
    freopen("tictactoe.out", "w", stdout);

    scanf("%d", &T);
    realT = T;

    for (int t = 1; t <= realT; t++)
    {
        // read the table
        for (int i = 0; i < 4; i++)
        {
            scanf("%s", &lines[i]);
        }

        bool dotExists = false;

        //check all the lines for the combination
        char WINNER = 'T';
        for (int i = 0; i < 4; i++)
        {
            int c[3];
            c[0] = 0; // T
            c[1] = 0; // X
            c[2] = 0; // O
            for (int j = 0; j < 4; j++)
            {
                if (lines[i][j] == '.')
                {
                    dotExists = true;
                }
                if (lines[i][j] == 'T')
                {
                    c[0] = 1;
                }
                if (lines[i][j] == 'X')
                {
                    c[1]++;
                }
                if (lines[i][j] == 'O')
                {
                    c[2]++;
                }
                if ((c[1] == 4) || ((c[1] == 3) && (c[0] == 1)))
                {
                    WINNER = 'X';
                }
                if ((c[2] == 4) || ((c[2] == 3) && (c[0] == 1)))
                {
                    WINNER = 'O';
                }
            }
        }


        if (WINNER == 'T')
        {
            for (int i = 0; i < 4; i++)
            {
                int c[3];
                c[0] = 0; // T
                c[1] = 0; // X
                c[2] = 0; // O
                for (int j = 0; j < 4; j++)
                {
                    if (lines[j][i] == 'T')
                    {
                        c[0] = 1;
                    }
                    if (lines[j][i] == 'X')
                    {
                        c[1]++;
                    }
                    if (lines[j][i] == 'O')
                    {
                        c[2]++;
                    }
                    if ((c[1] == 4) || ((c[1] == 3) && (c[0] == 1)))
                    {
                        WINNER = 'X';
                    }
                    if ((c[2] == 4) || ((c[2] == 3) && (c[0] == 1)))
                    {
                        WINNER = 'O';
                    }
                }
            }
        }

        // diagonals
        if (WINNER == 'T')
        {
            int c[3];
            c[0] = 0; // T
            c[1] = 0; // X
            c[2] = 0; // O
            for (int i = 0; i < 4; i++)
            {
                if (lines[i][i] == 'T')
                {
                    c[0] = 1;
                }
                if (lines[i][i] == 'X')
                {
                    c[1]++;
                }
                if (lines[i][i] == 'O')
                {
                    c[2]++;
                }
                if ((c[1] == 4) || ((c[1] == 3) && (c[0] == 1)))
                {
                    WINNER = 'X';
                }
                if ((c[2] == 4) || ((c[2] == 3) && (c[0] == 1)))
                {
                    WINNER = 'O';
                }
            }
        }

        if (WINNER == 'T')
        {
            int c[3];
            c[0] = 0; // T
            c[1] = 0; // X
            c[2] = 0; // O
            for (int i = 0; i < 4; i++)
            {
                if (lines[i][4 - i - 1] == 'T')
                {
                    c[0] = 1;
                }
                if (lines[i][4 - i - 1] == 'X')
                {
                    c[1]++;
                }
                if (lines[i][4 - i - 1] == 'O')
                {
                    c[2]++;
                }
                if ((c[1] == 4) || ((c[1] == 3) && (c[0] == 1)))
                {
                    WINNER = 'X';
                }
                if ((c[2] == 4) || ((c[2] == 3) && (c[0] == 1)))
                {
                    WINNER = 'O';
                }
            }
        }

        if (WINNER == 'T')
        {
            if (dotExists)
            {
                printf("Case #%d: Game has not completed\n", t);
            }
            else
            {
                printf("Case #%d: Draw\n", t);
            }
        }
        else
        {
            printf("Case #%d: %c won\n", t, WINNER);
        }
    }

    return 0;
}
