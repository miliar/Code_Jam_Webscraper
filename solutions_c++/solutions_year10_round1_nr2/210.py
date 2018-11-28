#include <iostream>
#define lim 1000000
using namespace std;

const int maxn=100+10,maxv=300;
int tot,a[maxn],f[maxn][maxv],D,I,M,n,ans;

void init()
{
	scanf("%d%d%d%d",&D,&I,&M,&n);
	for (int i=1;i<=n;++i)
		scanf("%d",&a[i]);
	fill(&f[0][0],&f[n][257],lim);
	f[0][256]=0;ans=lim;
}

void work()
{
	for (int i=1;i<=n;++i)
	{
		//change
		for (int j=0;j<=255;++j)
		{
			f[i][j]=min(f[i][j],f[i-1][256]+abs(j-a[i]));
			for (int k=0;k<=255;++k)
			{
				int t;
				if (M!=0)
				{
					t=abs(j-k)/M-1;
					if (abs(j-k)%M!=0) ++t;
					if (t<0) t=0;
					f[i][j]=min(f[i][j],f[i-1][k]+I*t+abs(j-a[i]));
				}
				else
				{
					if (j==k) t=0;
						else  t=lim;
					f[i][j]=min(f[i][j],f[i-1][k]+t+abs(j-a[i]));
				}
			}
		}
		//delete
		for (int j=0;j<=256;++j)
			f[i][j]=min(f[i][j],f[i-1][j]+D);
	}
	for (int i=0;i<=256;++i)
		ans=min(f[n][i],ans);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&tot);
	for (int tc=1;tc<=tot;++tc)
	{
		init();
		work();
		printf("Case #%d: %d\n",tc,ans);
	}
    return 0;
}
