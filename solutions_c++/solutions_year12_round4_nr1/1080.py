#include <stdio.h>
#include <math.h>

const int N=10010;
int TC,tc;
int n,d[N+1],l[N+1],s;
int a[N+1][N+1];
int m[N+2],x; bool v[N+2];

int main()
{
	int i,j,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	for(scanf("%d",&TC),tc=1;tc<=TC;++tc)
	{
		scanf("%d",&n);
		for(i=1;i<=n;++i)
			scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&d[++n]);
		for(i=1;i<=n-1;++i)
			for(j=1;j<=n;++j)
				if(i!=j && (k=abs(d[i]-d[j]))<=l[i])
					a[i][j]=k;
				else
					a[i][j]=0;

		for(i=1;i<=n;++i)
			m[i]=-1,v[i]=0;
		m[1]=d[1];
		for(i=1;i<=n;++i)
		{
			x=0;
			if(!v[i] && (x==0 || m[i]>m[x]))
				x=i;
			if(m[x]==-1) break;
			v[x]=1;
			for(j=1;j<=n;++j)
				if(a[x][j] && a[x][j]<=m[x] && a[x][j]>m[j])
					m[j]=a[x][j];
		}
		printf("Case #%d: ",tc);
		printf(m[x]==-1?"NO\n":"YES\n");
	}
	return 0;
}