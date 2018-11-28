/*
 Mahverik
 Using DevCpp 4.9.9.2
 Used input and output redirection instead of file I/O.
 Problem A
*/
 
#include<stdio.h>
#define NMAX 1000
main()
{
 int tcase,ttcase; scanf("%d",&ttcase);



 for(tcase=1;tcase<=ttcase;tcase++)
 {
  int a[NMAX]={0},b[NMAX]={0}; int i,j,n,ins=0;
  scanf("%d",&n);
  for(i=0;i<n;i++) 
  { 
   scanf("%d%d",a+i,b+i); 
   for(j=0;j<i;j++) { if((a[j]>a[i]&&b[j]<b[i])||(a[j]<a[i]&&b[j]>b[i])) ins++; }
  }
  
  printf("Case #%d: %d\n",tcase,ins);
 }      

}
