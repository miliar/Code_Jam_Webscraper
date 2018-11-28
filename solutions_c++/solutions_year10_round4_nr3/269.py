#include <cstdio>
#include <iostream>
#include <cstring>
#define MAXN 100
using namespace std;

int g[MAXN+1][MAXN+1],h[MAXN+1][MAXN+1];
int r;

void update()
{
    int i,j;
    for(i=1;i<=MAXN;i++)
    {
        for(j=1;j<=MAXN;j++)
        {
            if(g[i][j]==1)
            {
                h[i][j]=g[i-1][j]|g[i][j-1];
            }
            else
            {
                h[i][j]=g[i-1][j]&g[i][j-1];
            }
        }
    }
    memcpy(g,h,sizeof(g));
}

int check()
{
    int i,j;
    for(i=1;i<=MAXN;i++)
    {
        for(j=1;j<=MAXN;j++)
        {
            if(g[i][j]==1)
            {
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int i,c,t,x,y,x1,y1,x2,y2,step;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        memset(g,0,sizeof(g));
        scanf("%d",&r);
        for(i=0;i<r;i++)
        {
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            for(x=x1;x<=x2;x++)
            {
                for(y=y1;y<=y2;y++)
                {
                    g[x][y]=1;
                }
            }
        }
        for(step=0;check()==1;step++)
        {
            update();
        }
        printf("Case #%d: %d\n",c+1,step);
    }
    return 0;
}
