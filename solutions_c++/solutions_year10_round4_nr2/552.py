#include <cstdio>
#include <cstdlib>
#include <cstring>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))



const	long long	oo=(long long)999999*99999999;
int	a[1505];
long long	c[15][1505],g[15][1505];
long long	f[15][1505][15];
int		TEST,t,p,n,i,j,k,l,jj;
long long 	Ans;


void	MINN(long long &A,long long B) { A=(A<B?A:B); }

int	main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	
	for (scanf("%d",&TEST),t=1;t<=TEST;++t)
	{
		scanf("%d",&p);
		n=1<<p;
		for (i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			g[0][i]=a[i];
		}
		for (i=1;i<=p;++i)
		for (j=0;j<n;j+=1<<i)
		{
			scanf("%d",&c[i][j]);
			//g[i][j]=MIN(g[i-1][j],g[i-1][j+(1<<(i-1))]);
		}
		
		memset(f,60,sizeof(f));
		for (i=0;i<n;++i) f[0][i][a[i]]=0;
		
		for (i=1;i<=p;++i)
		for (j=0;j<n;j+=1<<i) {
			jj=j+(1<<(i-1));
			for (k=0;k<=p;++k)
			for (l=0;l<=p;++l)
			{
				if (k!=0 && l!=0)
					MINN(f[i][j][MIN(k,l)-1],f[i-1][j][k]+f[i-1][jj][l]);
				MINN(f[i][j][MIN(k,l)],f[i-1][j][k]+f[i-1][jj][l]+c[i][j]);
			}
		}
		
		Ans=oo;
		for (k=0;k<=a[0];++k)
		MINN(Ans,f[p][0][k]);
		printf("Case #%d: %d\n",t,Ans);
	}
	
	return 0;
}
