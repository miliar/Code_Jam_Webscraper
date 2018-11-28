#include <stdio.h>
#include <string.h>

#define N 2100

int u[N],v[N],col[N];

int x[N][N];
int xn;
long long n;

int go(int s, int m)
{
	int i,j;
	if (s==n)
	{
		for (i=0;i<xn;++i)
		{
			memset(v+1,0,m*sizeof(int));
			for (j=0;j<n;++j) if (x[i][j]==1) v[u[j]]=1;
			for (j=1;j<=m;++j) if (v[j]==0) break;
			if (j<=m) break;
		}
		if (i<xn)
		{
			return 0;
		} else
		{
			memcpy(col,u,n*sizeof(int));
			return 1;
		}
	}
	for (i=1;i<=m;++i) 
	{
		u[s]=i;
		if (go(s+1,m)) return 1;
	}
	return 0;
}

int main()
{
	long long ca=0,nn,in,i,j,k,s,m,l;
	scanf("%lld",&nn);
	for (in=0;in<nn;++in)
	{
		scanf("%lld %lld",&n,&m);
		for (i=0;i<m;++i) scanf("%d",u+i);
		for (i=0;i<m;++i) scanf("%d",v+i);
		xn=1;
		for (i=0;i<n;++i) x[0][i]=1;
		for (i=0;i<m;++i) 
		{
			--u[i];--v[i];
			for (j=0;j<xn;++j) if (x[j][u[i]] && x[j][v[i]]) break;
			s=0;
			for (k=0;k<n;++k)
			{
				if (x[j][k])
				{
					if (k==u[i] || k==v[i])
					{
						x[xn][k]=1;
						s=1-s;
					} else
					{
						if (s) x[xn][k]=0; else
						{
							x[xn][k]=1;
							x[j][k]=0;
						}
					}
				} else x[xn][k]=0;
			}
			++xn;
		}
		for (i=1;go(0,i);++i) ;
		printf("Case #%lld: %lld\n",++ca,i-1);
		for (i=0;i<n;++i) printf("%d ",col[i]);
		printf("\n");
	}
	return 0;
}
