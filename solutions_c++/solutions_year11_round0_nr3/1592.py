#include<string>
#include<algorithm>
#include<cstdlib>
#include<vector>
using namespace std;
const int maxn=1100;
int info[maxn];
int n;
void init()
{
  int i;
  scanf("%d",&n);
  for (i=1;i<=n;i++)
    scanf("%d",&info[i]);
}
void work()
{
  int i,z=0,sum=0,tmin=100000000;
  for (i=1;i<=n;i++)
    z=z^info[i];
  if (z)
  {
    printf("NO\n");
    return;
  }
  for (i=1;i<=n;i++)
  {
    sum+=info[i];
    if (tmin>info[i]) tmin=info[i];
  }
  printf("%d\n",sum-tmin);
}
int main()
{
  freopen("clarge.in","r",stdin);
  freopen("clarge.out","w",stdout);
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
