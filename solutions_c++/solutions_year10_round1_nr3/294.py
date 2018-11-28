#include<stdio.h>
#include<stdlib.h>

int yiping(int a,int b)
{
   int tmp,count=0;
   if(a==b)
      return 0;
   while(1)
   {
      if(a<b)
      {
         tmp=a;
         a=b;
         b=tmp;      
      }  
      if(a/b>1)
      {
         count++;
         break;         
      }   
      else
      {
         a-=b;    
         count++;
      }     
   }
   if(count%2==1)
      return 1;
   return 0;        
}


int main()
{
   freopen("C-small-attempt0.in","r",stdin);
   freopen("out","w",stdout);
   
   int cases,i,count,p,q,a1,a2,b1,b2;
   scanf("%d",&cases);
   for(i=1;i<=cases;i++)
   {
      count=0;
      scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
      for(p=a1;p<=a2;p++)
         for(q=b1;q<=b2;q++)
            count+=yiping(p,q);
      printf("Case #%d: %d\n",i,count);           
   }
   return 0;
}
