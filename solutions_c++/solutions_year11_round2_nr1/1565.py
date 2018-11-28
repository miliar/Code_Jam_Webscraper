#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;

int T,N;

char battle[128][128];
int wp[128][2];
double owp[128];
double oowp[128];
int main()
{
	freopen("data.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int t;
	scanf("%d",&T);
	for(t=1;t<=T;++t)
	{
		scanf("%d",&N);
		int i,j;
		for(i=0;i<N;++i)
		{
			scanf("%s",battle[i]);
			//printf("%s\n",battle[i]);
		}
		for(i=0;i<N;++i)
		{
			int cnt=0;
			int win=0;
			for(j=0;j<N;++j)
			{
				if(battle[i][j]=='1')
				{
					++cnt;
					++win;
				}
				else if(battle[i][j]=='0')
					++cnt;
			}
			wp[i][0]=win;
			wp[i][1]=cnt;
		}
		for(i=0;i<N;++i)
		{
			double ans=0;
			int cnt=0;
			for(j=0;j<N;++j)
			{
				if(battle[i][j]=='1')
				{
					ans+=(wp[j][0]+0.0)/(wp[j][1]-1.0);
					cnt++;
				}
				else if(battle[i][j]=='0')
				{
					ans+=(wp[j][0]-1.0)/(wp[j][1]-1.0);
					cnt++;
				}
			}
			ans/=cnt;
			owp[i]=ans;
		}
		for(i=0;i<N;++i)
		{
			double ans=0;
			int cnt=0;
			for(j=0;j<N;++j)
			{
				if(battle[i][j]!='.' )
				{
					ans+=owp[j];
					++cnt;
				}
			}
			oowp[i]=ans/cnt;
		}
		printf("Case #%d:\n",t);
		for(i=0;i<N;++i)
		{
			printf("%lf\n",0.25*wp[i][0]/(wp[i][1])+0.5*owp[i]+0.25*oowp[i]);
		}
	}

	return 0;
}
