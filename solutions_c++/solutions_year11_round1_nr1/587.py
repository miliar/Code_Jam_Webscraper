#include<stdio.h>

#define LL long long

int gcd(int a,int b)
{
	if(!b)return a;
	return gcd(b,(a%b));
}

int main()
{
	freopen("free1.in","r",stdin);
	freopen("free1.out","w",stdout);
	int t,pd,pg,cs=0;
	LL n;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lld%d%d",&n,&pd,&pg);
		int ok = 1;
		int g = gcd(pd,100);
		int d = 100/g;
		if(d>n)
			ok = 0;
		if(pd>0 && pg==0)
			ok = 0;
		if(pd<100 && pg==100)
			ok = 0;
		if(ok)
			printf("Case #%d: Possible\n",++cs);
		else
			printf("Case #%d: Broken\n",++cs);
	}
	return 0;
}