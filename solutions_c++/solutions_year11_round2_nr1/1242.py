#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cassert>
#include<ctime>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>

#define PB push_back
#define M 100
#define N 110
#define LL long long


using namespace std;






int main()
{
	int tc,ti;
	scanf("%d",&tc);
	for(ti=1;ti<=tc;++ti)
	{
		int i,j,k,n;
		char str[N][N];
		double won,pld,opps,pc,wp[N],ewp[N][N],owp[N],oowp[N];
		scanf("%d",&n);
		for(i=0;i<n;++i)
		scanf("%s",str[i]);
		
		for(i=0;i<n;++i)
		{
			won=0;pld=0;
			for(j=0;j<n;++j)
			{
				
				if(i!=j)
				{
					if(str[i][j]=='1')
					won+=1;
					if(str[i][j]!='.')
					pld+=1;
				}
				
				
			}
			if(pld!=0)
			wp[i]=won/pld;
			else
			wp[i]=0;
		}
		
		for(i=0;i<n;++i)
		{
			
			for(j=0;j<n;++j)
			{
				won=0;pld=0;
				for(k=0;k<n;++k)
				{
					if(i==k||j==k)
					continue;
					
					if(str[j][k]=='1')
					won+=1;
					if(str[j][k]!='.')
					pld+=1;
				
				}
				if(pld!=0)
				ewp[j][i]=won/pld;
				else
				ewp[j][i]=0;
			}
		}
		
		for(i=0;i<n;++i)
		{
			opps=0;pc=0;
			for(j=0;j<n;++j)
			{
				if(str[i][j]!='.')
				{
					opps+=1;
					pc+=ewp[j][i];
				}
			}
			if(opps!=0)
			owp[i]=pc/opps;
			else
			owp[i]=0;
			
		}
		
		for(i=0;i<n;++i)
		{
			opps=0;pc=0;
			for(j=0;j<n;++j)
			{
				if(str[i][j]!='.')
				{
					opps+=1;
					pc+=owp[j];
				}
			}
			if(opps!=0)
			oowp[i]=pc/opps;
			else
			oowp[i]=0;
			
		}
		
		
		
		printf("Case #%d:\n",ti);
		for(i=0;i<n;++i)
		{
			//printf("%lf %lf %lf\t",wp[i],owp[i],oowp[i]);
			printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
		
	}
	
	return 0;
}
