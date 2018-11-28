#include <cstdio>
#include <cmath>
using namespace std;
#define min(a,b) (a<b?a:b)
const int maxn=505;
double sx[maxn][maxn],sy[maxn][maxn],s[maxn][maxn],a[maxn][maxn],cx,cy,Sx,Sy;
int test,n,m,d,ans;
char S[maxn];

double Getx(int x1,int y1,int x2,int y2)
{
	return sx[x2][y2]-sx[x1-1][y2]-sx[x2][y1-1]+sx[x1-1][y1-1];
}

double Gety(int x1,int y1,int x2,int y2)
{
	return sy[x2][y2]-sy[x1-1][y2]-sy[x2][y1-1]+sy[x1-1][y1-1];
}

double Gets(int x1,int y1,int x2,int y2)
{
	return s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1];
}

double GetX(int i,int j)
{
	return (double)(i-0.5-cx)*a[i][j];
}

double GetY(int i,int j)
{
	return (double)(j-0.5-cy)*a[i][j];
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		scanf("%d%d%d",&n,&m,&d);
		for (int i=1;i<=n;i++)
		{
			scanf("%s",S+1);
			for (int j=1;j<=m;j++)
				a[i][j]=d+S[j]-'0';
		}
		for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
		{
			s[i][j]=s[i][j-1]+s[i-1][j]-s[i-1][j-1]+a[i][j];
			sx[i][j]=sx[i][j-1]+sx[i-1][j]-sx[i-1][j-1]+(double)(i-0.5)*a[i][j];
			sy[i][j]=sy[i][j-1]+sy[i-1][j]-sy[i-1][j-1]+(double)(j-0.5)*a[i][j];
		}
		ans=0;
		for (int i=2;i<=n-1;i++)
		for (int j=2;j<=m-1;j++)
		{
			cx=(double)(i-0.5);
			cy=(double)(j-0.5);
			Sx=Sy=0;
			for (int k=1;k<=min(min(n-i,m-j),min(i-1,j-1));k++)
			{
				Sx=Getx(i-k,j-k,i+k,j+k)-cx*Gets(i-k,j-k,i+k,j+k)-GetX(i-k,j-k)-GetX(i-k,j+k)-GetX(i+k,j-k)-GetX(i+k,j+k);
				Sy=Gety(i-k,j-k,i+k,j+k)-cy*Gets(i-k,j-k,i+k,j+k)-GetY(i-k,j-k)-GetY(i-k,j+k)-GetY(i+k,j-k)-GetY(i+k,j+k);
				if (fabs(Sx)<=1e-9&&fabs(Sy)<=1e-9&&k+k+1>ans) ans=k+k+1;
			}
		}
		for (int i=2;i<=n-2;i++)
		for (int j=2;j<=m-2;j++)
		{
			cx=(double)(i);
			cy=(double)(j);
			Sx=Sy=0;
			for (int k=2;k<=min(min(n-i,m-j),min(i,j));k++)
			{
				Sx=Getx(i-k+1,j-k+1,i+k,j+k)-cx*Gets(i-k+1,j-k+1,i+k,j+k)-GetX(i-k+1,j-k+1)-GetX(i-k+1,j+k)-GetX(i+k,j-k+1)-GetX(i+k,j+k);
				Sy=Gety(i-k+1,j-k+1,i+k,j+k)-cy*Gets(i-k+1,j-k+1,i+k,j+k)-GetY(i-k+1,j-k+1)-GetY(i-k+1,j+k)-GetY(i+k,j-k+1)-GetY(i+k,j+k);
				if (fabs(Sx)<=1e-9&&fabs(Sy)<1e-9&&k+k>ans) ans=k+k;
			}
		}
		printf("Case #%d: ",kase);
		if (!ans) printf("IMPOSSIBLE\n"); else printf("%d\n",ans);
	}
	
	return 0;
}
