#include <cstdio>
int tc,h,w,a[105][105];
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
char vis[105][105],c;
void dfs(int y,int x){
	vis[y][x]='#';
	int mn=a[y][x],ky=-1,kx=-1;
	for (int d=0;d<4;d++){
		int dy=dir[d][0]+y,dx=dir[d][1]+x;
		if (dy<0||dx<0||dy==h||dx==w) continue;
		if (mn>a[dy][dx]) mn=a[dy][dx],ky=dy,kx=dx;
	}
	if (kx==-1) vis[y][x]=c++;
	else if (vis[ky][kx]!=' ') vis[y][x]=vis[ky][kx];
	else {
		dfs(ky,kx);
		vis[y][x]=vis[ky][kx];
	}
}
int main(){
	scanf("%d",&tc);
	for (int k=1;k<=tc;k++){
		scanf("%d%d",&h,&w);
		for (int i=0;i<h;i++) for (int j=0;j<w;j++) scanf("%d",&a[i][j]),vis[i][j]=' ';
		c='a';
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
				if (vis[i][j]==' ')
					dfs(i,j);
		printf("Case #%d:\n",k);
		for (int i=0;i<h;i++)
			for (int j=0;j<w;j++)
				printf("%c%c",vis[i][j],j==w-1?'\n':' ');
	}
	scanf("\n");
	return 0;
}
