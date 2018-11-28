 
#include<stdio.h>


main()
{
 int test,ttest; scanf("%d ",&ttest); 
 int n=0,s=0,p=0,i=0,ans=0,t=0;
 for(test=1;test<=ttest;test++)
 {                    
  n=0;s=0;p=0;i=0;t=0;
  scanf("%d %d %d",&n,&s,&p); 
  ans=0;
  for(i=1;i<=n;i++)
  {
    scanf("%d",&t);
    if(t>=3*p-2) { ans++; }
    else if(t>=3*p-4&&s>0&&p>1) { s--; ans++; }                    
  }
  if(p==0) { ans=n; }
  printf("Case #%d: %d\n",test,ans);
 }      
}
