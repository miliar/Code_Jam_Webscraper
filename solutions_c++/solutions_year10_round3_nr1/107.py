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
   int a[1001],b[1001];
   for(fat=1;fat<=cs;fat++)
   {
	   int n;
	   scanf("%d",&n);
	   int i;
	   for(i=0;i<n;i++)
		   scanf("%d%d",&a[i],&b[i]);
	   int cx=0;
	   for(i=1;i<n;i++){
		   for(int j=i-1;j>=0;j--){
			   if(a[j]<a[i]&&b[j]>b[i])
				   ++cx;
			   if(a[j]>a[i]&&b[j]<b[i])
				   ++cx;
		   }
	   }
	   printf("Case #%d: %d\n",fat,cx);
   }
   return 0;
}
