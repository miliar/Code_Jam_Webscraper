#include <cstdio>
#include <algorithm>
using namespace std;
int f[101][101];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T,t,n,m,p,i,j,x,y;
	scanf("%d",&T);
	for (t=1; t<=T; ++t)
	{
		scanf("%d%d%d",&n,&m,&p);
		memset(f,200,sizeof f);
		f[0][0]=0;
		for (i=1; i<=n; ++i)
		{
			scanf("%d",&x);
			if (x%3) y=x/3+1; else y=x/3;
			for (j=0; j<=m; ++j) f[i][j]=f[i-1][j]+(y>=p);
			if (x>=2 && x<=28)
			{
				if (x%3==2) y=x/3+2; else y=x/3+1;
				for (j=1; j<=m; ++j) f[i][j]=max(f[i-1][j-1]+(y>=p),f[i][j]);
			}
		}
		printf("Case #%d: %d\n",t,f[n][m]);
	}
	return 0;
}
