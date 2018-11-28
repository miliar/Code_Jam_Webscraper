#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int sink[110][110];
int h[110][110];
char mp[110 * 110];
int n, m;

int dfs(int x, int y)
{
	if(sink[x][y] != -1){
		return sink[x][y];
	}
	sink[x][y] = x * m + y;
	int xx = -1, yy;
	for(int k = 0; k < 4; k++){
		int nx = x + d[k][0];
		int ny = y + d[k][1];
		if(nx < n && nx >= 0 && ny < m && ny >= 0 && h[nx][ny] < h[x][y]){
			if(xx == -1 || h[xx][yy] > h[nx][ny]){
				xx = nx;
				yy = ny;
			}
		}
	}
	if(xx != -1){
		sink[x][y] = dfs(xx, yy);
	}
	return sink[x][y];
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, i, j;
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++)
	{
		scanf("%d%d", &n, &m);
		for(i = 0; i < n; i++){
			for(j = 0; j < m; j++){
				scanf("%d", &h[i][j]);
			}
		}
		memset(sink, -1, sizeof(sink));
		for(i = 0; i < n; i++){
			for(j  = 0; j < m; j++){
				sink[i][j] = dfs(i, j);
			}
		}	
		memset(mp, 0, sizeof(mp));
		char ch = 'a';
		for(i = 0; i < n; i++){
			for(int j = 0; j < m; j++)
			{
				if(!mp[sink[i][j]]){
					mp[sink[i][j]] = ch++;
				}
			}
		}
		printf("Case #%d:\n", cases);
		for(i = 0; i < n; i++){
			for(j = 0; j < m - 1; j++)
			{
				printf("%c ", mp[sink[i][j]]);
			}
			printf("%c\n", mp[sink[i][j]]);
		}
	}
	return 0;
}

				


