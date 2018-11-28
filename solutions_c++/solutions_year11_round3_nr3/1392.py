#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int main()
{
  freopen("ac4.in","r",stdin);
  freopen("ac4.out","w",stdout);
  int t,to=0;
  scanf("%d",&t);
  while(t--)
  {
    to++;
    printf("Case #%d: ",to);
    int n;
    long long l,h;
    scanf("%d%lld%lld",&n,&l,&h);
    int i;
    long long a[10100]={0};
    for(i=0;i<n;i++)
      scanf("%lld",&a[i]);
    sort(a,&a[n]);
    if(l==1)
    {
      printf("1\n");
    }
    else
    {
      bool ok=0;
      long long j;
      for(j=l;j<=h;j++)
      {
        ok=0;
        for(i=0;i<n;i++)
        {
          if((a[i]%j!=0)&&(j%a[i]!=0)) {ok=1;break;}
        }
        if(ok==0)
        {
          printf("%lld\n",j);
          break;
        }
      }
      if(ok==1) printf("NO\n");
    }
  }
  return 0;
}
