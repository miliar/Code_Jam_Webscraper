#include<stdio.h>

int main()
{

	freopen("B-large.in", "r", stdin);
	freopen("B-large.ans", "w", stdout);

	int u, m, l, ub, mb, uc, mc, val, tst, n, s, p;

	scanf("%d", &tst);
	for(int t=1; t<=tst; t++)
	{
		uc=0;
		mc=0;
		scanf("%d %d %d", &n, &s, &p);
		if(p>0)
			ub = p+(p-1)+(p-1);
		else
			ub=p;
		if(p>1)
			mb = p+(p-2)+(p-2);
		else
			mb = p;

		for(int i=0; i<n; i++)
		{
			scanf("%d", &val);
			if(val>=ub) uc++;
			else if(val>=mb) mc++;
		}
		if(mc>s) uc+=(s);
		else uc+=mc;

		printf("Case #%d: %d\n", t, uc);
	}
	return 0;
}
