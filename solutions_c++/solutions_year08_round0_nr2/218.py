#include <stdio.h>
#include <string.h>
int tra(int hour, int min)
{
	return hour * 60 + min; 
}
int map[250][250], na, nb, link[250], lx[250], vis[250], ansa, ansb; 
int dfs(int cur)
{ 
	if (vis[cur])
		return 0; 
	vis[cur] = 1; 
	int i, n = na + nb; 
	for (i = 0; i < n; i++) 
		if (map[cur][i] && (link[i] == -1 || dfs(link[i])))
		{ 
			lx[cur] = i; 
			link[i] = cur; 
			return 1; 
		}
	return 0;
}
int max_match()
{ 
	int i, n = na + nb; 
	memset(link, 0xff, sizeof(link)); 
	memset(lx, 0xff, sizeof(lx)); 
	for (i = 0; i < n; i++) 
	{ 
		memset(vis, 0, sizeof(vis)); 
		dfs(i); 
	}
	ansa = ansb = 0; 
	for (i = 0; i < na; i++) 
		if (link[i] == -1) 
			ansa++; 
	for (i = na; i < na + nb; i++) 
		if (link[i] == -1) 
			ansb++; 
}
int ta[200], tb[200], ta1[200], tb1[200];
int main() 
{ 
	freopen("B-large.in", "r", stdin); 
	freopen("B-large.out", "w", stdout); 
	int T, tcnt = 0, i, j, tor; 
	int ah, am, bh, bm; 
	scanf("%d", &T); 
	while (T--) 
	{ 
		scanf("%d%d%d", &tor, &na, &nb); 
		for (i = 0; i < na; i++) 
		{
			scanf("%d:%d %d:%d", &ah, &am, &bh, &bm); 
			ta[i] = tra(ah, am); 
			tb[i] = tra(bh, bm); 
		}
		for (i = 0; i < nb; i++) 
		{
			scanf("%d:%d %d:%d", &bh, &bm, &ah, &am); 
			tb1[i] = tra(ah, am); 
			ta1[i] = tra(bh, bm); 
		}
		for (i = 0; i < na + nb; i++)
			for (j = 0; j < na + nb; j++) 
				map[i][j] = 0; 
		for (i = 0; i < na; i++) 
			for (j = 0; j < nb; j++) 
			{
				if (tb[i] + tor <= ta1[j])
					map[i][j + na] = 1; 
				if (tb1[j] + tor <= ta[i])
					map[j + na][i] = 1; 
			}
		/*for (i = 0; i < na + nb; i++) 
		{ 
			for (j = 0; j < na + nb; j++) 
				printf("%d ", map[i][j]); 
			printf("\n");
		}*/
		max_match();
		printf("Case #%d: %d %d\n", ++tcnt, ansa, ansb); 
	}
} 
