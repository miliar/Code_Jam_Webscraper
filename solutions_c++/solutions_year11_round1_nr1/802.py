#include <stdio.h>

int gcd(int a, int b)
{
	int r;
	if (b==0) return a;
	r=a%b;
	while (r)
	{
		a=b;
		b=r;
		r=a%b;
	}
	return b;
}

int main()
{
	__int64 pd,pg,gd,t,n;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%I64d",&t);
	for (int cas=1; cas<=t; cas++)
	{
		scanf("%I64d%I64d%I64d",&n,&pd,&pg);
		gd = gcd(100,pd);
		if (pd==100 && pg==100 && n>=1)
		{
			printf("Case #%d: Possible\n",cas);
		} else if (pd==0 && pg==0 && n>=1)
		{
			printf("Case #%d: Possible\n",cas);
		} else if (100/gd<=n && 100!=pg && 0!=pg)
			printf("Case #%d: Possible\n",cas);
		else printf("Case #%d: Broken\n",cas);
	}
	return 0;
}

