#include <cstdio>
#include <algorithm>

int d[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int c,n,m,AC,h[105][105],sx[105][105],sy[105][105];
char v[105][105];

void cal(int x,int y){
	int mn,tx,ty,fx,fy;
	mn=(1<<30);
		for (int k=0;k<4;k++){
		tx=x+d[k][0];
		ty=y+d[k][1];
			if (tx<1||ty<1||tx>n||ty>m) continue;
			if (h[tx][ty]<mn) mn=h[tx][ty],fx=tx,fy=ty;
		}
		if (mn<h[x][y]){
			if (!sx[fx][fy]) cal(fx,fy);
		sx[x][y]=sx[fx][fy];
		sy[x][y]=sy[fx][fy];
		}
		else sx[x][y]=x,sy[x][y]=y;
}

int main(){
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
	scanf("%d%d",&n,&m);
	memset(v,'$',sizeof(v));
	memset(sx,0,sizeof(sx));
	memset(sy,0,sizeof(sy));	
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++) scanf("%d",&h[i][j]);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				if (!sx[i][j]) cal(i,j);
	printf("Case #%d:\n",tc);
	AC='a';
		for (int i=1;i<=n;i++){
			for (int j=1;j<=m;j++){
				if (v[sx[i][j]][sy[i][j]]=='$') v[sx[i][j]][sy[i][j]]=AC++;
			printf("%c ",v[sx[i][j]][sy[i][j]]);
			}
		printf("\n");
		}
	}
	return 0;
}
