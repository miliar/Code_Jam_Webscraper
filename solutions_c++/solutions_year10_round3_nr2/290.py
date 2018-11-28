#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
  
   freopen("C://B-small.in","r",stdin);
   freopen("C://out.txt","w",stdout);
 int cas,cc=0;
   __int64 a,b,c;
   scanf("%d",&cas);
   while(cas--)
   {
	  cc++;
	  
	   scanf("%I64d %I64d %I64d",&a,&b,&c);
	   int cwp=0;
	   while(a*c<b)
	   {
		   cwp++;
		   a*=c;
		  
	   }
	   int zz=0;
	   while(cwp)
	   {
		   zz++;
		   cwp>>=1;
	   }
	   printf("Case #%d: %d\n",cc,zz);
   }
   return 0;
}
