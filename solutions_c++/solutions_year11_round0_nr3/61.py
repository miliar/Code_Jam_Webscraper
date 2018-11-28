#include <stdio.h>

int main()
{
	int cases;
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		int n, m=1000000000;
		scanf(" %d", &n);
		int res=0, sum=0;
		for(int i=0; i<n; i++)
		{
			int v;
			scanf(" %d", &v);
			res+=v;
			sum^=v;
			if (v<m) m=v;
		}
		printf("Case #%d: ", cs);
		if ((n>=2) && (sum))
			printf("NO\n");
		else
			printf("%d\n", res-m);
	}
	return 0;
}
