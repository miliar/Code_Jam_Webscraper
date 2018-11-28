#include <stdio.h>
#include <string.h>

char map[10][10];

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int i,j,n,cnt=1,T;
    scanf("%d",&T);
    while(T--)
    {
        for (i=0;i<4;i++)
        {
            scanf("%s",map[i]);
        }
        printf("Case #%d: ",cnt++);
        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
            {
                if (map[i][j]=='X' || map[i][j]=='T') continue;
                break;
            }
            if (j==4)
            {
                printf("X won\n");
                break;
            }
            for (j=0;j<4;j++)
            {
                if (map[i][j]=='O' || map[i][j]=='T') continue;
                break;
            }
            if (j==4)
            {
                printf("O won\n");
                break;
            }
        }
        if (i<4) continue;
        for (j=0;j<4;j++)
        {
            for (i=0;i<4;i++)
            {
                if (map[i][j]=='X' || map[i][j]=='T') continue;
                break;
            }
            if (i==4)
            {
                printf("X won\n");
                break;
            }
            for (i=0;i<4;i++)
            {
                if (map[i][j]=='O' || map[i][j]=='T') continue;
                break;
            }
            if (i==4)
            {
                printf("O won\n");
                break;
            }
        }
        if (j<4) continue;
        for (i=0;i<4;i++)
        {
            if (map[i][i]=='O' || map[i][i]=='T') continue;
            break;
        }
        if (i==4)
        {
            printf("O won\n");
            continue;
        }
        for (i=0;i<4;i++)
        {
            if (map[i][i]=='X' || map[i][i]=='T') continue;
            break;
        }
        if (i==4)
        {
            printf("X won\n");
            continue;
        }
        for (i=0;i<4;i++)
        {
            if (map[i][3-i]=='O' || map[i][3-i]=='T') continue;
            break;
        }
        if (i==4)
        {
            printf("O won\n");
            continue;
        }
        for (i=0;i<4;i++)
        {
            if (map[i][3-i]=='X' || map[i][3-i]=='T') continue;
            break;
        }
        if (i==4)
        {
            printf("X won\n");
            continue;
        }
        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
            {
                if (map[i][j]=='.') break;
            }
            if (j<4) break;
        }
        if (i<4)
        {
            printf("Game has not completed\n");
            continue;
        }

        printf("Draw\n");
    }
    return 0;
}
