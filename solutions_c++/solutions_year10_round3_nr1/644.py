#include <stdio.h>
#include <algorithm>
using namespace std;

class wire{
      public:
             long a,b;
};
long n;
wire w[2000];
main()
{
  freopen("A-large.in","r",stdin);
  freopen("file.out","w",stdout);
  long tc,t,cnt,ans,i,j;
  scanf("%d",&tc);
  for(t=1;t<=tc;t++)
  {
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d %d",&w[i].a,&w[i].b);
    ans = 0;
    for(i=0;i<n;i++)
    {
      cnt = 0;
      for(j=i+1;j<n;j++)
        if( (w[i].a < w[j].a && w[i].b > w[j].b) || (w[i].a>w[j].a && w[i].b < w[j].b) )
          cnt++;
      ans += cnt;
    }
    printf("Case #%d: %d\n",t,ans);
  }
}
