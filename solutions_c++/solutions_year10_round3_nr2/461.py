#include <stdio.h>
int main()
{
    long long t,l,p,c;
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    scanf("%lld",&t);
    for (long long ii=1;ii<=t;ii++)
    {
          scanf("%lld%lld%lld",&l,&p,&c);
          long long cnt=0;
          while (l<p)
          {
              l=l*c;
              cnt++;
          }  
          cnt--;
          long long sum=0;
          while (cnt!=0)
          {
                cnt/=2;
                sum++;
          }
          printf("Case #%lld: %lld\n",ii,sum);
    }
    return 0;
}
