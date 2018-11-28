#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
      int t,i,n,p1,p2,t1,t2,j,m1,m2,mm,tt;
      char order[12];
      freopen("A-large.in","r",stdin);
	   freopen("A-large.out","w",stdout);
      scanf("%d",&tt);
      for(i=1;i<=tt;i++)
      {
          t=0;
          p1=p2=1;
          t1=t2=0;
          scanf("%d",&n);
          for(j=0;j<n;j++)
          {
               scanf("%s %d",order,&mm);
               if(order[0]=='O')
               {
                      m1=mm-p1;
                      if(m1<0)
                      m1=-m1;
                      t1+=m1;
                      if(t1<=t)
                      t1=++t;
                      else
                      {
                          t1++;
                          t=t1;
                      } 
                      p1=mm;     
               }
               if(order[0]=='B')
               {
                      m2=mm-p2;
                      if(m2<0)
                      m2=-m2;
                      t2+=m2;
                      if(t2<=t)
                      t2=++t;
                      else
                      {
                          t2++;
                          t=t2;
                      }    
                      p2=mm;  
               }
          }
          printf("Case #%d: %d\n",i,t);

      }
      return  0;
}
