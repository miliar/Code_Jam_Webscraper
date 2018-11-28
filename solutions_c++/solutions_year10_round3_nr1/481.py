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
struct node{
  int l,r;
};
node a[maxn];
int n;
void init()
{
  int i;
  scanf("%d",&n);
  for (i=1;i<=n;i++)
  {
    scanf("%d%d",&a[i].l,&a[i].r);
  }
}
void work()
{
  int i,j,z=0;
  for (i=1;i<n;i++)
    for (j=i+1;j<=n;j++)
      if ((a[i].l<a[j].l&&a[i].r>a[j].r)||(a[i].l>a[j].l&&a[i].r<a[j].r)) z++;
  printf("%d\n",z);
}
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a.out","w",stdout);
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
