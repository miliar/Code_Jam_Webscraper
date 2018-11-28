#include <stdio.h>

int x[200][200];
int y[200][200];
int gc,mgc,n;
int g[200][200];
int p[200];

int go(int x)
{
	int i,j;
	if (x==n) return 1;
	for (i=0;i<gc;++i)
	{
		for (j=0;j<p[i];++j) if (y[x][g[i][j]]==0) break;
		if (j==p[i])
		{
			g[i][p[i]]=x;
			++p[i];
			if (go(x+1)) return 1;
			--p[i];
		}
	}
	if (gc<mgc)
	{
		p[gc]=1;
		g[gc][0]=x;
		++gc;
		if (go(x+1)) return 1;
		--gc;
	}
	return 0;
}

int main()
{
	int ni=1,i,j,k,l,r;
	scanf("%d",&n);
	while (scanf("%d %d",&n,&k)==2)
	{
		for (i=0;i<n;++i) for (j=0;j<k;++j) scanf("%d",x[i]+j);
		for (i=0;i<n;++i) for (j=0;j<n;++j) y[i][j]=0;
		for (i=0;i<n;++i) for (j=0;j<n;++j) 
		{
			for (l=0;l<k;++l) if (x[i][l]<=x[j][l]) break;
			if (l==k) y[i][j]=y[j][i]=1;
		}
		for (mgc=1;mgc<=n;++mgc) 	
		{
			gc=0;
			if (go(0)) break;
		}
		printf("Case #%d: %d\n",ni++,mgc);
	}
	return 0;
}
