#include <stdio.h>

#define ab(x) (((x)>=0)?(x):(-(x)))

int main()
{
	int n,i,a,b,ap,bp,t,p,ca=0;
	char s[1000],c;
	scanf("%d",&n);
	while (scanf("%d",&n)==1)
	{
		ap=bp=1;
		a=b=t=0;
		for (i=0;i<n;++i)
		{
			scanf("%s %d",s,&p);
			c=s[0];
			if (c=='O' || c=='o')
			{
				if (ab(p-ap)+a>t) t=ab(p-ap)+a;
				ap=p;
				a=++t;
			} else
			{
				if (ab(p-bp)+b>t) t=ab(p-bp)+b;
				bp=p;
				b=++t;
			}
		}
		printf("Case #%d: %d\n",++ca,t);
	}
	return 0;
}
