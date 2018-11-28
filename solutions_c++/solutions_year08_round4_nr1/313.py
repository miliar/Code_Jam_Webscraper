#include <cstdio>
#define nmax 10005

int ans[nmax][2];
int g[nmax],c[nmax];
int n;

void godown(int k)
{
	if (k+k>n)
	{
		ans[k][g[k]]=0;
		return ;
	}
	godown(k+k);
	godown(k+k+1);
	if (g[k]==1||c[k])
	{
		if (ans[k][1]>ans[k+k][1]+ans[k+k+1][1]+1-g[k]) ans[k][1]=ans[k+k][1]+ans[k+k+1][1]+1-g[k];
		if (ans[k][0]>ans[k+k][1]+ans[k+k+1][0]+1-g[k]) ans[k][0]=ans[k+k][1]+ans[k+k+1][0]+1-g[k];
		if (ans[k][0]>ans[k+k][0]+ans[k+k+1][1]+1-g[k]) ans[k][0]=ans[k+k][0]+ans[k+k+1][1]+1-g[k];
		if (ans[k][0]>ans[k+k][0]+ans[k+k+1][0]+1-g[k]) ans[k][0]=ans[k+k][0]+ans[k+k+1][0]+1-g[k];
	}
	if (g[k]==0||c[k])
	{
		if (ans[k][1]>ans[k+k][1]+ans[k+k+1][1]+g[k]) ans[k][1]=ans[k+k][1]+ans[k+k+1][1]+g[k];
		if (ans[k][1]>ans[k+k][1]+ans[k+k+1][0]+g[k]) ans[k][1]=ans[k+k][1]+ans[k+k+1][0]+g[k];
		if (ans[k][1]>ans[k+k][0]+ans[k+k+1][1]+g[k]) ans[k][1]=ans[k+k][0]+ans[k+k+1][1]+g[k];
		if (ans[k][0]>ans[k+k][0]+ans[k+k+1][0]+g[k]) ans[k][0]=ans[k+k][0]+ans[k+k+1][0]+g[k];
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T,i,j,k,v;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&v);
		for(i=1;i<=n;i++) ans[i][0]=ans[i][1]=1000000;
		for(i=1;i<=(n-1)/2;i++) scanf("%d%d",&g[i],&c[i]);
		for(i=(n-1)/2+1;i<=n;i++) scanf("%d",&g[i]);

		godown(1);

		printf("Case #%d: ",t);
		if (ans[1][v]==1000000) puts("IMPOSSIBLE"); else printf("%d\n",ans[1][v]);

	}
	return 0;
}