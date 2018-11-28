#include<stdio.h>
#include<stdlib.h>
int map[111][111];
int dir[111][111];
int count;
char ans[111][111];
int rx[] = {-1,0,0,1};
int ry[] = {0,-1,1,0};
int op[] = {3,2,1,0};
int w,h;
void dfs(int x,int y,char c){
	if(x == 0 || x == h + 1 || y == 0 || y == w + 1)return;

	ans[x][y] = c;
	for(int i=0;i<4;i++){
		int xt = x + rx[i];
		int yt = y + ry[i];
		if(dir[xt][yt] == op[i]){
			dfs(xt,yt,c);
		}
	}
	return;
}
int main(){
	int t;
	scanf("%d",&t);
	for(int ca = 0;ca<t;ca++){
		scanf("%d %d",&h,&w);
		for(int i=0;i<111;i++)
			for(int j=0;j<111;j++){
				map[i][j] = 10000000;
				ans[i][j] = 0;
			}
		for(int i=1;i<=h;i++){
			for(int j=1;j<=w;j++)
				scanf("%d",&map[i][j]);
		}
		for(int i=1;i<=h;i++){
			for(int j=1;j<=w;j++){
				int flag = -1;
				int min = 100000;
				for(int k=0;k<4;k++){
					int x = i + rx[k];
					int y = j + ry[k];
					if(map[x][y] < map[i][j] && min > map[x][y]){
						min = map[x][y];
						flag = k;
					}
				}
				dir[i][j] = flag;
			}
		}
		count = 0;
		for(int i=1;i<=h;i++){
			for(int j=1;j<=w;j++){
				if(ans[i][j] != 0)continue;
				int si = i,sj = j;
				while(1){
					if(dir[si][sj] == -1)break;
					int ti = si,tj = sj;
					si += rx[dir[ti][tj]];
					sj += ry[dir[ti][tj]];
				}
				dfs(si,sj,'a' + count);
				count++;
			}
		}
		printf("Case #%d:\n",ca + 1);
		for(int i=1;i<=h;i++){
			for(int j=1;j<=w;j++){
				if(j != 1)printf(" ");
				printf("%c",ans[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
