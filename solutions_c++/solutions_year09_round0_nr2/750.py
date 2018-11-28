#include <iostream>
using namespace std;

int mat[110][110];
int ans[110][110];
int edge[110][110][10];
int head[110][110];
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int h,w;

int check(int x,int y) {
	if(x >= 0 && x < h && y >= 0 && y < w)return 1;
	else return 0;
}

void bfs(int x,int y,int cnt) {
	ans[x][y] = cnt;
	for(int i = 0;i < head[x][y];++i) {
		int k = edge[x][y][i];
		int tx = x + dir[k][0],ty = y + dir[k][1];
		if(ans[tx][ty] == -1) {
			bfs(tx,ty,cnt);
		}
	}
}

void solve() {
	memset(head,0,sizeof(head));
	for(int i = 0;i < h;++i) {
		for(int j = 0;j < w;++j) {
			int gx = -1;
			int maxheight = mat[i][j];
			for(int k = 0;k < 4;++k) {
				int tx = i + dir[k][0],ty = j + dir[k][1];
				if(!check(tx,ty))continue;
				if(mat[tx][ty] < maxheight) {
					maxheight = mat[tx][ty];
					gx = k;
				}
			}
			if(gx == -1) {
				continue;
			} else {
				edge[i][j][head[i][j]++] = gx;
				edge[i + dir[gx][0]][j + dir[gx][1]][head[i + dir[gx][0]][j + dir[gx][1]]++] = 3 - gx;
			}
		}
	}
	memset(ans,-1,sizeof(ans));
	int cnt = 0;
	for(int i = 0;i < h;++i) {
		for(int j = 0;j < w;++j) {
			if(ans[i][j] == -1) {
				bfs(i,j,cnt);
				cnt++;
			}
		}
	}
	for(int i = 0;i < h;++i) {
		for(int j = 0;j < w;++j) {
			printf("%c ",ans[i][j] + 'a');
		}
		printf("\n");
	}
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	int cas = 1;
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d",&h,&w);
		for(int i = 0;i < h;++i) {
			for(int j = 0;j < w;++j) {
				scanf("%d",&mat[i][j]);
			}
		}
		printf("Case #%d:\n",cas++);
		solve();
	}
	return 0;
}