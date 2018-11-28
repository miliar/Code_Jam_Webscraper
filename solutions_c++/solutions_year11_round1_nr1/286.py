#include <stdio.h>

int calck(int);

int main()
{
	int t, pd, pg, kd, kg;
	long long n;
	bool ans;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		ans = false;
		scanf("%lld%d%d", &n, &pd, &pg);
		kd = calck(pd);
		kg = calck(pg);
		if (n>=kd)
		{
			if (pg==100)
			{
				if (pd==100)
					ans = true;
			}
			else if (pg==0)
			{
				if (pd==0)
					ans = true;
			}
			else
				ans = true;
		}
		printf("Case #%d: %s\n", i, ans?"Possible":"Broken");
	}
	return 0;
}

int calck(int p)
{
	int k = 100;
	if (p%2==0)
	{
		p /= 2;
		k /= 2;
	}
	if (p%2==0)
	{
		p /= 2;
		k /= 2;
	}
	if (p%5==0)
	{
		p /= 5;
		k /= 5;
	}
	if (p%5==0)
	{
		p /= 5;
		k /= 5;
	}
	return k;
}
