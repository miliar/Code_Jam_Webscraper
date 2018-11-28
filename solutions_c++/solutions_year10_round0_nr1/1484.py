#include<iostream>
#include<stdio.h>
using namespace std ;
main()
{
 int i,j,n,k,runs ;
 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  scanf("%d%d",&n,&k) ;
  printf("Case #%d: %s\n",t,(k+1)%(1<<n) == 0 ? "ON" : "OFF") ;
 }
}
