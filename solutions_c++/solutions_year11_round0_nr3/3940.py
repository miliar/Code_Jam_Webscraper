#include<stdio.h>

int main()
{
    freopen("C-large.in","r",stdin);
  freopen("cL.out","w",stdout);
 long t,n,cas=1,a[20000],i,min,sum,sumz;
 scanf("%ld",&t);
 while(t--)
 {
  scanf("%ld",&n);
  min=100000000;
  sum=0;
  sumz=0;
  for(i=0;i<n;i++) {
                   scanf("%ld",&a[i]);
                   sum=sum^a[i];
                   sumz+=a[i];
                   if(a[i]<min) min=a[i];
                   }
  if(sum!=0)
  {
   printf("Case #%ld: NO\n",cas++);
  }
  else
  {
   printf("Case #%ld: %ld\n",cas++,sumz-min);
  }
 }
 return 0;
}
