#include<iostream>
#include<algorithm>
#include<memory.h>
using namespace std;
int a[100005],n;
int main()
{
   int tcase,cas,n,i,j;
   freopen("C-large.in","r",stdin);
   freopen("C-large.out","w",stdout);
   cin>>tcase;
   for(cas=1;cas<=tcase;cas++)
   {
	     cin>>n;
		 for(i=1;i<=n;i++)
			 cin>>a[i];
		 sort(a+1,a+1+n);
		 int sum=0;
		 int xor=0;
		 for(i=1;i<=n;i++)
		 {
			 sum+=a[i];
			 xor^=a[i];
		 }
		 printf("Case #%d: ",cas);
		 if (xor!=0) printf("NO\n");
		 else printf("%d\n",sum-a[1]);
   }
}