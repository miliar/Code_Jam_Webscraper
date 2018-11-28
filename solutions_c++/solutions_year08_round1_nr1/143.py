#include <cstdio>
#include <memory>
#define oo 805
#define inf 100000000000000000LL
long long w[oo][oo];
int a[oo],b[oo];
int x[oo],y[oo];
long long lx[oo],ly[oo];
bool mx[oo],my[oo];
int N;
long long ans;
int T,Case;

inline bool Extend_Path(int u)
{
	mx[u]=true;
	for (int i=1;i<=N;++i)
		if (w[u][i]==lx[u]+ly[i] && !my[i])
		{
			my[i]=true;
			if (!y[i] || Extend_Path(y[i]))
			{
				y[i]=u;
				return true;
			}
		}
	return false;
}

inline void Modify()
{
	long long delta=inf;
	for (int i=1;i<=N;++i)
	if (mx[i])
		for (int j=1;j<=N;++j)
		if (!my[j])
			delta<?=w[i][j]-lx[i]-ly[j];
	
	for (int i=1;i<=N;++i)
		if (mx[i]) lx[i]+=delta;
	for (int j=1;j<=N;++j)
		if (my[j]) ly[j]-=delta;
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	for (scanf("%d",&T);T;T--)
	{
		scanf("%d",&N);
		for (int i=1;i<=N;++i)
			scanf("%d",&a[i]);
		for (int i=1;i<=N;++i)
			scanf("%d",&b[i]);
		for (int i=1;i<=N;++i)
			for (int j=1;j<=N;++j)
				w[i][j]=a[i]*b[j];
		
		for (int i=1;i<=N;++i)
		{
			lx[i]=w[i][1];
			for (int j=2;j<=N;++j)
				lx[i]<?=w[i][j];
		}
		
		memset(y,0,sizeof y);
		memset(ly,0,sizeof ly);
		for (int i=1;i<=N;++i)
			while (true)
			{
				memset(mx,0,sizeof mx);
				memset(my,0,sizeof my);
				if (Extend_Path(i)) break;
				Modify();
			}
		
		ans=0;
		for (int i=1;i<=N;++i)
			ans+=w[y[i]][i];
		
		printf("Case #%d: %I64d\n",++Case,ans);
	}
	return 0;
}
	
