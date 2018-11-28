#include <stdio.h>

long long n, pd, pg;

void cal(long long p, long long &a, long long &b)
{
	int t, i;
	t=100;
	a=t;
	b=p;
	if (b==0) return;
	for (i=2; i<=10; i++)
	  while (p%i==0 && t%i==0)
	  {
	  	p/=i;
	  	t/=i;
	  }
	a=t;
	b=p;  
}



int main()
{
	int T, cas=0;
	long long n, pd, pg, ad, bd, ag, bg;
	freopen("a2.in", "r", stdin);
	freopen("a2.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%I64d%I64d%I64d", &n, &pd, &pg);
		cal(pd, ad, bd);
		cal(pg, ag, bg);
		
		if (ad>n || bg==0 && bd>0 || ag-bg==0 && ad-bd>0)
			printf("Case #%d: Broken\n", ++cas);
		else printf("Case #%d: Possible\n", ++cas);		     
	}
	return 0;
}