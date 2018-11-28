#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=100+10;
int n,m,p1[maxn],p2[maxn];
long long d1[maxn],d2[maxn],f[maxn][maxn],ans;
void init()
{
	cin >>n>>m;
	for (int i=1;i<=n;i++)
		cin >>d1[i]>>p1[i];
	for (int i=1;i<=m;i++)
		cin >>d2[i]>>p2[i];
}
long long getmin(long long a,long long b)
{
	if (a<b)
		return a;
	return b;
}
long long getmax(long long a,long long b)
{
	if (a>b)
		return a;
	return b;
}
void solve()
{
	for (int i=0;i<=n;i++)
		for (int j=0;j<=m;j++)
			f[i][j]=0;
	long long sum1,sum2;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
		{
			f[i][j]=getmax(f[i-1][j],f[i][j-1]);
			if (p1[i]==p2[j])
			{
				sum1=0;
				for (int ii=i;ii>0;ii--)
				{
					if (p1[ii]==p1[i])
						sum1+=d1[ii];
					sum2=0;
					for (int jj=j;jj>0;jj--)
					{
						if (p2[jj]==p2[j])
							sum2+=d2[jj];
						f[i][j]=getmax(f[i][j],f[ii-1][jj-1]+getmin(sum1,sum2));		
					}
				}		
			}
		}	
	ans=f[n][m];	
}
void out(int t)
{
	cout <<"Case #"<<t<<": "<<ans<<endl;
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;
	cin >>t;
	for (int i=1;i<=t;i++)
	{
		init();
		solve();
		out(i);
	}
	return 0;
}
