#include<iostream>
using namespace std;

const int maxn=110;
int a[maxn][maxn],n,m,t;
char c[maxn][maxn];
bool cc;

void init()
{
  scanf("%d%d\n",&n,&m); cc=true;
  for (int i=1;i<=n;i++)
    {
      for (int j=1;j<=m;j++)
        {
          scanf("%c",&c[i][j]);
          a[i][j]=0;
        }
      scanf("\n");
    }
  for (int i=1;i<=n;i++)
    {
      for (int j=1;j<=m;j++)
        {
          if (c[i][j]=='.') continue;
          if (a[i][j]) continue;
          a[i][j]=1; a[i][j+1]=2; a[i+1][j]=2; a[i+1][j+1]=1;
          if ((i+1>n) || (j+1>m) || (c[i][j+1]!='#') || (c[i+1][j]!='#') || (c[i+1][j+1]!='#'))
            { cc=false; break; }
        }
    }
}

int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  scanf("%d",&t);
  for (int tt=1;tt<=t;tt++)
    {
      printf("Case #%d:\n",tt);
      init();
      if (!cc) printf("Impossible\n");
      else {
             for (int i=1;i<=n;i++)
               {
                 for (int j=1;j<=m;j++)
                   if (!a[i][j]) printf(".");
                   else if (a[i][j]==1) printf("/");
                   else printf("\\");
                 printf("\n");
               }
           }
    }
  return 0;
}
