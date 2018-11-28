#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,i,j,k,cnt;
    char m[5][5];
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++)
    {
        for(i=0;i<4;i++)
            scanf("%s",m[i]);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                if(m[i][j]=='.'||m[i][j]=='O')
                    break;
            if(j==4) break;
            for(j=0;j<4;j++)
                if(m[j][i]=='.'||m[j][i]=='O')
                    break;
            if(j==4) break;
        }
        if(i<4)
        {
            printf("Case #%d: X won\n",cnt);
            continue;
        }
        for(i=0;i<4;i++)
            if(m[i][i]=='.'||m[i][i]=='O')
                break;
        if(i==4)
        {
            printf("Case #%d: X won\n",cnt);
            continue;
        }
        for(i=0;i<4;i++)
            if(m[i][3-i]=='.'||m[i][3-i]=='O')
                break;
        if(i==4)
        {
            printf("Case #%d: X won\n",cnt);
            continue;
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                if(m[i][j]=='.'||m[i][j]=='X')
                    break;
            if(j==4) break;
            for(j=0;j<4;j++)
                if(m[j][i]=='.'||m[j][i]=='X')
                    break;
            if(j==4) break;
        }
        if(i<4)
        {
            printf("Case #%d: O won\n",cnt);
            continue;
        }
        for(i=0;i<4;i++)
            if(m[i][i]=='.'||m[i][i]=='X')
                break;
        if(i==4)
        {
            printf("Case #%d: O won\n",cnt);
            continue;
        }
        for(i=0;i<4;i++)
            if(m[i][3-i]=='.'||m[i][3-i]=='X')
                break;
        if(i==4)
        {
            printf("Case #%d: O won\n",cnt);
            continue;
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                if(m[i][j]=='.')
                    break;
            if(j<4) break;
        }
        if(i<4) printf("Case #%d: Game has not completed\n",cnt);
        else printf("Case #%d: Draw\n",cnt);
    }
}
