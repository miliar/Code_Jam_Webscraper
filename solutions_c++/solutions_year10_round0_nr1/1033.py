#include<iostream>
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<map>
#include<vector>
const int maxn=50;
using namespace std;
int n,m,cas;
int zt[maxn],info[maxn];
void init()
{
  scanf("%d%d",&n,&m);
}
void work()
{
  int i,j,z=0;
/*  memset(zt,0,sizeof(zt));
  zt[0]=1;
  for (i=1;i<=m+1;i++)
  {
    j=0;
    while (j<n&&zt[j+1])
     j++;
    if (j==n)
    {
      z=i;
      break;
    }
    zt[j+1]=1;
    for (;j;j--)
      zt[j]=0;
  }
  info[n]=z;*/
  info[n]=1<<n;
}
void pre()
{
  int i;
  for (i=1;i<=30;i++)
  {
    n=i;m=200000000;
    work();
  }
}
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a.out","w",stdout);
  int ii;
  pre();
  scanf("%d",&cas);
  for (ii=1;ii<=cas;ii++)
  {
    init();
    printf("Case #%d: ",ii);
    if (m%info[n]==info[n]-1) printf("ON\n");
    else printf("OFF\n");
  }
  return 0;
}
