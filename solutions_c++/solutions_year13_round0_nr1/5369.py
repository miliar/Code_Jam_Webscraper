#include <cstdio>

char map[5][5];

int check(char ch)
{
    switch (ch)
    {
    case 'X':
        return 0;
    case 'O':
        return 1;
    case 'T':
        return 2;
    case '.':
        return 3;
    }
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int cas = 1;
    int t;
    scanf("%d", &t);
    while (t --)
    {
        for (int i = 0; i < 4; i ++)
            scanf("%s", map[i]);
        printf("Case #%d: ", cas ++);
        bool flagx = false;
        bool flago = false;
        bool draw = false;
        int nn[4];//nx = no = nt = nd = 0;
        for (int i = 0; i < 4; i ++)
        {
            nn[0] = nn[1] = nn[2] = nn[3] = 0;
            for (int j = 0; j < 4; j ++)
                nn[check(map[i][j])] ++;
            if (nn[0] + nn[2] >= 4)
                flagx = true;
            if (nn[1] + nn[2] >= 4)
                flago = true;
            if (nn[0] + nn[3] >= 4 || nn[1] + nn[3] >= 4)
                draw = true;
            if (flagx || flago)
                break;
        }
        if (!flagx && !flago)
        {
            for (int j = 0; j < 4; j ++)
            {
                nn[0] = nn[1] = nn[2] = nn[3] = 0;
                for (int i = 0; i < 4; i ++)
                    nn[check(map[i][j])] ++;
                if (nn[0] + nn[2] >= 4)
                    flagx = true;
                if (nn[1] + nn[2] >= 4)
                    flago = true;
                if (nn[0] + nn[3] >= 4 || nn[1] + nn[3] >= 4)
                    draw = true;
                if (flagx || flago)
                    break;
            }
        }
        if (!flagx && !flago)
        {
            nn[0] = nn[1] = nn[2] = nn[3] = 0;
            for (int i = 0; i < 4; i ++)
                nn[check(map[i][i])] ++;
            if (nn[0] + nn[2] >= 4)
                flagx = true;
            if (nn[1] + nn[2] >= 4)
                flago = true;
            if (nn[0] + nn[3] >= 4 || nn[1] + nn[3] >= 4)
                draw = true;
        }
        if (!flagx && !flago)
        {
            nn[0] = nn[1] = nn[2] = nn[3] = 0;
            for (int i = 0; i < 4; i ++)
                nn[check(map[3-i][i])] ++;
            if (nn[0] + nn[2] >= 4)
                flagx = true;
            if (nn[1] + nn[2] >= 4)
                flago = true;
            if (nn[0] + nn[3] >= 4 || nn[1] + nn[3] >= 4)
                draw = true;
        }
        if ( flagx )
            printf("X won\n");
        else if ( flago )
            printf("O won\n");
        else if ( !draw )
            printf("Draw\n");
        else printf("Game has not completed\n");

    }
    return 0;
}
