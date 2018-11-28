#include <stdio.h>
#include <stdlib.h>

int t, n;
int x[810];
int y[810];
int num;

int cmp(const void *a, const void *b)
{
	return *(int *)a - *(int *)b;
}

int main()
{
	int i;
	FILE *out;
	out = fopen("C:\\MSP.txt", "wt");
	
	scanf("%d", &t);
	
	for(num = 1; num <= t; num++)
	{
		scanf("%d", &n);
		
		for(i = 0; i < n; i++)
		{
			scanf("%d", &x[i]);
		}
		for(i = 0; i < n; i++)
		{
			scanf("%d", &y[i]);
		}
		
		qsort(x, n, sizeof(x[0]), cmp);
		qsort(y, n, sizeof(y[0]), cmp);
		
		long long ans = 0;
		
		for(i = 0; i < n; i++)
		{
			ans += x[i] * y[n-1-i];
		}
		
		//printf("Case #%d: %lld\n", num, ans);
		fprintf(out, "Case #%d: %lld\n", num, ans);
	}
	
	return 0;
}