#include <cstdio>
#include <memory.h>
int n,m;
char b_map[101][101];
int map[101][101];
int ra;
int p[4][2]={{0,1},{1,0},{1,1},{1,-1}};
int dfs(int x,int y,int bang,int block,int color) { //bang : 0 ¡æ, 1 ¡è, 2 ¢Ö, 3 ¢Ø
	if(block==m) {
		if(map[x+p[bang][0]][y+p[bang][1]]!=color) {
			if((ra & color)==0) ra+=color;
		}
	}
	if(map[x+p[bang][0]][y+p[bang][1]]!=color) return 0;
	else dfs(x+p[bang][0],y+p[bang][1],bang,block+1,color);
	return 0;
}
int proc() {
	int i,j;
	for(i=1;i<=n;i++) {
		for(j=1;j<=n;j++) {
			if(map[i][j]==1) {
				if(j+m-1<=n) dfs(i,j,0,1,1);
				if(i+m-1<=n) dfs(i,j,1,1,1);
				if(j+m-1<=n && i+m-1<=n) dfs(i,j,2,1,1);
				if(j-m+1>0 && i+m-1<=n) dfs(i,j,0,1,1);
			}
			if(map[i][j]==2) {
				if(j+m-1<=n) dfs(i,j,0,1,2);
				if(i+m-1<=n) dfs(i,j,1,1,2);
				if(j+m-1<=n && i+m-1<=n) dfs(i,j,2,1,2);
				if(j-m+1>0 && i+m-1<=n) dfs(i,j,0,1,2);
			}
		}
	}
	return 0;
}
int main() {
	FILE *fi=fopen("INPUT.TXT","rt");
	FILE *fo=fopen("OUTPUT.TXT","wt");
	int T,Ti;
	fscanf(fi,"%d",&T);
	for(Ti=0;Ti<T;Ti++) {
		fscanf(fi,"%d%d",&n,&m);
		int i,j;
		for(i=1;i<=n;i++) {
			fscanf(fi,"%s",b_map[i]+1);
		}
		for(i=1;i<=n;i++) {
			for(j=1;j<=n;j++) {
				if(b_map[i][j]=='.') {
					map[n-j+1][i]=0;
				}
				if(b_map[i][j]=='R') {
					map[n-j+1][i]=1;
				}
				if(b_map[i][j]=='B') {
					map[n-j+1][i]=2;
				}
			}
		}
		int dif,sp;
		for(i=1;i<=n;i++) {
			dif=0;
			sp=-1;
			for(j=1;j<=n;j++) {
				if(map[j][i]==0) {
					dif++;
				}
				else {
					sp=i;
					map[j-dif][i]=map[j][i];
					if(dif!=0) map[j][i]=0;
				}
			}
		}
		proc();
		fprintf(fo,"Case #%d: ",Ti+1);
		if(ra==0) fprintf(fo,"Neither\n");
		else if(ra==1) fprintf(fo,"Red\n");
		else if(ra==2) fprintf(fo,"Blue\n");
		else if(ra==3) fprintf(fo,"Both\n");
		ra=0;
		for(i=0;i<=n;i++) {
			memset(b_map,0,sizeof(b_map));
			memset(map,0,sizeof(map));
		}
	}
	return 0;
}