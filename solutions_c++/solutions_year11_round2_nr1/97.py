#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

char pot[150][150];
double wp[150],owp[150],oowp[150];
double ans[150];

int main()
{
	int cas=1;
	freopen("A-large.in","r",stdin);
	freopen("outAL.txt","w",stdout);
	int T;scanf("%d",&T);
	while(T--)
	{
		int n;scanf("%d",&n);
		int i,j,k,v,b;
		memset(ans,0,sizeof(ans));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		for(i=0;i<n;++i)
			scanf("%s",pot[i]);
		for(i=0;i<n;++i)
		{
			double kl=0,kk=0;
			for(j=0;j<n;++j)
			{
				if(pot[i][j]=='1')
					kl=kl+1,kk+=1;
				else if(pot[i][j]=='0')
					kk+=1;
			}
			ans[i]+=0.25*kl/kk;
			for(j=0;j<n;++j)
			{
				kl=kk=0;
				for(k=0;k<n;++k)
				{
					if(k==i) continue;
					if(pot[j][k]=='1')
						kl=kl+1,kk+=1;
					else if(pot[j][k]=='0')
						kk+=1;
				}
				wp[j]=kl/kk;
			}
			int cnt=0;
			for(j=0;j<n;++j)
			{
				if(pot[i][j]=='1'||pot[i][j]=='0')
					owp[i]+=wp[j],cnt++;
			}
			owp[i]/=cnt;
		}
		for(i=0;i<n;++i)
		{
			int cnt=0;
			for(j=0;j<n;++j)
			{
				if(pot[i][j]=='.') continue;
				oowp[i]+=owp[j],cnt++;
			}
			oowp[i]/=cnt;
		}
		for(i=0;i<n;++i)
			ans[i]+=0.5*owp[i]+0.25*oowp[i];
		printf("Case #%d:\n",cas++);
		for(i=0;i<n;++i)
			printf("%.12f\n",ans[i]);
	}
}