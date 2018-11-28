/*
 Mahverik.Maven
 Using DevCpp 4.9.9.2
 Used input and output redirection instead of file I/O.
 Problem C : Candy Splitting
*/
 
#include<stdio.h>
#include <algorithm>

main()
{
 int test,ttest; scanf("%d",&ttest);
 for(test=1;test<=ttest;test++)
 {
   long int n=0,i=0,j=0,r=0;
   scanf("%d",&n); int a[1000]={0};
   for(i=0;i<n;i++) scanf("%d",a+i); 
   std::sort(a,a+n);
   long int a1=0,a2=0,s=0;
   //for(i=0;i<n;i++) printf("%d ",a[i]);
   for(i=0;i<n;i++) { a2^=a[i]; s+=a[i];}
   
   for(j=0;j<n-1;j++)
   {
    a1^=a[j]; a2^=a[j]; s-=a[j];
    if(a1==a2) { r=s; break; }              
   }
   
   if(a1!=a2) printf("Case #%d: NO\n",test);
   else printf("Case #%d: %d\n",test,r);
 }      
}
