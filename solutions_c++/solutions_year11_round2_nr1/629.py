#include<cstdio>
#include<algorithm>

using namespace std;

typedef long double LD;

#define MX 105

int tt;
int n;

char T[MX][MX];

LD RPI[MX],OWP[MX],OOWP[MX];
int games[MX],WP[MX];

int main()
{
	scanf("%d",&tt);
	for(int t=1;t<=tt;++t)
	{
		memset(games,0,sizeof games);
		memset(RPI,0,sizeof RPI);
		memset(WP,0,sizeof WP);
		memset(OWP,0,sizeof OWP);
		memset(OOWP,0,sizeof OOWP);
		scanf("%d\n",&n);
		for(int i=0;i<n;++i)
		{
			scanf("%s",T[i]);
			for(int j=0;j<n;++j)
			{
				if (T[i][j]!='.')
				{
					games[i]++;
					if (T[i][j]=='1') WP[i]++;
				}
			}
			RPI[i]=WP[i]/(LD)games[i]*.25;
		}
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<n;++j)
			{
				if (T[i][j]!='.')
				{
					int x=WP[j];
					if (T[i][j]=='0') x--;
					OWP[i]+=x/(LD)(games[j]-1);
				}
			}
			OWP[i]/=(LD)games[i];
			RPI[i]+=OWP[i]*.5;
		}
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<n;++j)
			{
				if (T[i][j]!='.')
				{
					OOWP[i]+=OWP[j];
				}
			}
			OOWP[i]/=(LD)games[i];
			RPI[i]+=OOWP[i]*.25;
		}
		printf("Case #%d: \n",t);
		for(int i=0;i<n;++i)
		{
			printf("%.11lf\n",(double)RPI[i]);
		}
	}
	return 0;
}
