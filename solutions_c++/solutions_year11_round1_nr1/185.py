#include <stdio.h>
#include <stdlib.h>
long long n;
int t;
int pd,pg;
int d;
int isexceed;
long long tmp;
bool ispass;
inline int gcd(int a,int b)
{
 if(b==0){return a;}
 else{return gcd(b,a%b);}
}
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%I64d",&n);
  scanf("%d%d",&pd,&pg);
  ispass=false;
  if(pd==0){ispass=true;}
  else
  {
  d=gcd(pd,100);
  isexceed=100/d;
  tmp=isexceed;
   if(tmp<=n){ispass=true;}
  }
  if(ispass==true)
  {
   if(pg==100)
   {
    if(pd==100){printf("Case #%d: Possible\n",i);}
    else{printf("Case #%d: Broken\n",i);}
   }
   else if(pg==0)
   {
    if(pd==0){printf("Case #%d: Possible\n",i);}
    else{printf("Case #%d: Broken\n",i);}
   }
   else
   {
     printf("Case #%d: Possible\n",i);
   }
  }
  else
  {
   printf("Case #%d: Broken\n",i);
  }
 }
 return 0;
}
