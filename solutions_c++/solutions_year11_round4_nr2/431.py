#include<string>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
using namespace std;
const int maxn=20;
char info[maxn][maxn];
int n,m,d;
void init()
{
  int i,j;
  char t;
  scanf("%d%d%d\n",&n,&m,&d);
  for (i=1;i<=n;i++) 
  {
    for (j=1;j<=m;j++)
      scanf("%c",&info[i][j]);
    scanf("\n");
  }
}
void work()
{
  int i1,j1,k;
  int z=0,i,j;
  int sumi,sumj;
  for (i1=1;i1<=n;i1++)
    for (j1=1;j1<=m;j1++)
      for (k=3;i1+k-1<=n&&j1+k-1<=m;k++)
      {
        if (i1==2&&j1==2&&k==5)
        {
          k++;k--;
        }
        sumi=0;sumj=0;
        for (i=i1;i<=i1+k-1;i++)
          for (j=j1;j<=j1+k-1;j++)
          {
            if (i==i1&&j==j1) continue;
            if (i==i1&&j==j1+k-1) continue;
            if (i==i1+k-1&&j==j1) continue;
            if (i==i1+k-1&&j==j1+k-1) continue;
            sumi+=((i-i1)*2+1-k)*(info[i][j]-'0');
            sumj+=((j-j1)*2+1-k)*(info[i][j]-'0');
          }
        if (sumi==0&&sumj==0&&k>z) 
          z=k;
      }
  if (z==0) printf("IMPOSSIBLE\n");
  else printf("%d\n",z);
}
int main()
{
  freopen("b0.in","r",stdin);
  freopen("b0.out","w",stdout);
  int cas,ii;
  scanf("%d",&cas);
  for (ii=1;ii<=cas;ii++)
  {
    init();
    printf("Case #%d: ",ii);
    work();
  }
  return 0;
}
