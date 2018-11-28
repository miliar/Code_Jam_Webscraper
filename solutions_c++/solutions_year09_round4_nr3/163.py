#include <stdio.h>
#include <string.h>
#define INF 0x3ffffff
int price[110][110], g[110][110], n, vis[110], link[110];
int can(int cur)
{
	if (vis[cur]) 
		return 0;
	vis[cur] = 1;
	for (int i = 0; i < n; i++)
		if (g[cur][i] && (link[i] == -1 || can(link[i])))
		{
			link[i] = cur;
			return 1;
		}
	return 0;
}
int max_match()
{
	int res = 0, i;
	memset(link, 0xff, sizeof(link));
	for (i = 0; i < n; i++)
	{
		memset(vis, 0, sizeof(vis));
		if (can(i))
			res++;
	}
	return res;
}
int main()
{
	int T, tcnt = 1;
	freopen("C-large.in", "r", stdin);
	freopen("ans.txt", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		int i, j, l, k;
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; i++)
			for (j = 0; j < k; j++)
				scanf("%d", &price[i][j]);
		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
				g[i][j] = 0; 
		for (i = 0; i < n; i++)
			for (l = i + 1; l < n; l++)
			{
				for (j = 0; j < k; j++)
					if ((price[i][j] > price[l][j]) != (price[i][0] > price[l][0]) || price[i][j] == price[l][j])
						break;
				if (j == k)
				{ 
					if (price[i][0] > price[l][0])
						g[l][i] = 1;
					else
						g[i][l] = 1;
				}
			}
		/*for (i = 0; i < n; i++)	
			for (j = 0; j < n; j++)
				printf("%d%c", g[i][j], j == n - 1 ? '\n' : ' ');*/
		printf("Case #%d: %d\n", tcnt++, n - max_match());
	}
	return 0;
}
