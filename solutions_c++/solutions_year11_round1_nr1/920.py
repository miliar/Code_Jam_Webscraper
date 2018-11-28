#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int gcd(int a,int b)
{
      if(a==0)
      return b;
      return gcd(b%a,a);
}

int main()
{
           int t,i,pd,pg,think;
           __int64 n;
           bool flag,get;
           freopen("1AA4.in","r",stdin);
           freopen("1AA4.out","w",stdout);
           scanf("%d",&t);
           for(i=1;i<=t;i++)
           {
               get=false;
               scanf("%I64d%d%d",&n,&pd,&pg);
               if(pg==100)
               {
                     get=true;
                     if(pd==100)
                     flag=true;
                     else
                     flag=false;
               }
               if(pg==0)
               {
                        get=true;
                        if(pd==0)
                        flag=true;
                        else
                        flag=false;
               }
               if(pd==0)
               {
                        get=true;
                        flag=true;
               }
               if(!get)
               {
                       think=pd/gcd(pd,100);
                           if(think<=n)
                           {
                              get=true;
                              flag=true;
                           }
                           else
                           {
                               get=true;
                               flag=false;
                           }
               }
               printf("Case #%d: ",i);
               if(flag)
               printf("Possible\n");
               else
               printf("Broken\n");
           }
           return 0;
}
