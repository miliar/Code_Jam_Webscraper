#include <iostream>
#define lim 1000000000
using namespace std;

const int maxp=10;
int tot,tc,M[1<<maxp],f[1<<maxp][maxp+1][maxp+1],c[1<<maxp][maxp+1],P,ans;

void init()
{
	ans=0;
	scanf("%d",&P);
	for (int i=0;i<(1<<P);++i)
		for (int x=0;x<=P;++x)
			for (int y=0;y<=P;++y) f[i][x][y]=lim;
	memset(c,0,sizeof(c));
	for (int i=0;i<1<<P;++i)
	{
		scanf("%d",&M[i]);
		M[i]=P-M[i];
		f[i][0][M[i]]=0;
	}
	for (int i=1;i<=P;++i)
		for (int j=0;j<1<<P;j+=(1<<i))
			scanf("%d",&c[j][i]);
}

void work()
{
	for (int j=1;j<=P;++j)
		for (int i=0;i<(1<<P);i+=(1<<j))
			for (int k=0;k<=P;++k)
			{
				for (int x=0;x<=k+1;++x)
					for (int y=0;y<=k+1;++y)
					{
						f[i][j][k]=min(f[i][j][k],f[i][j-1][x]+f[i+(1<<(j-1))][j-1][y]+c[i][j]);
						if (x<=k && y<=k)
							f[i][j][k]=min(f[i][j][k],f[i][j-1][x]+f[i+(1<<(j-1))][j-1][y]);
					}
			}
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
    	printf("Case #%d: %d\n",tc,f[0][P][0]);
    }
    return 0;
}
