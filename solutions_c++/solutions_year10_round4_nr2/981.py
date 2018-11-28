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
const int maxn=2000;
int mis[maxn],yy[maxn],gc[20],cost[maxn],er[20];
int p,n;
void qiuer()
{
  int i;
  er[0]=1;
  for (i=1;i<=13;i++)
    er[i]=er[i-1]*2;
}
void init()
{
  int i,j,t;
  memset(yy,0,sizeof(yy));
  scanf("%d",&p);
  n=(1<<p);
  for (i=1;i<=n;i++)
    scanf("%d",&mis[i]);
  for (i=p-1;i>=0;i--)
  {
    t=er[i]-1;
    for (j=1;j<=er[i];j++)
      scanf("%d",&cost[t+j]);
  }
}
void work()
{
  int i,t,j,z=0;
  for (i=1;i<=n;i++)
  {
    t=(i+1)/2+er[p-1]-1;
    for (j=p;j;j--)
    {
      gc[j]=t;
      t/=2;
    }
    for (j=1;j+mis[i]<=p;j++)
      if (yy[gc[j]]==0)
      {
        yy[gc[j]]=1;
        z+=cost[gc[j]];
      }
  }
  printf("%d\n",z);
}   
int main()
{
  qiuer();
  freopen("B-small-attempt0.in","r",stdin);
  freopen("b.out","w",stdout);
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
