#include<cstdio>
#include<algorithm>
using namespace std;
const int maxn=100+10;
const int movex[4]={-1,0,0,1};
const int movey[4]={0,-1,1,0};
int n,m,g[maxn][maxn],p[maxn][maxn],tot;
void init()
{
    scanf("%d%d",&n,&m);
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++)
            scanf("%d",&g[i][j]);
}
void fill(int sx,int sy)
{
    int t=-1,x=sx,y=sy;
    while (true)
    {
        if (p[x][y]>=0)
        {
            t=p[x][y];
            break;
        }
        int xx,yy,x0,y0,h=g[x][y];
        for (int i=0;i<4;i++)
        {
            xx=x+movex[i];
            yy=y+movey[i];
            if (xx>=0 && xx<n && yy>=0 && yy<m && g[xx][yy]<h)
                h=g[x0=xx][y0=yy];
        }
        if (h==g[x][y])
            break;
        x=x0;
        y=y0;
    }
    if (t==-1)
        t=tot++;
    x=sx;
    y=sy;
    while (true)
    {
        int xx,yy,x0,y0,h=g[x][y];
        p[x][y]=t;
        for (int i=0;i<4;i++)
        {
            xx=x+movex[i];
            yy=y+movey[i];
            if (xx>=0 && xx<n && yy>=0 && yy<m && g[xx][yy]<h)
                h=g[x0=xx][y0=yy];
        }
        if (h==g[x][y])
            return;
        x=x0;
        y=y0;
    }
}
void solve()
{
    memset(p,-1,sizeof(p));
    tot=0;
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++)
            if (p[i][j]==-1)
                fill(i,j);
}
void out(int test)
{
    printf("Case #%d:\n",test);
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
            printf("%c ",(char)(p[i][j]+'a'));
        printf("\n");
    }
}
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        init();
        solve();
        out(i);
    }
    return 0;
}
