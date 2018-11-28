#include<string>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
using namespace std;
const int maxn=1100;
int shi[maxn],su[maxn];
int n,s;
int geshu[maxn];
int call;
void qiusu()
{
  int i,j;
  for (i=2;i<maxn;i++)
    shi[i]=1;
  for (i=2;i<maxn;i++)
    if (shi[i])
      for (j=i;i*j<maxn;j++)
        shi[i*j]=0;
  s=0;
  for (i=2;i<maxn;i++)
    if (shi[i]) su[++s]=i;
}
void init()
{
  scanf("%d",&n);
}
void inse(int ii)
{
  int i,t;
  int temp=0;
  for (i=1;i<=s;i++)
  {
    if (su[i]>ii) break;
    t=0;
    while (ii%su[i]==0)
    {
      t++;
      ii=ii/su[i];
    }
    if (geshu[i]<t)
    {
      temp=1;
      geshu[i]=t;
    }
  }
  call+=temp;
}
int manzu(int t1,int t2)
{
  int temp=1;
  while (t2)
  {
    temp*=t1;
    if (temp>n) return 0;
    t2--;
  }
  return 1;
}
int mi(int t1,int t2)
{
  int temp=1;
  while (t2)
  {
    temp*=t1;
    t2--;
  }
  return temp;
}
void work()
{
  int i,t1,ii;
  call=1;
  memset(geshu,0,sizeof(geshu));
  for (ii=1;ii<=10;ii++)
  {
    for (i=1;i<=s;i++)
      if (manzu(su[i],ii)) inse(mi(su[i],ii));
  }
  t1=call;
  if (n==1) call=1;
  else call=0;
  memset(geshu,0,sizeof(geshu));
  for (ii=10;ii>=1;ii--)
  {
    for (i=1;i<=s;i++)
      if (manzu(su[i],ii)) inse(mi(su[i],ii));
  }
  printf("%d\n",t1-call);
}
int main()
{
  freopen("c2.in","r",stdin);
  freopen("c2.out","w",stdout);
  int cas,ii;
  qiusu();
  scanf("%d",&cas);
  for (ii=1;ii<=cas;ii++)
  {
    init();
    printf("Case #%d: ",ii);
    work();
  }
  return 0;
}
