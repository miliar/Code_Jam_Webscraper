#include<cstdio>

const int maxn=100+10;
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};

int h[maxn][maxn];
int ID[maxn][maxn];
int ch[maxn][maxn];
int n,m;
int test;
int cases;

void dfs(int u,int v)
{
	if (ID[u][v]>=0) return;
	int x=u,y=v;
	for (int i=0;i<4;i++)
	{
		int _u=u+dx[i];
		int _v=v+dy[i];
		if (_u>=0 && _u<n && _v>=0 && _v<m && h[_u][_v]<h[x][y])
			x=_u,y=_v;
	}
	if (x==u && y==v) ID[u][v]=u*m+v;
	else
	{
		dfs(x,y);
		ID[u][v]=ID[x][y];
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	
	for (scanf("%d",&test);test;test--)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			scanf("%d",&h[i][j]),ID[i][j]=ch[i][j]=-1;
		for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
		if (ID[i][j]==-1) dfs(i,j);
		
		printf("Case #%d:\n",++cases);
		int tmp='a';
		for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
		{
			int u=ID[i][j]/m;
			int v=ID[i][j]%m;
			if (ch[u][v]==-1) ch[u][v]=tmp++;
			printf("%c%c",ch[u][v],(j==m-1)?'\n':' ');
		}
	}
}