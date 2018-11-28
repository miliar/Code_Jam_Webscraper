#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
char map[105][105];
double wp[105],owp[105],oowp[105];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Aout.out","w",stdout);
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		memset(map,0,sizeof(map));
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		int n;
		scanf("%d",&n);
		int i,j,k;
		for(i=0;i<n;i++)
			scanf("%s",map[i]);
		for(i=0;i<n;i++)
		{
			double win=0,sum=0;
			for(j=0;j<n;j++)
				if(map[i][j]!='.')
				{
					sum++;
					if(map[i][j]=='1')
						win++;
				}
			wp[i]=win/sum;
		}
		for(i=0;i<n;i++)
		{
			double num=0,wins=0;
			for(j=0;j<n;j++)
				if(map[i][j]!='.')
				{
					num++;
					double sum=0,win=0;
					for(k=0;k<n;k++)
						if(k!=i&&map[j][k]!='.')
						{
							sum++;
							if(map[j][k]=='1')
								win++;
						}
					wins+=win/sum;
				}
			owp[i]=wins/num;
		}
		for(i=0;i<n;i++)
		{
			double num=0,sum=0;
			for(j=0;j<n;j++)
				if(map[i][j]!='.')
				{
					num++;
					sum+=owp[j];
				}
			oowp[i]=sum/num;
		}
		printf("Case #%d:\n",cas);
		for(i=0;i<n;i++)
		{
			double tmp;
			tmp=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			printf("%.7f\n",tmp);
		}
	}
	return 0;
}
