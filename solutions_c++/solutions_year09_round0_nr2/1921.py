#include<stdio.h>
#include<string.h>

const int dx[4]={-1,0,0,1}, dy[4]={0,-1,1,0};
int n,m,a[200][200];
char ans[200][200],cc;

char dfs(int x,int y){
	if (ans[x][y]) return ans[x][y];
	int xx=-1, yy=-1;
	for (int i=0; i<4; i++){
		int nx=x+dx[i], ny=y+dy[i];
		if (nx<0 || ny<0 || nx>=n || ny>=m) continue;
		if (a[nx][ny]<a[x][y] && (xx==-1 || a[nx][ny]<a[xx][yy])){
			xx=nx; yy=ny;
		}
	}
	return ans[x][y]=(xx==-1)?(cc++):dfs(xx,yy);
}

int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		scanf("%d%d",&n,&m);
		for (int i=0; i<n; i++){
			for (int j=0; j<m; j++) scanf("%d",&a[i][j]);
		}
		cc='a';
		memset(ans,0,sizeof(ans));
		printf("Case #%d:\n",tt);
		for (int i=0; i<n; i++){
			for (int j=0; j<m; j++){
				printf("%c ",dfs(i,j));
			}
			printf("\n");
		}
	}
	return 0;
}
