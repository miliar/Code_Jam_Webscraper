#include <stdio.h>
#include <string.h>

char s[6][6];


int main()
{
    int t, i, j, test;
    int countx, counto, countt, flago, flagx, sumo, sumx;
//    freopen("A-small-attempt1.in","r",stdin);
//    freopen("A-small-attempt1.out", "w", stdout);

    scanf("%d",&t);
    for(test=1;test<=t;test++)
    {
        flagx=flago=0;
        sumo=sumx=0;
        for(i=0;i<4;i++)
        {
            scanf("%s",s[i]);
            counto=countx=countt=0;
            for(j=0;j<4;j++)
            {
                if(s[i][j]=='O') counto++;
                if(s[i][j]=='X') countx++;
                if(s[i][j]=='T') countt++;
            }
            if(counto+countt==4) flago=1;
            if(countx+countt==4) flagx=1;
            sumo+=counto;
            sumx+=countx;
        }
        for(i=0;i<4;i++)
        {
            counto=countx=countt=0;
            for(j=0;j<4;j++)
            {
                if(s[j][i]=='O') counto++;
                if(s[j][i]=='X') countx++;
                if(s[j][i]=='T') countt++;
            }
            if(counto+countt==4) flago=1;
            if(countx+countt==4) flagx=1;
        }
        counto=countx=countt=0;
        for(i=0;i<4;i++)
        {
            if(s[i][i]=='O') counto++;
            if(s[i][i]=='X') countx++;
            if(s[i][i]=='T') countt++;
        }
        if(counto+countt==4) flago=1;
        if(countx+countt==4) flagx=1;
        counto=countx=countt=0;
        for(i=0;i<4;i++)
        {
            if(s[i][3-i]=='O') counto++;
            if(s[i][3-i]=='X') countx++;
            if(s[i][3-i]=='T') countt++;
        }
        if(counto+countt==4) flago=1;
        if(countx+countt==4) flagx=1;

        printf("Case #%d: ",test);
        if(flagx==1) printf("X won\n");
        else if(flago==1) printf("O won\n");
        else if(sumo+sumx>=15) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}

