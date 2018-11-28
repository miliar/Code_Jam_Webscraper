#include <cstdio>
#define oo 105
#define valid(x,y) ((x)>0&&(x)<=N&&(y)>0&&(y)<=M)
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};
int Test,Case;
int h[oo][oo],c[oo][oo];
int f[oo*oo],g[oo*oo];
int N,M;

inline void Readin()
{
	scanf("%d%d",&N,&M);
	for (int i=1;i<=N;++i)
		for (int j=1;j<=M;++j)
			scanf("%d",h[i]+j);
}

int find_set(int u)
{
	return u==f[u]?u:f[u]=find_set(f[u]);
}

inline void Union(int x,int y)
{
	f[find_set(x)]=find_set(y);
}

inline void Solve()
{
	for (int i=1,cnt=0;i<=N;++i)
		for (int j=1;j<=M;++j)
			c[i][j]=++cnt;
	for (int i=1;i<=N*M;++i)
	{
		f[i]=i;
		g[i]=0;
	}
	
	for (int i=1;i<=N;++i)
		for (int j=1;j<=M;++j)
		{
			int t=0,p;
			for (int k=0;k<4;++k)
				if (valid(i+dx[k],j+dy[k]) && h[i+dx[k]][j+dy[k]]<h[i][j] &&
				(!t || p>h[i+dx[k]][j+dy[k]]))
				{
					t=c[i+dx[k]][j+dy[k]];
					p=h[i+dx[k]][j+dy[k]];
				}
			if (t)
				Union(c[i][j],t);
		}
	
	for (int i=1,cnt=0;i<=N;++i)
		for (int j=1;j<=M;++j)
			if (!g[find_set(c[i][j])])
				g[find_set(c[i][j])]=++cnt;
	
	for (int i=1;i<=N;++i)
		for (int j=1;j<=M;++j)
			printf("%c%c",'a'+g[find_set(c[i][j])]-1,j==M?'\n':' ');
}	

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d:\n",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
