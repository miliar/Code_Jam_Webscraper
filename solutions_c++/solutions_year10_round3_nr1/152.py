#include <stdio.h>
#include <string.h>

int main(void)
{
	int t, n, i, j, test = 0, ans;
	int a[1002], b[1002];
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	while(t --)
	{
		scanf("%d", &n);
		for(i = 0;i < n;i ++)
			scanf("%d %d", &a[i], &b[i]);
		ans = 0;
		for(i = 0;i < n;i ++)
		{
			for(j = i + 1;j < n;j ++)
			{
				if((a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j]))
					ans ++;
			}
		}
		printf("Case #%d: %d\n", ++ test, ans);
	}
	return 0;
}
