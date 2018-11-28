#include <cstdio>
#include <cstring>
int TT;
int N,M;
int grid[100][100];
char marca[100][100];
char qual;

int dy[]={-1,0,0,1};
int dx[]={0,-1,1,0};

char dfs(int y,int x) {
	if(marca[y][x]!=-1) {
		return marca[y][x];
	}
	int minimo=grid[y][x];
	int q=-1;
	for(int i=0;i<4;i++) {
		int py=y+dy[i];
		int px=x+dx[i];
		if(py>=0 and py<N and px>=0 and px<M and grid[py][px]<grid[y][x]) {
			if(q==-1 or minimo>grid[py][px])
				minimo=grid[py][px],q=i;
		}
	}
	if(q==-1) {
		marca[y][x]=qual;
		return qual++;
	}
	return marca[y][x]=dfs(y+dy[q],x+dx[q]);
}

int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		scanf("%d %d",&N,&M);
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				scanf("%d",&grid[i][j]);
		memset(marca,-1,sizeof(marca));

		qual=0;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++) if(marca[i][j]==-1)
				dfs(i,j);

		printf("Case #%d:\n",T);
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++)
				printf("%c ",marca[i][j]+'a');
			printf("\n");
		}
	}
	return 0;
}
