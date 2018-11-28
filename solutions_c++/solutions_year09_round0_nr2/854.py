#include<cstdio>
using namespace std;

const int DX[]={-1,0,0,1};
const int DY[]={0,-1,1,0};

int t[111][111],basen[111][111],id;

int dfs(int x,int y) {
	if(basen[x][y]!=0)
		return basen[x][y];
	int best=t[x][y],bestid=-1;
	for(int i=0;i<4;++i) {
		if(t[x+DX[i]][y+DY[i]]<best) {
			best=t[x+DX[i]][y+DY[i]];
			bestid=i;
		}
	}
	if(bestid==-1)
		return basen[x][y]=++id;
	return basen[x][y]=dfs(x+DX[bestid],y+DY[bestid]);
}

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		int h,w;
		scanf("%d%d",&h,&w);
		for(int i=0;i<h+2;++i)
			t[i][0]=t[i][w+1]=12345;
		for(int j=0;j<w+2;++j)
			t[0][j]=t[h+1][j]=12345;
		for(int i=1;i<=h;++i)
			for(int j=1;j<=w;++j)
				scanf("%d",t[i]+j);
		for(int i=0;i<h+2;++i)
			for(int j=0;j<w+2;++j)
				basen[i][j]=0;
		id=0;
		for(int i=1;i<=h;++i)
			for(int j=1;j<=w;++j)
				dfs(i,j);
		printf("Case #%d:\n",z);
		for(int i=1;i<=h;++i) {
			for(int j=1;j<=w;++j)
				printf("%c ",basen[i][j]-1+'a');
			puts("");
		}
	}
}
