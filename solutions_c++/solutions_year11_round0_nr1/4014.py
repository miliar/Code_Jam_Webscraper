/*
 Mahverik.Maven
 Using DevCpp 4.9.9.2
 Used input and output redirection instead of file I/O.
 Problem A : Bot Trust
*/
 
#include<stdio.h>
#define abs(x) (((x)>=0)?(x):-(x))
#define max(a,b) ((a)>=(b)?(a):(b))

main()
{
 int test,ttest; scanf("%d",&ttest);
 int n,ni; char b1,b2,c;
 for(test=1;test<=ttest;test++)
 {
  int st1=0,st2=0,t=0,tn=0,to1=1,to2=1;
  scanf("%d",&n); scanf(" %c",&b1); 
  if(b1=='O') b2='B'; else b2='O'; scanf("%d",&tn); 
  t=abs(tn-to1)+1; to1=tn; if(st1+t<=st2) st1=st2+1; else st1=st1+t; 
  for(ni=1;ni<n;ni++)
  {
    scanf(" %c",&c); 
    if(c==b1)
    {
      scanf("%d",&tn); t=abs(tn-to1)+1; to1=tn; 
      if(st1+t<=st2) st1=st2+1; else st1=st1+t;
    }             
    else if(c==b2)
    {
      scanf("%d",&tn); t=abs(tn-to2)+1; to2=tn;
      if(st2+t<=st1) st2=st1+1; else st2=st2+t;
    }
  }
   printf("Case #%d: %d\n",test,max(st1,st2));
 }      
}
