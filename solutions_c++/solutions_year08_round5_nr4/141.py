#include <cstdio>
#include <cstring>
int i,j,k,s,t,n,m;
int a[200][200];
int b[200][200];
int T,I;
main()
{
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d%d%d",&n,&m,&k);
		memset(b,0,sizeof b);
		for (i=1;i<=k;++i)
		{
			scanf("%d%d",&s,&t);
			b[s-1][t-1]=1;
		}
		memset(a,0,sizeof a);
		a[0][0]=1;
		for (i=0;i<n;++i)
		for (j=0;j<m;++j)
		if (b[i][j]==false)
		{
			if (i-1>=0 && j-2>=0)
				a[i][j]+=a[i-1][j-2];
			a[i][j]%=10007;
			if (i>=2 && j>=1)
				a[i][j]+=a[i-2][j-1];
			a[i][j]%=10007;
		}
		else a[i][j]=0;
		printf("Case #%d: %d\n",++I,a[n-1][m-1]);
	}
	return 0;
}
