#include <stdio.h>

int main()
{
	int cases;
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		int n, v, res=0;
		scanf(" %d", &n);
		for(int i=1; i<=n; i++)
		{
			scanf(" %d", &v);
			if (v!=i) res++;
		}
		printf("Case #%d: %d.000000\n", cs, res);
	}
	return 0;
}
