#include<iostream>
using namespace std;

const int N=1010;
int a[N],b[N];
int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
   int n,x,t,i,j;
   scanf("%d",&t);
   int cs=0;
   while(t--)
   {
	   scanf("%d",&n);
	   for(i=0;i<n;i++) scanf("%d%d",&a[i],&b[i]);
	   int ans=0;
	   for(i=0;i<n;i++)
		   for(j=i+1;j<n;j++)
		   {
			   x=(a[i]-a[j])*(b[i]-b[j]);
			   if(x<0) ans++;
		   }
		   printf("Case #%d: %d\n",++cs,ans);
   }
   return 0;
}