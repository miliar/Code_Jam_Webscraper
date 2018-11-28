#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define MAXN 102
char mp[MAXN][MAXN];
double WP[MAXN], OWP[MAXN],OOWP[MAXN];
int Cnt[MAXN];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,N;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%s",mp[i]);
		for(int i=0;i<N;i++)
		{
			int cnt=0,k=0;
			for(int j=0;j<N;j++)
			{
				if(mp[i][j]!='.')
				{
					cnt++;
					if(mp[i][j]=='1')
						k++;
				}
			}
			Cnt[i]=cnt;
			WP[i]=k*1.0/cnt;
		}
		for(int i=0;i<N;i++)
		{
			double sum=0;
			for(int j=0;j<N;j++)
			{
				int a=0,cnt=0;
				if(mp[i][j]!='.')
				{
					for(int k=0;k<N;k++)
						if(k!=i)
						{
							if(mp[j][k]!='.')
							{
								cnt++;
								if(mp[j][k]=='1')
									a++;
							}
						}
					sum+=a*1.0/cnt;
				}
			}
			OWP[i]=sum/Cnt[i];
		}
		for(int i=0;i<N;i++)
		{
			double sum=0;
			for(int j=0;j<N;j++)
			{
				int a=0,cnt=0;
				if(mp[i][j]!='.')
				{
				
					sum+=OWP[j];
				}
			}
			OOWP[i]=sum/Cnt[i];
		}
		printf("Case #%d:\n",t);
		for(int i=0;i<N;i++)
		{
			//printf("%.3lf %.3lf %.3lf\n",WP[i],OWP[i],OOWP[i]);
			printf("%.8lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}
	}
	return 0;
}
