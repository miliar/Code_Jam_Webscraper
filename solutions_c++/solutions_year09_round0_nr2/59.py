#include <cstdio>
#include <cstring>
#define maxn 105

int f[maxn][maxn],n,m,mark[maxn*maxn],map[maxn][maxn];
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};

inline bool range(int x,int y)
{
	return x>=0 && x<n && y>=0 && y<m;
}

inline void search(int x,int y)
{
	f[x][y]=x*m+y;
	int tarx=-1,tary;
	for (int k=0;k<4;++k)
	{
		int tx=x+dx[k],ty=y+dy[k];
		if (range(tx,ty) && map[tx][ty]<map[x][y])
		{
			if (tarx==-1 || map[tx][ty]<map[tarx][tary]) tarx=tx,tary=ty;
		}
	}
	if (tarx!=-1)
	{
		if (f[tarx][tary]==-1) search(tarx,tary);
		f[x][y]=f[tarx][tary];
	}
}

int main()
{
	freopen("B_large.in","r",stdin);
	freopen("B_large.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				scanf("%d",&map[i][j]);
		printf("Case #%d:\n",test);
		memset(f,-1,sizeof(f));
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
			if (f[i][j]==-1) search(i,j);
		
		memset(mark,-1,sizeof(mark));
		int cnt=0;
		for (int i=0;i<n;++i)
		{
			for (int j=0;j<m;++j)
			{
				if (mark[f[i][j]]==-1) mark[f[i][j]]=cnt++;
				printf("%c",'a'+mark[f[i][j]]);
				if (j+1<m) printf(" ");
			}
			puts("");
		}
	}
	return 0;
}
