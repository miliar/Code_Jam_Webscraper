#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int H,W;
int A[101][101];
char S[101][101];
char lab;
const int fx[]={-1,0,0,1};
const int fy[]={0,-1,1,0};
bool IN(int x,int y)
{
     return x>0&&y>0&&x<=H&&y<=W;
}
void Sink(int x,int y,int &sx,int &sy)
{
     S[x][y]=lab;
     int bi,b=-1;
     for (int i=0;i<4;i++)
     {
         int nx=x+fx[i],ny=y+fy[i];
         if (IN(nx,ny)&&S[nx][ny]==0)
         {
            int t=10*A[nx][ny]+i;
            if (b>t||b==-1)
            {
               if (A[nx][ny]<A[x][y])
               {
                  b=t;
                  bi=i;
               }
            }
         }
     }
     if (b==-1)
     {
        sx=x;
        sy=y;
     }
     else
         Sink(x+fx[bi],y+fy[bi],sx,sy);
}
bool Check(int tx,int ty,int x,int y)
{
     int bi,b=-1;
     for (int i=0;i<4;i++)
     {
         int nx=x+fx[i],ny=y+fy[i];
         if (IN(nx,ny))
         {
            int t=10*A[nx][ny]+i;
            if (b>t||b==-1)
            {
               if (A[nx][ny]<A[x][y])
               {
                  b=t;
                  bi=i;
               }
            }
         }
     }
     if (b==-1) return false;
     return tx==x+fx[bi]&&ty==y+fy[bi];
}
void DFS(int x,int y)
{
     S[x][y]=lab;
     for (int i=0;i<4;i++)
     {
         int nx=x+fx[i],ny=y+fy[i];
         if (IN(nx,ny)&&(S[nx][ny]==0||S[nx][ny]==S[x][y]))
            if (Check(x,y,nx,ny))
               DFS(nx,ny);
     }
}
int main()
{
    //freopen("a.txt","r",stdin);
    //freopen("b.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++)
    {
        memset(S,0,sizeof(S));
        scanf("%d%d",&H,&W);
        for (int i=1;i<=H;i++)
            for (int j=1;j<=W;j++)
                scanf("%d",&A[i][j]);
        lab='a'-1;
        for (int i=1;i<=H;i++)
            for (int j=1;j<=W;j++)
                if (S[i][j]==0)
                {
                   lab++;
                   int sx,sy;
                   Sink(i,j,sx,sy);
                   DFS(sx,sy);
                }
        printf("Case #%d:\n",Case);
        for (int i=1;i<=H;i++)
        {
            for (int j=1;j<W;j++)
                printf("%c ",S[i][j]);
            printf("%c\n",S[i][W]);
        }
    }
    return 0;
}
