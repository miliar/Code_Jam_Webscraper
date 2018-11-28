#include <stdio.h>

int main()
{
	int tc,t,n,s,p,i,k,r;
	scanf("%d\n",&t);
	for (tc=0;tc<t;++tc)
	{
		scanf("%d %d %d",&n,&s,&p);
		r=0;
		for (i=0;i<n;++i)
		{
			scanf("%d",&k);
			if (k>=3*p-2) ++r; else if (p>1 && s>0 && k>=3*p-4) { ++r; --s; }
		}
		printf("Case #%d: %d\n",tc+1,r);
	}
	return 0;
}
