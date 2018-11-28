#include <stdio.h>

const int MAXN = 60;

int n, k, b, t;
int x[MAXN], v[MAXN];
int ans;

void process()
{
	int check[MAXN], i, cnt = 0;
	int j;

	for(i = 0; i < n; i++)
	{
		check[i] = (x[i] + v[i]*t >= b);
		cnt += check[i];
	}
	if(cnt < k)
	{
		ans = -1;
		return;
	}
	ans = cnt = 0;
	i = n-1;
	while(k > 0) k -= check[i--];
	i++;
	for(; i < n; i++)
	{
		if(check[i] == 0) continue;
		for(j = i+1; j < n; j++)
			if(check[j] == 0) ans++;
	}
}

int main()
{
	int c, z = 1, i;

	scanf("%d", &c);
	while(c > 0)
	{
		scanf("%d %d %d %d", &n, &k, &b, &t);
		for(i = 0; i < n; i++)
			scanf("%d", &x[i]);
		for(i = 0; i < n; i++)
			scanf("%d", &v[i]);
		printf("Case #%d: ", z++);
		process();
		if(ans < 0) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
		c--;
	}

	return 0;
}