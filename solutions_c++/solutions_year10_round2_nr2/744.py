#include <stdio.h>

int main(void)
{
	int t, b, T, n, k, test = 0, cnt, i, j, ans;
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &t);
	int a[52], v[52];
	bool flag[52];
	while(t --)
	{
		scanf("%d %d %d %d", &n, &k, &b, &T);
		for(i = 0;i < n;i ++)
			scanf("%d", &a[i]);
		for(i = 0;i < n;i ++)
			scanf("%d", &v[i]);
		cnt = 0;
		ans = 0;
		for(i = n - 1;i >= 0;i --)
		{
			if(a[i] + v[i] * T >= b)
			{
				flag[i] = true;
				cnt ++;
				for(j = i + 1;j < n;j ++)
				{
					if(!flag[j])
						ans ++;
				}
			}
			else
				flag[i] = false;
			if(cnt == k)
				break;


		}
		printf("Case #%d: ", ++ test);
		if(cnt < k)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
	return 0;
}


