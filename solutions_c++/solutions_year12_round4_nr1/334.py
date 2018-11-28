#include <iostream>
#include <cstdio>

using namespace std;

long long f[200005]={0};
long a[200005]={0};
long b[200005]={0};

int main()
{
 long t,tt;
 long i,j;
 long n;
 long D;
 
 freopen("1.in","r",stdin);
 freopen("1.out","w",stdout);
 
 scanf("%ld",&t);
 
 for(tt=1;tt<=t;tt++)
   {
    printf("Case #%ld: ",tt);
    scanf("%ld",&n);
    for(i=1;i<=n;i++)
      {
       scanf("%ld%ld",&a[i],&b[i]);
      }
    scanf("%ld",&D);
    f[1]=a[1];
    for(i=2;i<=n;i++)
      {
       f[i]=0;
       for(j=1;j<i;j++)
         if(a[j]+f[j]>=a[i]&&a[i]-a[j]>f[i])
          f[i]=a[i]-a[j];
       if(b[i]<f[i])
        f[i]=b[i];
      }
    for(i=1;i<=n;i++)
      if(a[i]+f[i]>=D)
       {
        printf("YES\n");
        goto loop;
       }
    printf("NO\n");
    loop:;
   }
 
 return 0;
}
