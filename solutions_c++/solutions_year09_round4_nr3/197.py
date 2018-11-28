#include <stdio.h>
#include <string.h>

int cost[110][110];
int map[110][110];
bool mark[110];
int link[110];
int n;
int match(int cur)
{
	if (mark[cur]) 
		return 0;
	mark[cur] = 1;
	for (int i = 0; i < n; i++)
		if (map[cur][i] && (link[i] == -1 || match(link[i])))
		{
			link[i] = cur;
			return 1;
		}
	return 0;
}
int max_match()
{
	int res = 0, i;
	memset(link, -1, sizeof(link));
	for (i = 0; i < n; i++)
	{
		memset(mark, 0, sizeof(mark));
		if (match(i))
			res++;
	}
	return res;
}
int main()
{
	int tcse, ics = 1;
	freopen("clin.in", "r", stdin);
	freopen("clout.txt", "w", stdout);
	scanf("%d", &tcse);
	for(ics = 1; ics <= tcse; ics++)
	{
		int i, j, l, k;
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; i++)
			for (j = 0; j < k; j++)
				scanf("%d", &cost[i][j]);
		memset(map, 0, sizeof(map));
		for (i = 0; i < n; i++)
			for (l = i + 1; l < n; l++)
			{
				for (j = 0; j < k; j++)
					if ((cost[i][j] > cost[l][j]) != (cost[i][0] > cost[l][0]) 
					|| cost[i][j] == cost[l][j])
						break;
				if (j == k)
				{ 
					if (cost[i][0] > cost[l][0]) map[l][i] = 1;
					else map[i][l] = 1;
				}
			}
		/*for (i = 0; i < n; i++)	
			for (j = 0; j < n; j++)
				printf("%d%c", g[i][j], j == n - 1 ? '\n' : ' ');*/
		printf("Case #%d: %d\n", ics, n - max_match());
	}
	return 0;
}
