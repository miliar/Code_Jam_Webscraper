#include <stdio.h>

long long sum;
long j,k,tn,t,v1[1000],v2[1000],n,i;
void swap(long *r1,long *r2)
{long r3;
 r3=*r1; 
 *r1=*r2; 
 *r2=r3;
}
main()
{
 freopen("first.in","r",stdin);
 freopen("first.out","w",stdout);
 scanf("%d",&tn);
 for(t=0;t<tn;t++)
 {
   scanf("%d",&n);
   sum=0;
   for(k=0;k<n;k++)
   scanf("%d",&v1[k]);
   for(k=0;k<n;k++)
   scanf("%d",&v2[k]);
   for(k=0;k<n;k++)
   for(j=0;j<n-1;j++)
   if (v1[j]>v1[j+1]) swap(&v1[j],&v1[j+1]);
   for(k=0;k<n;k++)
   for(j=0;j<n-1;j++)
   if (v2[j]<v2[j+1]) swap(&v2[j],&v2[j+1]);
   for(k=0;k<n;k++)
   sum+=v1[k]*v2[k];
   printf("Case #%d: %d\n",t+1,sum);
 }
}
