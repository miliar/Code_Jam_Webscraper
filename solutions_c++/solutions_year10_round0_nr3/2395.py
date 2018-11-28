#include <stdio.h>
#include <string.h>

int main(void)
{
	int i, n, k, r, t, ans, sum , test = 0;
	int a[1002];
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("c-small.out", "w", stdout);
	scanf("%d", &t);
	while(t --)
	{
		scanf("%d %d %d", &r, &k, &n);
		sum = 0;
		for(i = 0;i < n;i ++)
		{
			scanf("%d", &a[i]);
			sum += a[i];
		}
		if(sum <= k)
		{
			printf("Case #%d: %d\n", ++ test, sum * r);
			continue;
		}
		i = 0;
		ans = 0;
		while(r --)
		{
			sum = 0;
			while(sum <= k)
			{
				sum += a[i ++];
				if(i == n)
					i = 0;
			}
			if(i == 0)
			{
				sum -= a[n - 1];
				i = n - 1;
			}
			else
			{
				sum -= a[i - 1];
				i --;
			}
			ans += sum;
		}
		printf("Case #%d: %d\n", ++ test, ans);

	}
	return 0;
}
	
