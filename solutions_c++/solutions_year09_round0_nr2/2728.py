#include<stdio.h>
#include<iostream>
#include<queue>
#include<map>
#include<vector>
#include<string>
#include<sstream>
#include<queue>
#include<math.h>
#include<algorithm>
#define _clr(x) memset(x,-1,sizeof(x))
#define clr(x) memset(x,0,sizeof(x))
#define pb push_back
#define M 1001
using namespace std;
int d[4][2]={-1,0,0,-1,0,1,1,0};
struct ft
{
    int x,y;
    ft(){}
    ft(int x,int y):x(x),y(y){}
};
int sign;
int v[200][200],g[200][200];
class prio
{
    public:
    bool operator ()(const ft &a,const ft &b)
    {
        return g[a.x][a.y]<g[b.x][b.y];
    }
};
int h,w;
int dfs(int x,int y)
{
    if(v[x][y])return v[x][y];
    int t=g[x][y],wx,wy;
    for(int i=0;i<4;i++)
    {
        int tx=x+d[i][0];
        int ty=y+d[i][1];
        if(tx>=0&&tx<h&&ty>=0&&ty<w&&g[tx][ty]<t)
        {
            t=g[tx][ty];
            wx=tx;wy=ty;
        }
    }
    if(t==g[x][y])
    {
        v[x][y]=sign++;
		return v[x][y];
    }
    return v[x][y]=dfs(wx,wy);
}
char ans[200][200];
int is[200*200];
int main()
{
    freopen("in.txt","r",stdin);
    //freopen("in.in","r",stdin);
    freopen("in.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        priority_queue<ft,vector<ft>,prio>q;

        scanf("%d%d",&h,&w);
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
            {
                scanf("%d",&g[i][j]);
                q.push(ft(i,j));
            }
        }
        memset(v,0,sizeof(v));
        sign=1;
        while(!q.empty())
        {
            int x=q.top().x;
            int y=q.top().y;
            q.pop();
            if(v[x][y])continue;
            v[x][y]=dfs(x,y);
        }
        memset(is,0,sizeof(is));
        int k=1;
        for(int i=0;i<h;i++)
            for(int j=0;j<w;j++)
            {
                if(!is[v[i][j]])
                    is[v[i][j]]=k++;
                ans[i][j]=is[v[i][j]]-1+'a';
            }
        printf("Case #%d:\n",++ca);
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
                printf("%c ",ans[i][j]);
            printf("\n");
        }
    }
}
