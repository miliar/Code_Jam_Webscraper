#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=200+10;
const int maxm=10000+100;
const int maxnum=1000000000;
int m,n,tot,sum[maxm],f[maxn][maxn],a[maxn],d[maxn],ans;
void init()
{
	cin >>m>>n;
	memset(sum,0,sizeof(sum));
	for (int i=0;i<n;i++)
	{
		cin >>a[i];
		a[i]--;
		sum[a[i]-1]=1;
		sum[a[i]+1]=1;
	}
	sum[0]=sum[m-1]=1;
}
void solve()
{
	tot=0;
	for (int i=0;i<m;i++)
		if (sum[i])
			d[tot++]=i;
	for (int i=1;i<m;i++)
		sum[i]+=sum[i-1];
	for (int i=0;i<m;i++)
		sum[i]--;
	memset(f,0,sizeof(f));
	for (int i=tot-1;i>=0;i--)
		for (int j=i;j<tot;j++)
		{
			f[i][j]=maxnum;
			for (int k=0;k<n;k++)
				if (a[k]>=d[i] && a[k]<=d[j])
					f[i][j]=min(f[i][j],f[i][sum[a[k]-1]]+f[sum[a[k]+1]][j]+d[j]-d[i]);			
			if (f[i][j]==maxnum)
				f[i][j]=0;
		}				
	ans=f[0][tot-1];
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
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
