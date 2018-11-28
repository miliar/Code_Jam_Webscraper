/*
 Mahverik
 Using DevCpp 4.9.9.2
 Used input and output redirection instead of file I/O.
 Problem C : Theme Park
*/
 
#include<stdio.h>
 
main()
{
 int t,tt; scanf("%d",&tt);
 unsigned long long int r,k,sum,temp; int n,i,j,q; int a[1000]; 
 for(t=1;t<=tt;t++,sum=0)
 {
  scanf("%lld %lld %d",&r,&k,&n);
  for(i=0;i<n;i++) { scanf("%d",a+i); }
  temp=0;
  for(i=j=0;i<r;i++)
  {
   for(temp=0,q=j;temp+a[j]<=k;) { /*printf("%d,",a[j]);*/ temp+=a[j]; j=(j+1)%n; if(q==j) break; } sum+=temp; //printf("\n");
  }
  printf("Case #%d: %lld\n",t,sum);
 }      
}
 
