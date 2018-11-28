#include<cstdio>
#include<cstring>

int T,n,m,h[107][107],tot,mn,mi,X,Y;
char id[107][107];

const int dx[]={-1,0,0,+1};
const int dy[]={0,-1,+1,0};

char dfs(int x,int y)
{
	if (id[x][y]) return id[x][y];
	mi=-1;mn=~0U>>1;
	for (int i=0;i<4;++i){
		X=dx[i]+x;Y=dy[i]+y;
		if (X>=0 && X<n && Y>=0 && Y<m)
			if (h[X][Y]<h[x][y] && h[X][Y]<mn) mn=h[X][Y],mi=i;
	}
	if (mi==-1) return id[x][y]=tot++;
	return id[x][y]=dfs(x+dx[mi],y+dy[mi]);
}

int main()
{
	scanf("%d",&T);
	for (int test=1;test<=T;++test){
		scanf("%d%d",&n,&m);tot='a';
		memset(id,0,sizeof(id));
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j) scanf("%d",h[i]+j);
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j) if (!id[i][j]) dfs(i,j);
		printf("Case #%d:\n",test);
		for (int i=0;i<n;++i){
			for (int j=0;j<m-1;++j) printf("%c ",id[i][j]);
			printf("%c\n",id[i][m-1]);
		}
	}
	return 0;
}

