#include <cstdio>
#include <algorithm>
using namespace std;
int t[101][101], H, W;
int res[101][101];
bool vis[101][101];
int ix[] = {-1,0,0,1};
int iy[] = {0,-1,1,0};
int CNT;
int dfs(int x,int y) {
	if(vis[x][y] == 1) return res[x][y];
	vis[x][y] = 1;
	int min = t[x][y], ind = -1;
	for(int k=0;k<4;++k)
		if(x+ix[k] >= 0 && x+ix[k] < H && y+iy[k] >= 0 && y+iy[k]<W && t[x+ix[k]][y+iy[k]] < min) min = t[x+ix[k]][y+iy[k]], ind = k;
	if(min == t[x][y]) {
		res[x][y] = CNT++;
	} else
		res[x][y] = dfs(x+ix[ind],y+iy[ind]);
	return res[x][y];
}
int main() {
	int T;
	scanf("%d",&T);
	for(int x=1;x<=T;++x) {
		CNT = 0;
		printf("Case #%d:\n", x);
		res[0][0] = 1;
		scanf("%d%d",&H,&W);
		for(int i=0;i<H;++i)
			for(int j=0;j<W;++j)
				vis[i][j] = 0, scanf("%d",&t[i][j]);
		for(int i=0;i<H;++i)
			for(int j=0;j<W;++j)
				res[i][j] = dfs(i,j);
		for(int i=0;i<H;++i) {
			for(int j=0;j<W;++j)
				printf("%c ",'a'+res[i][j]);
			printf("\n");
		}
	}
	return 0;
}
