
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char str[4][10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int dot;
    char c,flag;
    int ti,tc,i,j,k;
    scanf("%d",&tc);
    for(ti=1; ti<=tc; ti++)
    {
        flag=0;
        dot=0;
        for(i=0; i<4; i++)
        {
            scanf("%s",str[i]);
            for(j=0;j<4;j++)
            {
                if(str[i][j]=='.')dot=1;
            }
        }
        for(i=0; i<4; i++)
        {
            if(str[i][0]=='T')c=str[i][1];
            else c=str[i][0];
            for(j=1; j<4; j++)
            {
                if(c=='.'||str[i][j]!=c&&str[i][j]!='T')break;
            }
            if(j>=4)
            {
                break;
            }
        }
        if(i<4)flag=c;
        if(flag==0)
        {
            for(i=0; i<4; i++)
            {
                if(str[0][i]=='T')c=str[1][i];
                else c=str[0][i];
                for(j=1; j<4; j++)
                {
                    if(c=='.'||str[j][i]!=c&&str[j][i]!='T')break;
                }
                if(j>=4)
                {
                    break;
                }
            }
            if(i<4)flag=c;
        }
        if(flag==0)
        {
            if(str[0][0]=='T')c=str[1][1];
            else c=str[0][0];
            for(i=0; i<4; i++)
            {
                if(c=='.'||str[i][i]!=c&&str[i][i]!='T')break;
            }
            if(i>=4)flag=c;
        }
        if(flag==0)
        {
            if(str[3][0]=='T')c=str[2][1];
            else c=str[3][0];
            for(i=0; i<4; i++)
            {
                if(c=='.'||str[i][3-i]!=c&&str[i][3-i]!='T')break;
            }
            if(i>=4)flag=c;
        }
        printf("Case #%d: ",ti);
        if(flag)
        {
            printf("%c won\n",flag);
        }
        else
        {
            if(dot)printf("Game has not completed\n");
            else printf("Draw\n");
        }
    }
    return 0;
}
