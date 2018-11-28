#include <stdio.h>
#include <memory.h>
int f[11000],color[11000];
int a[110][110];
int fa(int k)
{
    int i,j,l;
    i=k;
    while (f[i]) i=f[i];
    j=k;
    while (f[j])
    {
        l=f[j];f[j]=i;j=l;
    }
    return i;
}
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Bsmall1.out","w",stdout);
    int x1,y1,x,y,tests,n,m;
    scanf("%d",&tests);
    for (int t0=1;t0<=tests;t0++)
    {
        printf("Case #%d:\n",t0);
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;i++)
          for (int j=1;j<=m;j++)

          {
              scanf("%d",&a[i][j]);
          }
        memset(f,0,sizeof(f));
        for (int i=1;i<=n;i++)
          for (int j=1;j<=m;j++)
          {
              x1=-1;
              for (int k=0;k<4;k++)
              {
                  x=dx[k]+i;y=dy[k]+j;
                  if (x==0||y==0||x>n||y>m) continue;
                  if (a[x][y]>=a[i][j]) continue;

                  if (x1==-1) x1=x,y1=y;
                  else if (a[x][y]<a[x1][y1]) x1=x,y1=y;
              }
              if (x1==-1) continue;
              int p=(i-1)*m+j,q=(x1-1)*m+y1;

              if (fa(p)!=fa(q)) f[fa(p)]=q;
          }
        int now=0;
        memset(color,0,sizeof(color));
        for (int i=1;i<=n;i++)
        {
          for (int j=1;j<=m;j++)
          {
              int k=(i-1)*m+j;
              if (color[fa(k)]==0) color[fa(k)]=++now;
              printf("%c",color[fa(k)]+96);
              if (j!=m) printf(" ");
          }
          printf("\n");
        }

    }
}
