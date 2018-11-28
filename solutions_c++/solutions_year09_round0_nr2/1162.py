#include <stdio.h>
#include <vector>

using namespace std;

int size;
int h,w;
int g[109][109];
char rusCh[109][109];
vector<int> rus[109 * 109];
bool visit[109 * 109];
int cas;

void input() {
	int i,j;

	for (i = 0; i < 109 * 109; ++i) rus[i].clear();
	memset(visit, 0, sizeof(visit));
	scanf("%d %d",&h,&w);
	for(i = 0; i < h; i++) {
		for(j = 0; j < w; j++ ) {
			scanf("%d",&g[i][j]);
		}
	}
}

int findMin(int row,int col) {
	int min = g[row][col];
	int temp = row * w + col;
	if(row != 0 && g[row - 1][col] < min) {
		min = g[row - 1][col];
		temp = (row - 1) * w + col;
	}
	if(col != 0 && g[row][col - 1] < min) {
		min = g[row][col - 1];
		temp = row * w + col - 1;
	}
	if(col + 1 <= (w - 1) && g[row][col + 1] < min) {
		min = g[row][col + 1];
		temp = row * w + col + 1;
	}
	if(row + 1 <= h - 1 && g[row + 1][col] < min) {
		min = g[row + 1][col];
		temp = (row + 1) * w + col;
	}

	return temp;
}

void dfs(int u,char cur) {
	int i,x,xrow,xcol;
	visit[u] = true;
	rusCh[u / w][u % w] = cur;
	for(i = 0; i < rus[u].size(); i++ ) {
		x = rus[u][i];
		if (visit[x]) continue;
		xrow = x / w;
		xcol = x % w;
		rusCh[xrow][xcol] = cur;
		dfs(rus[u][i],cur);
	}
}


void solve() {
	int i,j,u,v;
	char cur;
	for(i = 0; i < h; i++ ) {
		for(j = 0; j < w; j++ ) {
			u = i * w + j;
			v = findMin(i,j);
			if (u == v) continue;
		//	printf("u = %d v = %d\n", u, v);
			rus[u].push_back(v);
			rus[v].push_back(u);
		}
	}
	cur = 'a';
	for(i = 0; i < h; i++ ) {
		for(j = 0; j < w; j++ ) {
			
			u = i * w + j;
			if (visit[u]) continue;
			dfs(u,cur);
			cur++;
		}
	}
	printf("Case #%d:\n", ++cas);
	for(i = 0; i < h; i++ ) {
		for(j = 0; j < w; j++ ) {
			if (j) printf(" ");
			printf("%c",rusCh[i][j]);
		}
		printf("\n");
	}
}
		


int main() {
	freopen("D:\\B-large.in", "r", stdin);
	freopen("D:\\B-large.out", "w", stdout);
	int i;
	scanf("%d",&size);
	for(i = 0; i < size; i++ ) {
		input();
		solve();
	}
	return 0;
}