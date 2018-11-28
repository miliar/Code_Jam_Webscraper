#include <stdio.h>

int n, k, ans;
int map[110][30];
int graph[110][110];
int temp[110];

void re(int st, int cnt)
{
	int i, j;

	if(cnt > ans) ans = cnt;
	for(i = st; i < n; i++)
	{
		for(j = 0; j < cnt; j++)
		{
			if(graph[i][temp[j]] == 0) break;
		}
		if(j == cnt)
		{
			temp[cnt] = i;
			re(i+1, cnt+1);
		}
	}
}

void process()
{
	int i, j, l;

	for(i = 0; i < n; i++)
		for(j = 0; j < n; j++)
			graph[i][j] = 0;
	for(i = 0; i < n; i++)
		for(j = i+1; j < n; j++)
		{
			for(l = 0; l < k; l++)
				if(map[i][l] == map[j][l]) break;
			if(l < k)
			{
				graph[i][j] = 1;
				graph[j][i] = 1;
				continue;
			}
			if(map[i][0] < map[j][0])
			{
				for(l = 0; l < k; l++)
					if(map[i][l] > map[j][l]) break;
			}
			else
			{
				for(l = 0; l < k; l++)
					if(map[i][l] < map[j][l]) break;
			}
			if(l < k)
			{
				graph[i][j] = 1;
				graph[j][i] = 1;
			}
		}
	ans = 0;
	re(-1, 0);
}

int main()
{
	int i, j;
	int t, casecnt;

	scanf("%d", &t);
	for(casecnt = 0; casecnt < t; casecnt++)
	{
		scanf("%d %d", &n, &k);
		for(i = 0; i < n; i++)
			for(j = 0; j < k; j++)
				scanf("%d", &map[i][j]);
		process();
		printf("Case #%d: %d\n", casecnt+1, ans);
	}

	return 0;
}