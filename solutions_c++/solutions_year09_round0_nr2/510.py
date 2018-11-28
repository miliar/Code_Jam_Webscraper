#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int map[105][105];
int f[105][105];
int smap[105][105];
int n, h, w;
int dx[] = { -1, 0, 0, 1 };
int dy[] = { 0, -1, 1, 0 };
int sx[30];
int sy[30];
int ans[30];
int sn;	

int dfs(int x, int y)
{
	if(f[x][y] > 0 )return f[x][y];
	int k = -1;
	int kx, ky;
	for(int i = 3; i >= 0; i-- ){
		int xx = x+dx[i];
		int yy = y+dy[i];
		if(xx>=0&&xx<h && yy >=0  && yy < w ){
			if(map[xx][yy] < map[x][y]){
				if( k < 0 || map[xx][yy] <= map[kx][ky] ){
					k = i;
					kx = xx;
					ky = yy;
				}
			}		
		}
	}
	return (f[kx][ky] = dfs(kx, ky));
}

void solve()
{
	sn = 0;
	for(int i = 0; i < h; i++){
		for(int j = 0; j < w; j++ ){
			int flag = 0;
			for(int k = 0; k < 4; k++ ){
				if(i+dx[k] >= 0 && i+dx[k] < h && j+dy[k] >= 0 && j+dy[k] < w && map[i+dx[k]][j+dy[k]] < map[i][j]){
					flag = 1;
					break;
				}
			}
			if(flag==0)
			{
				sx[sn] = i;
				sy[sn++] = j;
			}
		}
	}
	memset(f,0,sizeof(f));	
	for(int i = 0; i < sn; i++ ){
		f[sx[i]][sy[i]] = i+1;
	}
	for(int i = 0; i < h; i++ ){
		for(int j = 0; j < w; j++){
			f[i][j] = dfs(i,j);
		}
	}
	memset(ans,0,sizeof(ans));
	int index = 0;
	for(int i = 0; i < h; i++ ){
		for(int j = 0; j < w; j++ ){
			if(ans[f[i][j]] == 0 ){
				ans[f[i][j]] = ++index;
				
			}
			printf("%c ", 'a' - 1 + ans[f[i][j]] );
		}
		printf("\n");
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&n);
	for(int i = 1; i <= n; i++){
		scanf("%d%d",&h,&w);
		for(int j = 0; j < h; j++){
			for(int k = 0; k < w; k++ ){
				scanf("%d",&map[j][k]);		
			}
		}
		printf("Case #%d:\n",i);
		solve();
	}
	return 0;
}
