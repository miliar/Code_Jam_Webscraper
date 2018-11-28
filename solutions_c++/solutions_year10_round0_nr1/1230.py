/*
 Mahverik
 Using DevCpp 4.9.9.2
 Used input and output redirection instead of file I/O.
 Problem A : Snapper Chain
*/
 
#include<stdio.h>
 
main()
{
 int t,tt; scanf("%d",&tt);
 long long unsigned int n,k;
 for(t=1;t<=tt;t++)
 {
  scanf("%lld %lld",&n,&k); ++k;
  printf("Case #%d: %s\n",t, (k & (-1+(1<<n))) ? "OFF" : "ON" ); 
 }      
}
 
