#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

class pnt
{
    public:
        int x; int y;
};

int T,H,W,i,j,k,Q,p,i2,j2;
int a[111][111],l[111][111];
pnt dir[4];
char c[111][111],z;

void dfs(int x, int y)
{
    int d,k,v;
    if(l[x][y]==0) l[x][y]=p;
    v=200000; d=-1;
    for(k=0;k<4;k++)
        if(a[x+dir[k].x][y+dir[k].y]<v && a[x+dir[k].x][y+dir[k].y]<a[x][y])
        {
            v=a[x+dir[k].x][y+dir[k].y];
            d=k;
        }
    if(d!=-1)
    {
        dfs(x+dir[d].x,y+dir[d].y);
        l[x][y]=l[x+dir[d].x][y+dir[d].y];
    }
}

main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    dir[0].x=-1; dir[1].x=0; dir[2].x=0; dir[3].x=1;
    dir[0].y=0; dir[1].y=-1; dir[2].y=1; dir[3].y=0;
    scanf("%d",&T);
    for(Q=1;Q<=T;Q++)
    {
        scanf("%d%d",&H,&W);
        memset(a,200000,sizeof(a));
        memset(l,0,sizeof(l));
        p=0;
        for(i=1;i<=H;i++)
            for(j=1;j<=W;j++)
                scanf("%d",&a[i][j]);
        for(i=1;i<=H;i++)
            for(j=1;j<=W;j++)
                if(l[i][j]==0) { p++; dfs(i,j); }
        z='a';
        for(i=1;i<=H;i++)
            for(j=1;j<=W;j++)
                if(l[i][j]!=0)
                {
                    k=l[i][j];
                    for(i2=1;i2<=H;i2++)
                        for(j2=1;j2<=W;j2++)
                            if(l[i2][j2]==k) { l[i2][j2]=0; c[i2][j2]=z; }
                    z++;
                }
        printf("Case #%d:\n",Q);
        for(i=1;i<=H;i++)
        {
            for(j=1;j<W;j++)
                printf("%c ",c[i][j]);
            printf("%c\n",c[i][W]);
        }
    }
}
