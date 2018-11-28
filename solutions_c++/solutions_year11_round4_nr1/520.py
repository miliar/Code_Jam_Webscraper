#include<string>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
using namespace std;
const int maxn=11000;
int w,r,t,n;
double x;
double info[maxn][3];
int ci[maxn];
void init()
{
  int i;
  scanf("%lf%d%d%d%d",&x,&w,&r,&t,&n);
  for (i=1;i<=n;i++)
  {
    scanf("%lf%lf%lf",&info[i][0],&info[i][1],&info[i][2]);
    ci[i]=i;
  }
}
int cmp(int t1,int t2)
{
  return info[t1][2]<info[t2][2];
}
void work()
{
  int i;
  sort(ci+1,ci+n+1,cmp);
  double left=t;
  double z=0;
  for (i=1;i<=n;i++)
    x=x-(info[i][1]-info[i][0]);
  if (x/r>left)
  {
    z=z+left+(x-left*r)/w;
    left=0;
  }
  else 
  {
    z=z+x/r;
    left-=x/r;
  }
  for (i=1;i<=n;i++)
  {
    x=x-(info[ci[i]][1]-info[ci[i]][0]);
    if ((info[ci[i]][1]-info[ci[i]][0])/(r+info[ci[i]][2])>left)
    {
      z=z+left+(info[ci[i]][1]-info[ci[i]][0]-left*(r+info[ci[i]][2]))/(w+info[ci[i]][2]);
      left=0;
    }
    else
    {
      z=z+(info[ci[i]][1]-info[ci[i]][0])/(r+info[ci[i]][2]);
      left-=(info[ci[i]][1]-info[ci[i]][0])/(r+info[ci[i]][2]);
    }
  }

  printf("%.10lf\n",z);
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
