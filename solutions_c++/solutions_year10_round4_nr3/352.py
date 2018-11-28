#include <iostream>
using namespace std;

const int maxn=1000;
int tot,tc,a[maxn][maxn],b[maxn][maxn],ans,n,cnt;

void init()
{
	memset(a,0,sizeof(a));
	scanf("%d",&n);
	for (int i=1;i<=n;++i)
	{
		int x1,y1,x2,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		for (int x=x1;x<=x2;++x)
			for (int y=y1;y<=y2;++y)
				a[x][y]=1;
	}
	cnt=0;
	for (int i=1;i<=100;++i)
		for (int j=1;j<=100;++j)
			cnt+=a[i][j];
	ans=0;
}

void work()
{
	while (cnt>0)
	{
		memset(b,0,sizeof(b));
		for (int i=1;i<=100;++i)
			for (int j=1;j<=100;++j)
			{
				if (a[i][j]==0)
				{
					if (a[i-1][j]==1 && a[i][j-1]==1) b[i][j]=1;
												else  b[i][j]=0;
				}
				else
				{
					if (a[i-1][j]==0 && a[i][j-1]==0) b[i][j]=0;
												else  b[i][j]=1;
				}
			}
		cnt=0;
		for (int i=1;i<=100;++i)
			for (int j=1;j<=100;++j)
			{
				a[i][j]=b[i][j];
				cnt+=b[i][j];
			}
		++ans;
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
    	printf("Case #%d: %d\n",tc,ans);
    }
    return 0;
}
