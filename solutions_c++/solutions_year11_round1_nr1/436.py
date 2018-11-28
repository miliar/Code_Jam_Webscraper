#include<string>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<iostream>
using namespace std;
long long n;
int pd,pg;
void init()
{
  cin>>n>>pd>>pg;
}
void work()
{
  if ((pd<100&&pg==100)||(pd>0&&pg==0))
  {
    printf("Broken\n");
    return;
  }
  if (n>=100)
  {
    printf("Possible\n");
    return;
  }
  int i,j;
  for (i=1;i<=n;i++)
    for (j=0;j<=i;j++)
      if (100*j==i*pd)
      {
        printf("Possible\n");
        return;
      }
  printf("Broken\n");
  return;
}
int main()
{
  freopen("al.in","r",stdin);
  freopen("al.out","w",stdout);
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
