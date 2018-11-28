#include <cstdio>
#define nmax 10
#define mmax 100

int l[mmax],a[mmax][mmax],b[mmax][mmax];
int ans[nmax],min1;

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,n,m,i,j,k,q,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)
		{
			scanf("%d",&l[i]);
			for(j=0;j<l[i];j++) 
			{
				scanf("%d%d",&a[i][j],&b[i][j]);
				--a[i][j];
			}
		}
		min1=n+1;

		for(k=0;k<(1<<n);k++)
		{
			for(i=0,q=0;i<n;i++) q+=((1<<i)&k?1:0);
			for(i=0;i<m;i++)
			{
				for(j=0;j<l[i];j++)
					if ((((1<<a[i][j])&k)?1:0)==b[i][j]) break;
				if (j==l[i]) break;
			}
			if (i==m && min1>q)
			{
				min1=q;
				for(i=0;i<n;i++)
					ans[i]=((1<<i)&k?1:0);
			}
		}

		printf("Case #%d: ",t);
		if (min1==n+1) puts("IMPOSSIBLE"); else
		{
			for(i=0;i<n;i++) printf("%d ",ans[i]);
			puts("");
		}
	}
	return 0;
}