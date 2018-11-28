#include<stdio.h>
#include<memory.h>
#include<set>
#include<map>
#include<vector>
#include<string.h>
#include<string>
#include<math.h>
#include<iostream>
using namespace std;


int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};
int i1,n1,L,t;
int g[300][300],heng[300][300],shu[300][300];
char s[20];

bool Judge(int x,int y)
{
    return x>=0&&x<=220&&y>=0&&y<=220;
}

void DFS(int x,int y)
{
    g[x][y]=1;
    int i;
    for(i=0;i<4;i++)
    {
        if(!Judge(x+dx[i],y+dy[i]))
            continue;
        if(g[x+dx[i]][y+dy[i]]==1)
            continue;
        if(i==0)
        {  
            if(heng[x][y+1]==1)
                continue;
        }
        else if(i==1)
        {  
            if(shu[x+1][y]==1)
                continue;
        }
        else if(i==2)
        {  
            if(heng[x][y]==1)
                continue;
        }
        else 
        {  
            if(shu[x][y]==1)
                continue;
        }
        DFS(x+dx[i],y+dy[i]);
    }
}

int x,y,pos,tot,i,j,k,da,xiao;

int main()
{
    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d",&L);
        memset(heng,0,sizeof(heng));
        memset(shu,0,sizeof(shu));        
        x=105;y=105;pos=0;
        for(i=1;i<=L;i++)
        {
            scanf("%s",&s);
            scanf("%d",&t);
            for(j=1;j<=t;j++)
            {
                for(k=0;k<strlen(s);k++)
                {
                    switch(s[k])
                    {
                        case'F':
                            if(pos==0)
                                shu[x][y]=1;
                            else if(pos==1)
                                heng[x][y]=1;
                            else if(pos==2)
                                shu[x][y-1]=1;
                            else 
                                heng[x-1][y]=1;
                            x=x+dx[pos];
                            y=y+dy[pos];
                            break;
                        case'R':
                            pos=(pos+1)%4;
                            break;
                        case'L':
                            pos=(pos+3)%4;
                            break;
                    }
                }
            }
        }
        memset(g,0,sizeof(g));
        DFS(0,0);
        for(i=0;i<=220;i++)
        {
            da=0;xiao=220;
            for(j=0;j<=220;j++)
            {
                if(g[i][j]==0&&j>da)
                    da=j;
                if(g[i][j]==0&&j<xiao)
                    xiao=j;
            }
            for(j=xiao;j<=da;j++)
            {
                if(g[i][j]==1)
                    g[i][j]=2;
            }
        }
        for(j=0;j<=220;j++)
        {
            da=0;xiao=220;
            for(i=0;i<=220;i++)
            {
                if(g[i][j]==0&&i>da)
                    da=i;
                if(g[i][j]==0&&i<xiao)
                    xiao=i;
            }
            for(i=xiao;i<=da;i++)
            {
                if(g[i][j]==1)
                    g[i][j]=2;
            }
        }
        tot=0;
        for(i=0;i<=220;i++)
            for(j=0;j<=220;j++)
                if(g[i][j]==2)
                    tot++;
        printf("Case #%d: %d\n",i1,tot);
    }
    return 0;
}       
