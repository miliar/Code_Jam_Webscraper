#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char g[10][10];
int Judge()
{
    int i, j, xc, oc, draw = 0;
    for(i = 1; i <= 4; i ++)
    {
        for(j = 1, xc = oc = 0; j <= 4; j ++)
        {
            xc += g[i][j] == 'X' || g[i][j] == 'T';
            oc += g[i][j] == 'O' || g[i][j] == 'T';
            draw += g[i][j] == '.';
        }
        if(xc == 4) return 1;
        if(oc == 4) return 2;
        for(j = 1, xc = oc = 0; j <= 4; j ++)
        {
            xc += g[j][i] == 'X' || g[j][i] == 'T';
            oc += g[j][i] == 'O' || g[j][i] == 'T';
            draw += g[i][j] == '.';
        }
        if(xc == 4) return 1;
        if(oc == 4) return 2;
    }
    for(j = i = 1, xc = oc = 0; j <= 4; j ++, i ++)
    {
        xc += g[i][j] == 'X' || g[i][j] == 'T';
        oc += g[i][j] == 'O' || g[i][j] == 'T';
        draw += g[i][j] == '.';
    }
    if(xc == 4) return 1;
    if(oc == 4) return 2;
    for(j = 1, i = 4, xc = oc = 0; j <= 4; j ++, i --)
    {
        xc += g[i][j] == 'X' || g[i][j] == 'T';
        oc += g[i][j] == 'O' || g[i][j] == 'T';
        draw += g[i][j] == '.';
    }
    if(xc == 4) return 1;
    if(oc == 4) return 2;
    if(draw == 0) return 3;
    return 4;
}

int main()
{
    int t, i, ca;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    for(scanf("%d", &t), ca = 1; ca <= t; ca ++)
    {
        for(i = 1; i <= 4; i ++)
            scanf("%s", g[i] + 1);
        printf("Case #%d: ", ca);
        switch(Judge())
        {
            case 1: printf("X won\n");break;
            case 2: printf("O won\n");break;
            case 3: printf("Draw\n");break;
            case 4: printf("Game has not completed\n");break;
        }
    }
    return 0;
}
