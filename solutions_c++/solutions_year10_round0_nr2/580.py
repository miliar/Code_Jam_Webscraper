#include <cstdio>
using namespace std;

int n;
int a[1100];

int gcd(int x1,int x2)
{
	for(;;)
	{
		if(x2==0)break;
		x1%=x2;
		if(x1==0)break;
		x2%=x1;
	}
	return x1+x2;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int t1=1;t1<=t;++t1)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;++i)
			scanf("%d",&a[i]);
		for(int i=n;i>=1;--i)
		{
			int t=a[i]-a[i-1];
			if(t<0)t=-t;
			a[i]=t;
		}
		int g=0;
		for(int i=2;i<=n;++i)
			g=gcd(g,a[i]);
		printf("Case #%d: %d\n",t1,(g-(a[1]%g))%g);
	}
	return 0;
}

