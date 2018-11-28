#include <stdio.h>

int main()
{
    char table[5][5];
    int t;
    int i, j;
    char st[10];

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d\n", &t);

    for(int k = 1 ; k <= t ; k++)
    {
        bool noComplete = false;
        for(i = 0 ; i < 4 ; i++)
        {
            gets(st);
            for(j = 0 ; j < 4 ; j++)
            {
                table[i][j] = st[j];
                if(st[j] == '.')
                    noComplete = true;
            }
        }
        gets(st);

        printf("Case #%d: ", k);
        int ret = 0; // 1 is O, 2 is X
        for(i = 0 ; i < 4 ; i++)
        {
            char start = table[i][0];
            if(start == '.') continue;
            j = 1;
            if(start == 'T')
            {
                start = table[i][1];
                if(start == '.') continue;
                j = 2;
            }

            bool ok = true;
            for(; j < 4 ; j++)
            {

                if(table[i][j] != 'T' && table[i][j] != start)
                {
                    ok = false;
                    break;
                }
            }
            if(ok)
            {
                ret = (start == 'O') ? 1 : 2;
                break;
            }
        }

        if(ret != 0)
        {
            if(ret == 1) printf("O won\n");
            else printf("X won\n");
            continue;
        }

        for(j = 0 ; j < 4 ; j++)
        {
            char start = table[0][j];
            if(start == '.') continue;
            i = 1;
            if(start == 'T')
            {
                start = table[1][j];
                if(start == '.') continue;
                i = 2;
            }

            bool ok = true;
            for(; i < 4 ; i++)
                if(table[i][j] != 'T' && table[i][j] != start)
                {
                    ok = false;
                    break;
                }
            if(ok)
            {
                ret = (start == 'O') ? 1 : 2;
                break;
            }
        }

        if(ret != 0)
        {
            if(ret == 1) printf("O won\n");
            else printf("X won\n");
            continue;
        }

        char start = table[0][0];
        int d = 1;
        do
        {
            if(start == '.') break;
            if(start == 'T')
            {
                start = table[1][1];
                d = 2;
                if(start == '.') break;
            }

            bool ok = true;
            for( ; d < 4 ; d++)
                if(table[d][d] != 'T' && table[d][d] != start)
                {
                    ok = false;
                    break;
                }
            if(ok)
            {
                ret = (start == 'O') ? 1 : 2;
            }
        } while(false);

        if(ret != 0)
        {
            if(ret == 1) printf("O won\n");
            else printf("X won\n");
            continue;
        }

        start = table[0][3];
        d = 1;
        do
        {
            if(start == '.') break;
            if(start == 'T')
            {
                start = table[1][2];
                d = 2;
                if(start == '.') break;
            }

            bool ok = true;
            for( ; d < 4 ; d++)
                if(table[d][3 - d] != 'T' && table[d][3 - d] != start)
                {
                    ok = false;
                    break;
                }
            if(ok)
            {
                ret = (start == 'O') ? 1 : 2;
            }
        } while(false);

        if(ret != 0)
        {
            if(ret == 1) printf("O won\n");
            else printf("X won\n");
            continue;
        }

        if(noComplete)
        {
            printf("Game has not completed\n");
        }
        else
        {
            printf("Draw\n");
        }
    }
}
