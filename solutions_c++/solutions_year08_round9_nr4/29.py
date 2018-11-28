#include<iostream>
using namespace std;
const int maxn=50;
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};
int ans,sx,sy,n,m,g[maxn][maxn],u[maxn][maxn],v[maxn][maxn],d[maxn][maxn],test,t,qx[maxn*maxn],qy[maxn*maxn],p[maxn][maxn][2];
void init()
{
     int i,j;
     char ch;
     scanf("%d%d\n",&n,&m);
     memset(g,0,sizeof(g));
     for (i=0;i<n;i++)
     {
         for (j=0;j<m;j++)
         {
             scanf("%c",&ch);
             if (ch!='.')
             {
                g[i][j]=1;
                if (ch=='T')
                {
                   sx=i;
                   sy=j;
                }
             }
         }
         scanf("\n");
     }
}

int outside(int x1,int y1)
{
    if (x1<0) return 1;
    if (y1<0) return 1;
    if (x1>=n) return 1;
    if (y1>=m) return 1;
    return 0;
}

void bfs(int x1,int y1)
{
     memset(v,-1,sizeof(v));
     int h,t,i,j,xx,yy;
     h=0;
     t=1;
     qx[1]=x1;
     qy[1]=y1;
     v[x1][y1]=0;
     for (;h<t;)
     {
         h++;
         for (i=0;i<4;i++)
         {
             xx=qx[h]+dx[i];
             yy=qy[h]+dy[i];
             if (outside(xx,yy)) continue;
             if (!g[xx][yy]) continue;
             if (v[xx][yy]!=-1) continue;
             t++;
             qx[t]=xx;
             qy[t]=yy;
             v[xx][yy]=v[qx[h]][qy[h]]+1;
             p[xx][yy][0]=qx[h];
             p[xx][yy][1]=qy[h];
         }
     }
     for (i=0;i<n;i++)
         for (j=0;j<m;j++)
         if (v[i][j]!=-1)
            if ((d[i][j]==-1)||(v[i][j]<d[i][j])) d[i][j]=v[i][j];
}

void go(int x1,int y1)
{
     u[x1][y1]=1;
     ans+=v[x1][y1];
     if ((!x1)&&(!y1)) return;     
     go(p[x1][y1][0],p[x1][y1][1]);
}

void work()
{
     ans=0;
     int i,j;
     memset(d,-1,sizeof(d));
     bfs(0,0);
     memset(u,0,sizeof(u));
     if (sx+sy!=0)
     {
        go(sx,sy);
        bfs(sx,sy);
     }     
     for (i=0;i<n;i++)
         for (j=0;j<m;j++)
         if ((g[i][j])&&(!u[i][j])) ans+=d[i][j];
}

void print()
{
     printf("Case #%d: %d\n",t,ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d\n",&test),t=1;t<=test;t++)
    {
        init();
        work();
        print();
    }
    return 0;
}
