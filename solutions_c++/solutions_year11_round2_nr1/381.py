#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;
double wp[1005],owp[1005],oowp[1005];
char a[1005][1005];

int main()
{
	int ca=0;
	int cas;
	int n,i,j,k;
	int cnt,ans;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	while (cas--)
	{
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		scanf("%d",&n);
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
				if (j==1)
				scanf(" %c",&a[i][j]);
				else scanf("%c",&a[i][j]);
		for (i=1;i<=n;i++)
		{
			cnt=0;
			ans=0;
			for (j=1;j<=n;j++)
				if (i!=j)
				{
					if (a[i][j]!='.')
					{
						cnt++;
						if (a[i][j]=='1')		ans++;
					}
				
				}
			wp[i]=double(ans)/cnt;
		}
		
		for (i=1;i<=n;i++)
		{
			double re=0;
			int q=0;
			for (j=1;j<=n;j++)
				if (j!=i)
				if (a[i][j]!='.')
				{
					q++;
					cnt=0;
					ans=0;
					for (k=1;k<=n;k++)
						if (i!=k&&k!=j)
						if (a[j][k]!='.')
						{
							cnt++;
							if (a[j][k]=='1') ans++;
						}
					re+=double(ans)/cnt;
				}
			owp[i]=re/q;
		}

		for (i=1;i<=n;i++)
		{
			cnt=0;
			for (j=1;j<=n;j++)
				if (i!=j)
				if (a[i][j]!='.')
				{
				oowp[i]+=owp[j];
				cnt++;
				}
			oowp[i]/=cnt;
		}
		
		ca++;
		printf("Case #%d:\n",ca);
		for (i=1;i<=n;i++)
		{
			printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
return 0;
}