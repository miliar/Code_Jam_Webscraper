#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

char map[5][5];
int main()
{
    freopen("A-small-practice.in", "r", stdin);
    freopen("A-small-practice.out", "w", stdout);
    int countO,countX,countT,countspot;
    int T;
    while(scanf("%d",&T)!=EOF)
    {
        for(int i=1;i<=T;i++)
        {
            for(int m=0;m<4;m++)
                    scanf("%s",map[m]);
            int state=0;//开始默认平局

            for(int m=0;m<4;m++)
            {
                countO=countT=countX=countspot=0;
                for(int n=0;n<4;n++)
                {
                    if(map[m][n]=='O')countO++;
                    else if(map[m][n]=='X')countX++;
                    else if(map[m][n]=='T')countT++;
                    else countspot++;
                }
                if(countO==4||countO==3&&countT==1){state=1;goto PRINT;}
                else if(countX==4||countX==3&&countT==1){state=2;goto PRINT;}
                else if(countspot>0)state=-1;
                //else state=0;
            }

            for(int n=0;n<4;n++)
            {
                countO=countT=countX=countspot=0;
                for(int m=0;m<4;m++)
                {
                    if(map[m][n]=='O')countO++;
                    else if(map[m][n]=='X')countX++;
                    else if(map[m][n]=='T')countT++;
                    else countspot++;
                }
                if(countO==4||countO==3&&countT==1){state=1;goto PRINT;}
                else if(countX==4||countX==3&&countT==1){state=2;goto PRINT;}
                else if(countspot>0)state=-1;
                //else state=0;
            }
            countO=countT=countX=countspot=0;
            for(int m=0,n=0;m<4&&n<4;m++,n++)
            {
                if(map[m][n]=='O')countO++;
                else if(map[m][n]=='X')countX++;
                else if(map[m][n]=='T')countT++;
                else countspot++;
            }
            if(countO==4||countO==3&&countT==1){state=1;goto PRINT;}
            else if(countX==4||countX==3&&countT==1){state=2;goto PRINT;}
            else if(countspot>0)state=-1;
            //else state=0;
            countO=countT=countX=countspot=0;
            for(int m=0,n=3;m<4&&n>=0;m++,n--)
            {
                if(map[m][n]=='O')countO++;
                else if(map[m][n]=='X')countX++;
                else if(map[m][n]=='T')countT++;
                else countspot++;
            }
            if(countO==4||countO==3&&countT==1)state=1;
            else if(countX==4||countX==3&&countT==1)state=2;
            else if(countspot>0)state=-1;
            //else state=0;
            PRINT:
                printf("Case #%d: ",i);
                if(state==1)printf("O won\n");
                else if(state==2)printf("X won\n");
                else if(state==-1)printf("Game has not completed\n");
                else printf("Draw\n");
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
