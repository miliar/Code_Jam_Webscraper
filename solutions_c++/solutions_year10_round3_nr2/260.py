#include <stdio.h>

int main()
{
	__int64 tc,t;
	freopen("B-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	scanf("%I64d",&tc);
	for(t=1;t<=tc;t++)
	{
		__int64 L,P,C;
		scanf("%I64d%I64d%I64d",&L,&P,&C);
		__int64 x=L;
		__int64 cnt=0;
		while(x<P)
		{
			x*=C;
			cnt++;
		}
		__int64 res;
		if (cnt == 1)
		{
			res=0;
		}
		else
		{
			res=0;
			__int64 y=1;
			while(y<cnt)
			{
				y*=2;
				res++;
			}
		}
		printf("Case #%I64d: %I64d\n", t, res);
	}

	return 0;
}