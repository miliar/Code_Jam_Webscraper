#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int t,T,a1[1002][2][4],a2[1002][2][4],x1[1002][2],x2[1002][2],co,win;
char c[6][6];

int main(){
    int i,j;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        for(i=0;i<4;i++)
        {
            scanf("%s",c[i]);
        }
        co=0;
        win=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(c[i][j]=='O')
                {
                    a1[t][0][i]++;
                    a2[t][0][j]++;
                    if(i==j)x1[t][0]++;
                    if(i+j==3)x2[t][0]++;
                    co++;
                }else if(c[i][j]=='X'){
                    a1[t][1][i]++;
                    a2[t][1][j]++;
                    if(i==j)x1[t][1]++;
                    if(i+j==3)x2[t][1]++;
                    co++;
                }else if(c[i][j]=='T'){
                    a1[t][0][i]++;
                    a2[t][0][j]++;
                    if(i==j)x1[t][0]++;
                    if(i+j==3)x2[t][0]++;
                    a1[t][1][i]++;
                    a2[t][1][j]++;
                    if(i==j)x1[t][1]++;
                    if(i+j==3)x2[t][1]++;
                    co++;
                }
            }
        }
        for(i=0;i<4;i++)
        {
            if(a1[t][0][i]==4)win=1;
            else if(a2[t][0][i]==4)win=1;
            else if(a1[t][1][i]==4)win=2;
            else if(a2[t][1][i]==4)win=2;
            else if(x1[t][0]==4)win=1;
            else if(x2[t][0]==4)win=1;
            else if(x1[t][1]==4)win=2;
            else if(x2[t][1]==4)win=2;
        }
        printf("Case #%d: ",t);
        if(win==1)printf("O won\n");
        else if(win==2)printf("X won\n");
        else{
            if(co==16)printf("Draw\n");
            else printf("Game has not completed\n");
        }
    }
    
    scanf(" ");
    return 0;
}
