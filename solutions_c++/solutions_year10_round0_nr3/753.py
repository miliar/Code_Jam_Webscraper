#include <stdio.h>
int it,t,i,j,n,r,k,sum;
long long s;
int a[5000],b[5000],raod[5000];
int main()
{
freopen("C-large.in","r",stdin);
freopen("C-large.out","w",stdout);
scanf("%d",&t);
for(it=1;it<=t;it++)
   {
   printf("Case #%d: ",it);
   scanf("%d %d %d",&r,&k,&n);
   for(i=0;i<n;i++)
      scanf("%d",&a[i]);
   for(i=n;i<(n<<1);i++)
      a[i]=a[i-n];
   for(s=i=0;i<n;i++)
      s+=(long long)a[i];
   if(s<=k)
      {
      printf("%lld\n",(long long)s*(long long)r);
      continue;
      }
   for(i=0;i<n;i++)
      for(b[i]=i,sum=0,j=i;;j++)
         if((sum+=a[j])>k)
            {
            b[i]=j;
            raod[i]=sum-a[j];
            break;
            }
   for(j=0,s=0,i=0;i<r;i++)
      {
      s+=(long long)raod[j];
      j=b[j]%n;
      }
   printf("%lld\n",s);
   }
return 0;
}
