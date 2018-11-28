#include <stdio.h>

const int N = 1000;

int main()
{
	int t, n, ans, now, count;
	int get[N], use[N];
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		ans = 0;
		scanf("%d", &n);
		for (int j=0;j<n;j++)
		{
			scanf("%d", &get[j]);
			get[j]--;
			use[j] = 0;
		}
		for (int j=0;j<n;j++)
			if (!use[j] && get[j]!=j)
			{
				count = 1;
				now = j;
				while (get[now]!=j)
				{
					now = get[now];
					use[now] = 1;
					count++;
				}
				ans += count;
			}
		printf("Case #%d: %d.000000\n", i, ans);
	}
	return 0;
}
