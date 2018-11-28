/**/
#include <stdio.h>
#include <string.h>

#define MAXN 16384

int n, love;
int dist[MAXN], len[MAXN];
char mark[MAXN][MAXN];

int dfs(int x, int y)
{
	int i, l;
	if ( y >= 0 && mark[x][y] >= 0 )
		return mark[x][y];
	if ( y >= 0 )
	{
		mark[x][y] = 0;
		l = dist[x] - dist[y];
	}
	else
		l = dist[x];
	if ( l < 0 )
		l = -l;
	if ( len[x] < l )
		l = len[x];
	if ( dist[x] + l >= love )
		return mark[x][y] = 1;
	for ( i = 0; i < n; ++i )
	{
		if ( i != x && dist[i] >= dist[x] - l && dist[i] <= dist[x] + l )
		{
			if ( dfs(i, x) )
				return mark[x][y] = 1;
		}
	}
	return 0;
}

int main()
{
	FILE *fin = fopen("A-small-attempt1.in", "r");
	FILE *fout = fopen("A-small-attempt1.out", "w");
	int itest, ntest;
	fscanf(fin, "%d", &ntest);
	for ( itest = 0; ++itest <= ntest; )
	{
		int i, j, k;
		memset(mark, -1, sizeof(mark));
		fscanf(fin, "%d", &n);
		for ( i = 0; i < n; ++i )
			fscanf(fin, "%d%d", dist+i, len+i);
		fscanf(fin, "%d", &love);
		if ( dfs(0, -1) )
			fprintf(fout, "Case #%d: YES\n", itest);
		else
			fprintf(fout, "Case #%d: NO\n", itest);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
/**/
