#include<iostream>
long long gcd(long long x,long long y)
{
     if(y==0)
     return x;
     return gcd(y,x%y);
     }
int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);

     long long T,n,pd,pg;
     long long t;

     scanf("%I64d",&T);
     for(t=1;t<=T;t++)
     {
          scanf("%I64d%I64d%I64d",&n,&pd,&pg);
          long long pos=1;
          long long k=gcd(pd,100);

          if(100/k>n)
          pos=0;

          if(pg==100&&pd!=100)
          pos=0;

          if(pg==0&&pd!=0)
          pos=0;

          if(pos==0)
          printf("Case #%I64d: Broken\n",t);
          else
          printf("Case #%I64d: Possible\n",t);
          }
     return 0;
     }
