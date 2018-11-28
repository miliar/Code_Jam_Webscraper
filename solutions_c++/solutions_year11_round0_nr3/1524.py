#include <stdio.h>
#include <string.h>

int main()
{
	int n,t,i,a,total,min,sum;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int cas = 1; cas<=t; cas++)
	{
		scanf("%d",&n);
		sum = total = 0;
		min = 11111111;
		for (i=0; i<n; i++)
		{
			scanf("%d",&a);
			sum ^= a;
			if (min>a) min=a;
			total += a;
		}
		if (sum!=0) {
			printf("Case #%d: NO\n",cas);
			continue;
		}
		printf("Case #%d: %d\n",cas,total-min);
	}
	return 0;
}

