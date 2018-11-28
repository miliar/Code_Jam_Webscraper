#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
long long b[1001],c[1001],g[1001],d[1001],sum[1001],a[1001];
int main()
{
    long long cas,n,r,q,w,k,i,j;
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%lld",&cas);
    for (j=1;j<=cas;j++)
    {
          scanf("%lld%lld%lld",&r,&k,&n);
          memset(b,0,sizeof(b));
          for (i=0;i<n;i++)
          scanf("%lld",&a[i]);
          long long last=0;
          sum[0]=a[0];
          for (i=1;i<n;i++)
          sum[i]=sum[i-1]+a[i];
          if (sum[n-1]<=k)
          {
             printf("Case #%lld: %lld\n",j,r*sum[n-1]);
             continue;
          }
          long long nono=r;
          long long f=0;
          long long can=0;
          for (i=1;i<=r;i++)
          {
              long long ss=0;
              ss=a[last];
              while (ss<=k)
              {
                 last=(last+1)%n;
                 ss+=a[last];
              }
              ss-=a[last];
       //       cout<<ss<<endl;
              can+=ss;
              if (b[(last+n-1)%n]==0)
              {
                 b[(last+n-1)%n]=can;
                 f=can;
                 c[(last+n-1)%n]=i;
                 d[(last+n-1)%n]=ss;
              }
              else
              {
                  nono=c[(last+n-1)%n]+(r-c[(last+n-1)%n])/(i-c[(last+n-1)%n])*(i-c[(last+n-1)%n]);
                  f=(can-b[(last+n-1)%n])*((r-c[(last+n-1)%n])/(i-c[(last+n-1)%n]))+b[(last+n-1)%n];
                  break;
              }
             
          }
          for (i=nono+1;i<=r;i++)
          {
              long long ss=0;
              ss=a[last];
              while (ss<=k)
              {
                 last=(last+1)%n;
                 ss+=a[last];
              }
              ss-=a[last];
              f+=ss;
          }
          printf("Case #%lld: %lld\n",j,f);
    }
}
    
    
