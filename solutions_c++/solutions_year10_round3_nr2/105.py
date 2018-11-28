#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
   int cs,fat=0;
   freopen("C:\\a.in","r",stdin);
   freopen("C:\\a.out","w",stdout);
   scanf("%d",&cs);
   for(fat=1;fat<=cs;fat++)
   {
	   int a,b,c;
	   scanf("%d%d%d",&a,&b,&c);
	   int cx=0;
	   while(a*c<b) {
		   a*=c;
		   cx++;
	   }
	   int t=0;
	   while(cx){
		   t++;
		   cx>>=1;
	   }
	   printf("Case #%d: %d\n",fat,t);
   }
   return 0;
}
