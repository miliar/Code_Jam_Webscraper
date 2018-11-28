#include<iostream>
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<map>
#include<vector>
using namespace std;
const int maxn=200;
int info[2][maxn][maxn];
int n,m,tt;
void init()
{
  int t,x1,y1,x2,y2,i,j;
  tt=0;
  memset(info,0,sizeof(info));
  scanf("%d",&t);
  n=0;m=0;
  for (;t;t--)
  {
    scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
    for (i=x1;i<=x2;i++)
      for (j=y1;j<=y2;j++)
        info[0][i][j]=1;
    n=max(n,x2);
    m=max(m,y2);
  }
}
int notempty()
{
  int i,j;
  for (i=1;i<=n;i++)
    for (j=1;j<=m;j++)
      if (info[tt][i][j]) return 1;
  return 0;
}
void work()
{
  int z=0,i,j;
  while (notempty())
  {
    z++;
    tt=1-tt;
    for (i=1;i<=n;i++)
      for (j=1;j<=m;j++)
      {
        info[tt][i][j]=info[1-tt][i][j];
        if (info[1-tt][i][j-1]==0&&info[1-tt][i-1][j]==0) info[tt][i][j]=0;
        if (info[1-tt][i][j-1]&&info[1-tt][i-1][j]) info[tt][i][j]=1;
      }
  }
  printf("%d\n",z);
}
int main()
{
  freopen("C-small-attempt1.in","r",stdin);
  freopen("c.out","w",stdout);
  int ii,cas;
  scanf("%d",&cas);
  for (ii=1;ii<=cas;ii++)
  {
    init();
    printf("Case #%d: ",ii);
    work();
  }
  return 0;
}
