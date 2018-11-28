#include<stdio.h>
#include<string.h>
int SX,SO,ST,SD;
char s[20][20];
int main()
{
    freopen("aa.in","r",stdin);
    freopen("aa.out","w",stdout);
    int T,aa=0;
    int i,j,can;
    scanf("%d",&T);
    for (aa=1; aa<=T; aa++)
    {
        printf("Case #%d: ",aa);
        for (i=0; i<4; i++) scanf("%s",s[i]);
        can=0;
        for (i=0; i<4; i++)
        {
            SX=SO=ST=0;
            for (j=0; j<4; j++)
            {
                if (s[i][j]=='X') SX++;
                if (s[i][j]=='O') SO++;
                if (s[i][j]=='T') ST++;
            }
            if (SX+ST==4&&SX-ST>=2)
            {
                can=1;
                printf("X won\n");
                break;
            }
            if (SO+ST==4&&SO-ST>=2)
            {
                can=1;
                printf("O won\n");
                break;
            }
        }
        if (can) continue;
        for (j=0; j<4; j++)
        {
            SX=SO=ST=0;
            for (i=0; i<4; i++)
            {
                if (s[i][j]=='X') SX++;
                if (s[i][j]=='O') SO++;
                if (s[i][j]=='T') ST++;
            }
            if (SX+ST==4&&SX-ST>=2)
            {
                can=1;
                printf("X won\n");
                break;
            }
            if (SO+ST==4&&SO-ST>=2)
            {
                can=1;
                printf("O won\n");
                break;
            }
        }
        if (can) continue;
        SX=SO=ST=0;
        for (i=0; i<4; i++)
        {
            if (s[i][i]=='X') SX++;
            if (s[i][i]=='O') SO++;
            if (s[i][i]=='T') ST++;
        }
        if (SX+ST==4&&SX-ST>=2)
        {
            can=1;
            printf("X won\n");
        }
        if (SO+ST==4&&SO-ST>=2)
        {
            can=1;
            printf("O won\n");
        }
        if (can) continue;
        SX=SO=ST=0;
        for (i=0; i<4; i++)
        {
            if (s[i][3-i]=='X') SX++;
            if (s[i][3-i]=='O') SO++;
            if (s[i][3-i]=='T') ST++;
        }
        if (SX+ST==4&&SX-ST>=2)
        {
            can=1;
            printf("X won\n");
        }
        if (SO+ST==4&&SO-ST>=2)
        {
            can=1;
            printf("O won\n");
        }
        if (can) continue;
        for (i=0; i<4; i++)
            for (j=0; j<4; j++)
                if (s[i][j]=='.') can=1;
        if (can) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
