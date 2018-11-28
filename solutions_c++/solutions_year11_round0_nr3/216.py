#include <cstdio>
#include <cstring>
#define oo 1005
int f[2][1048581];
int g[2][1048581];
int N;
int a[oo];

inline void Readin()
{
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%d",a+i);
}

inline void Solve()
{
	int sum=0,sum2=0;
	int Max=(1<<20)-1;
	for (int i=1;i<=N;++i)
	{
		sum ^= a[i];
		sum2 += a[i];
	}
	memset(f,0,sizeof f);
	memset(g,63,sizeof g);
	for (int i=1;i<N;++i)
	{
		g[i+1&1][a[i]] <?= a[i];
		for (int j=0;j<=Max;++j)
		{
			f[i+1&1][j] >?= f[i&1][j];
			f[i+1&1][j^a[i]] >?=f[i&1][j] +a[i];
			
			g[i+1&1][j] <?= g[i&1][j];
			g[i+1&1][j^a[i]] <?= g[i&1][j] + a[i];
		}
	}
	int res=-1;
	for (int j=0;j<=Max;++j)
		if ((sum^j)==j)
		{
			res >?= f[N&1][j];
			res >?= sum2 - g[N&1][j];
		}
	if (res == -1) printf("NO\n");
	else printf("%d\n",res);
}

int main()
{
	//freopen("i.txt","r",stdin);
	int Test,Case=0;
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
