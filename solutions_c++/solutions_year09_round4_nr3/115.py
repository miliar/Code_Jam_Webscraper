#include <cstdio>
#include <cstring>
#define oo 105
#define kk 30
bool map[oo][oo];
int p[oo][kk];
int N,Test,Case,K;
bool mk[oo];
int y[oo];

inline void Readin()
{
	scanf("%d%d",&N,&K);
	for (int i=1;i<=N;++i)
		for (int j=1;j<=K;++j)
			scanf("%d",p[i]+j);
}

inline void Prepare()
{
	memset(map,0,sizeof map);
	for (int i=1;i<=N;++i)
		for (int j=1;j<=N;++j)
		{
			map[i][j]=true;
			for (int k=1;k<=K;++k)
				map[i][j]&=(p[i][k]>p[j][k]);
		}
}

bool Extend_Path(int u)
{
	for (int i=1;i<=N;++i)
		if (map[u][i] && !mk[i])
		{
			mk[i]=true;
			if (!y[i] || Extend_Path(y[i]))
			{
				y[i]=u;
				return true;
			}
		}
	return false;
}

inline void Solve()
{
	int ans=N;
	memset(y,0,sizeof y);
	for (int i=1;i<=N;++i)
	{
		memset(mk,0,sizeof mk);
		ans-=Extend_Path(i);
	}
	
	printf("%d\n",ans);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Prepare();
		Solve();
	}
	
	return 0;
}
