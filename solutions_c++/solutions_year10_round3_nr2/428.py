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
int l,r,c,z;
long long ll,rr,cc,tc;
void init()
{
  scanf("%d%d%d",&l,&r,&c);
  z=0;
}
void work()
{
  ll=l;rr=r;
  cc=c;
  if (ll*cc>=rr)
  {
    z=0;
    return;
  }
  z=1;
  cc*=cc;
  while (ll*cc<rr)
  {
    z++;
    cc*=cc;
  }
}
int main()
{
  freopen("B-large.in","r",stdin);
  freopen("b.out","w",stdout);
  int ii,cas;
  scanf("%d",&cas);
  for (ii=1;ii<=cas;ii++)
  {
    init();
    work();
    printf("Case #%d: ",ii);
    printf("%d\n",z);
  }
  return 0;
}
