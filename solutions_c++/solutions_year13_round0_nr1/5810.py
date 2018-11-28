#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<iostream>
#include<queue>
#include<set>
using namespace std;
#define PI 2 * acos (0.0)

char G[5][5];
bool X_win()
{
    int i,j,c;
    for(i=0;i<4;i++)
    {
        c=0;
        for(j=0;j<4;j++)
        {
            if(G[i][j]=='X'||G[i][j]=='T')
                c++;
        }
        if(c==4)
            return true;
    }

    for(i=0;i<4;i++)
    {
        c=0;
        for(j=0;j<4;j++)
        {
            if(G[j][i]=='X'||G[j][i]=='T')
                c++;
        }
        if(c==4)
            return true;
    }
    c=0;
    for(i=0,j=0;i<4;i++,j++)
    {
        if(G[i][j]=='X'||G[i][j]=='T')
                c++;
    }
    if(c==4)
            return true;

    c=0;
    for(i=0,j=3;i<4;i++,j--)
    {
        if(G[i][j]=='X'||G[i][j]=='T')
                c++;
    }
    if(c==4)
            return true;

    return false;
}

bool O_win()
{
    int i,j,c;
    for(i=0;i<4;i++)
    {
        c=0;
        for(j=0;j<4;j++)
        {
            if(G[i][j]=='O'||G[i][j]=='T')
                c++;
        }
        if(c==4)
            return true;
    }

    for(i=0;i<4;i++)
    {
        c=0;
        for(j=0;j<4;j++)
        {
            if(G[j][i]=='O'||G[j][i]=='T')
                c++;
        }
        if(c==4)
            return true;
    }
    c=0;
    for(i=0,j=0;i<4;i++,j++)
    {
        if(G[i][j]=='O'||G[i][j]=='T')
                c++;
    }
    if(c==4)
            return true;

    c=0;
    for(i=0,j=3;i<4;i++,j--)
    {
        if(G[i][j]=='O'||G[i][j]=='T')
                c++;
    }
    if(c==4)
            return true;

    return false;
}

bool Draw()
{
    int i,j,c=0;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        if(G[i][j]!='.')
        c++;
    if(c==16)
        return true;
    return false;
}
int main()
{
    freopen("C:\\Users\\talha\\Desktop\\A-large.in","r",stdin);
    freopen("C:\\Users\\talha\\Desktop\\A-large.out","w",stdout);
    int i,tc,t=1;
    scanf("%d",&tc);
    while(tc--)
    {
        for(i=0;i<4;i++)
        {
            scanf("%s",G[i]);
        }
        if(X_win())
            printf("Case #%d: X won\n",t++);
        else if(O_win())
            printf("Case #%d: O won\n",t++);
        else if(Draw())
            printf("Case #%d: Draw\n",t++);
        else
        printf("Case #%d: Game has not completed\n",t++);
    }
    return 0;
}
