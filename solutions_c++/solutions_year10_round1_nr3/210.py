#include <stdio.h>
#include <algorithm>
#define N 100
#define phi 1.61803398875

using namespace std;

int T,i,j,k,a1,a2,b1,b2,a[2000000],adr[2000000],t,m[10];
__int64 ans;

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);
	for(i=0;i<=1000000;i++)
		a[i]=i*phi+1;
	for(i=0;i<1000000;i++)
		for(j=a[i];j<a[i+1];j++)
			adr[j]=i;
	while(T--)
	{
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		ans=0;
		for(i=a1;i<=a2;i++)
		{
			if(adr[i]<b1 && a[i]>b2)
				continue;
			if(adr[i]>=b2 || a[i]<=b1)
			{
				ans+=(b2-b1+1);
				continue;
			}
			if(a[i]<=b2)
				ans+=(b2-a[i]+1);
			if(adr[i]>=b1)
				ans+=(adr[i]-b1+1);
		}
		printf("Case #%d: %I64d\n",++t,ans);
	}
	return 0;
}
