#include <cstdio>
#include <algorithm>
#include <climits>
#include <cstdlib>
using namespace std;
const int maxn=110,maxc=260;
int a[maxn];
int del,ins,m,n;
void init()
{
	scanf("%d%d%d%d",&del,&ins,&m,&n);
	for(int i=0;i<n;i++) scanf("%d",&a[i]);
}
int solve()
{
	static int f[maxn][maxc]={};
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<256;j++)
		{
			int z=INT_MAX;
			for(int k=0;k<256;k++)
			{
				int t=min(abs(j-a[i-1]),del+ins);
				if(j==k)
				{
					t=min(t,del);
					z=min(z,t+f[i-1][k]);
				}
				else if(m>0) z=min(z,t+(abs(j-k)-1)/m*ins+f[i-1][k]);
			}
			f[i][j]=z;
		}
	}
	int ans=INT_MAX;
	for(int i=0;i<256;i++) ans=min(ans,f[n][i]);
	/*for(int i=1;i<=n;i++)
	{
		for(int j=0;j<10;j++) printf("%8d",f[i][j]);
		putchar('\n');
	}*/
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		init();
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
