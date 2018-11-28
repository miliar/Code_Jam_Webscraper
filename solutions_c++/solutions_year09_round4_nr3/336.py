#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

vector<int>v[200];
vector<int>w;
int T,t;
int u[400];
int i,j,n,m,k,ans;
int a[200][200],b[400][400],c[400][400];

bool dfs(int ne)
{
	if(ne==n-1)
		return 1;
	u[ne]=1;
	int i;
	for(i=0;i<n;i++)
		if(!u[i] && b[ne][i]>=1+c[ne][i] && dfs(i))
		{
			c[ne][i]++;
			c[i][ne]--;
			return 1;
		}
	return 0;
}


int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++t);
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			v[i].resize(m);
			for(j=0;j<m;j++)
				scanf("%d",&v[i][j]);
		}
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				a[i][j]=0;
				for(k=0;k<m;k++)
					if(v[i][k]>=v[j][k])
						break;
				if(k==m)
					a[i][j]=1;
			}
		for(i=0;i<2*n+2;i++)
			for(j=0;j<2*n+2;j++)
				b[i][j]=c[i][j]=0;
		for(i=0;i<n;i++)
		{
			b[0][i+1]=1;
			b[i+1+n][2*n+1]=1;
		}
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(a[i][j])
					b[i+1][j+1+n]=1;
		n=2*n+2;
		ans=0;
		memset(u,0,sizeof(u));
		while(dfs(0))
		{
			memset(u,0,sizeof(u));
			ans++;
		}
		printf("%d\n",n/2-1-ans);
	}
	return 0;
}