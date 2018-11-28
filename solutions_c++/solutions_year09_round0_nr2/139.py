#include<cstdio>
#include<cstring>

int cnt,size,c,test,n,m,s[105][105],color[105][105],link[105][105],
	dx[4]={-1,0,0,1},
	dy[4]={0,-1,1,0},
	T[30],list[105][105],next[11025];
char ans[105][105];
struct TQue
{
	int x,y;
}Q[11025],e[11025];

inline void AddEdge(int a,int b,int u,int v)
{
	e[++size].x=u;e[size].y=v;next[size]=list[a][b];list[a][b]=size;
}
inline void Floodfill(int x,int y)
{	
	color[x][y]=++c;
	int h=0,r=1;
	Q[r].x=x;Q[r].y=y;
	for (;h<r;)
	{
		int x=Q[++h].x,y=Q[h].y;
		for (int p=list[x][y];p;p=next[p])
		{
			color[e[p].x][e[p].y]=c;
			Q[++r].x=e[p].x;Q[r].y=e[p].y;
		}
	}
}
int main()
{
	freopen("water.in","r",stdin);
	freopen("water.out","w",stdout);
	scanf("%d",&test);
	int cnt=1;
	for (;test;--test,++cnt)
	{
		printf("Case #%d:\n",cnt);
		scanf("%d%d",&n,&m);
		memset(link,-1,sizeof(link));
		memset(color,0,sizeof(color));
		memset(list,0,sizeof(list));
		size=0;c=0;
		for (int i=1;i<=n;++i)
		for (int j=1;j<=m;++j) scanf("%d",&s[i][j]);
		for (int i=1;i<=n;++i)
		for (int j=1;j<=m;++j)
		{
			int ans=-1,oo=s[i][j];
			for (int k=0;k<4;++k)
			{
				int xx=i+dx[k],yy=j+dy[k];
				if (xx>=1 && xx<=n && yy>=1 && yy<=m && s[xx][yy]<oo) oo=s[xx][yy],ans=k;
			}
			link[i][j]=ans;
			if (ans!=-1) AddEdge(i+dx[ans],j+dy[ans],i,j);
		}
		memset(T,-1,sizeof(T));
		int now=0;
		for (int i=1;i<=n;++i)
		for (int j=1;j<=m;++j) if (link[i][j]==-1) Floodfill(i,j);
		for (int i=1;i<=n;++i)
		for (int j=1;j<=m;++j)
		{
			if (T[color[i][j]]==-1) T[color[i][j]]=now++;
			ans[i][j]='a'+T[color[i][j]];
		}
		for (int i=1;i<=n;++i)
		{
			for (int j=1;j<=m;++j)
			{
				printf("%c",ans[i][j]);
				if (j<m) printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
}
