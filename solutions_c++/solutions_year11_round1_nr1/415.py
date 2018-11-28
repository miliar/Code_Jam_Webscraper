#include<cstdio>
using namespace std;

bool ok(long long int n, int pd, int pg)
{
	if (pd == 0 && pg != 100)
		return true;

	if (pg == 0 && pd != 0)
		return false;
	if (pg == 100 && pd != 100)
		return false;

	int min = 100;
	while ((pd % 5 == 0) && (min % 5 == 0))
	{
		pd /= 5;
		min /= 5;
	}
	while ((pd % 2 == 0) && (min % 2 == 0))
	{
		pd /= 2;
		min /= 2;
	}

	if (min > n)
		return false;

	
}

int main()
{
	int t,d,g;
	long long int n;
	scanf("%d",&t);
	for (int it=1; it<=t; it++)
	{
		scanf("%lld %d %d",&n,&d,&g);
		if (ok(n,d,g))
			printf("Case #%d: Possible\n",it);
		else
			printf("Case #%d: Broken\n",it);

	}
}
