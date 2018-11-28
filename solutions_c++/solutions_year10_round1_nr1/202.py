#include <iostream>
using namespace std;

const int maxn=50+10,way[4][2]={{1,0},{0,1},{1,1},{1,-1}};
int tot,n,k;
char a[maxn][maxn],b[maxn][maxn];
bool red,blue;

void init()
{
	scanf("%d%d",&n,&k);
	gets(a[0]);
	for (int i=1;i<=n;++i)
	{
		gets(a[i]);
		for (int j=n;j>0;--j) a[i][j]=a[i][j-1];
	}
	red=blue=false;
}

bool check(int x,int y)
{
	if (x==0 || y==0) return false;
	if (x>n || y>n) return false;
	if (b[x][y]=='.') return false;
	return true;
}

void work()
{
	for (int i=1;i<=n;++i)
		for (int j=1;j<=n;++j)
			b[i][j]=a[n+1-j][i];
	for (int i=n;i>0;--i)
		for (int j=1;j<=n;++j)
		{
			if (b[i][j]=='.') continue;
			int k=i;
			while (k<n && b[k+1][j]=='.')
			{
				b[k+1][j]=b[k][j];
				b[k][j]='.';
				++k;
			}
		}
	for (int i=1;i<=n;++i)
		for (int j=1;j<=n;++j)
		{
			if (b[i][j]=='.') continue;
			for (int r=0;r<4;++r)
			{
				int x=i,y=j,cnt=0;
				while (check(x,y))
				{
					if (b[x][y]!=b[i][j]) break;
					++cnt;
					x+=way[r][0];y+=way[r][1];
				}
				if (cnt>=k)
				{
					if (b[i][j]=='R') red=true;
					if (b[i][j]=='B') blue=true;
				}
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
		printf("Case #%d: ",tc);
		if (red && blue) printf("Both\n");
		if (red && !blue) printf("Red\n");
		if (!red && blue) printf("Blue\n");
		if (!red && !blue) printf("Neither\n");
	}
    return 0;
}
