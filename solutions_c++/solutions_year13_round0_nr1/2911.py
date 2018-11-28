#include <stdio.h>
#include <string.h>

char mp[10][10];

int ok()
{
    int i,j,k;
    for (i = 0;i < 4;i++)
    {
        for (j = 0;j < 3;j++)
        {
            if (mp[i][j] != mp[i][j + 1])
                break;
        }
        if (j == 3)
        {
            if (mp[i][0] == 'X')
                return 0;
            else if (mp[i][0] == 'O')
                return 1;
        }
    }
    for (j = 0;j < 4;j++)
    {
        for (i = 0;i < 3;i++)
        {
            if (mp[i][j] != mp[i + 1][j])
                break;
        }
        if (i == 3)
        {
            if (mp[0][j] == 'X')
                return 0;
            else if (mp[0][j] == 'O')
                return 1;
        }
    }
    for (i = 0;i < 3;i++)
    {
        if (mp[i][i] != mp[i + 1][i + 1])
            break;
    }
    if (i == 3)
    {
        if (mp[0][0] == 'X')
            return 0;
        else if (mp[0][0] == 'O')
            return 1;
    }
    for (i = 0;i < 3;i++)
    {
        if (mp[i][3 - i] != mp[i + 1][2 - i])
            break;
    }
    if (i == 3)
    {
        if (mp[0][3] == 'X')
            return 0;
        else if (mp[0][3] == 'O')
            return 1;
    }
    for (i = 0;i < 4;i++)
    {
        for (j = 0;j < 4;j++)
        {
            if (mp[i][j] == '.')
            {
                return 2;
            }
        }
    }
    return 3;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k;
    int p,q;
    int t;
    scanf("%d", &t);
    for (k = 1;k <= t;k++)
    {
        p = q = 5;
        for (i = 0;i < 4;i++)
        {
            scanf("%s", &mp[i]);
            for (j = 0;j < 4;j++)
            {
                if (mp[i][j] == 'T')
                {
                    p = i;
                    q = j;
                }
            }
        }
        printf("Case #%d: ", k);
        mp[p][q] = 'X';
        if (ok() == 0)
        {
            printf("X won\n");
            continue;
        }
        mp[p][q] = 'O';
        if (ok() == 1)
        {
            printf("O won\n");
            continue;
        }
        if (ok() == 2)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }
    return 0;
}
