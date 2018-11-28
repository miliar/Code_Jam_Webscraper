#include <iostream>
#include <cstdio>
#include <algorithm>
int main()
{
	int i,k,t,cas = 1,n,l,a,sum;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d",&n);
		k = 0;
		sum = 0;
		l = 100000000;
		for (i = 0;i < n;i++)
		{
			scanf("%d",&a);
			sum += a;
			k = k^a;
			if (a < l)
				l = a;
		}
		if (k == 0)
			printf("Case #%d: %d\n",cas++,sum - l);
		else
			printf("Case #%d: NO\n",cas++);
	}
	return 0;
}