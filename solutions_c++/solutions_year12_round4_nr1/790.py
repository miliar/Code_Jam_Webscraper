#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;
const int N = 10010;
int a[N][2];
int vis[N],D;
int main(void)
{
	int T,n;
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	int g=0;
	while(T--)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d%d",&a[i][0],&a[i][1]);
		}
		scanf("%d",&D);
		a[n+1][0]=D;
		a[n+1][1]=100;
		memset(vis,0,sizeof(vis));
		vis[1]=a[1][0];
		for (int i=1;i<=n;i++)
		for (int j=i+1;j<=n+1;j++)
		{
				
			if (a[i][0]+vis[i]>=a[j][0])
			{
				int d=a[j][0]-a[i][0];
				vis[j]=max(vis[j],min(d,a[j][1]));
			}
			else break;	
		}	
		if(vis[n+1])
		{
			printf("Case #%d: YES\n",++g);
		}
		else
		{
			printf("Case #%d: NO\n",++g);
		}				
						
	}
	return 0;
}
