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
const int maxn=1100;
int n;
int info[maxn];
void init()
{
  scanf("%d",&n);
  for (int i=1;i<=n;i++)
    scanf("%d",&info[i]);
}
int gcd(int t1,int t2)
{
  if (t1<t2) return gcd(t2,t1);
  if (t1%t2) return gcd(t2,t1%t2);
  return t2;
}
void work()
{
  int i,j,z;
  for (i=1;i<=n;i++)
    for (j=i+1;j<=n;j++)
      if (info[i]!=info[j]) z=abs(info[i]-info[j]);
  for (i=1;i<=n;i++)
    for (j=i+1;j<=n;j++)
      if (info[i]!=info[j]) z=gcd(z,abs(info[i]-info[j]));
  if (info[1]%z==0) printf("%d\n",0);
  else printf("%d\n",z-info[1]%z);
}
int main()
{
  freopen("B-small-attempt1.in","r",stdin);
  freopen("b.out","w",stdout);
  int cas;
  scanf("%d",&cas);
  for (int ii=1;ii<=cas;ii++)
  {
    init();
    printf("Case #%d: ",ii);
    work();
  }
  return 0;
}
