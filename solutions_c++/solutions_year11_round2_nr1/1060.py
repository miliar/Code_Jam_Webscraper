#include <cstdio>
#include <cstdlib>
#define MAX 100
char buffer[MAX+10];
int map[MAX][MAX];
double wp[MAX];
double owp[MAX];
double oowp[MAX];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int nT,t=0;
	scanf("%d",&nT);
	while(nT--)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
		{
			scanf("%s",buffer);
			for(int j=0;j<n;++j)
			{
				if(buffer[j]=='1')
					map[i][j]=1;	
				else if(buffer[j]=='0')
					map[i][j]=0;
				else
					map[i][j]=-1;
			}
		}
		for(int i=0;i<n;++i)
		{
			int cc=0;
			wp[i]=0;
			for(int j=0;j<n;++j)
			{
				if(map[i][j]!=-1)
				{
					++cc;
					if(map[i][j]==1)
						++wp[i];
				}
			}
			wp[i]/=cc;
		}
		for(int i=0;i<n;++i)
		{
			int cc=0;
			owp[i]=0;
			for(int j=0;j<n;++j)
			{
				if(map[i][j]!=-1)
				{
					++cc;
					int opCC=0;
					int opWin=0;
					for(int k=0;k<n;++k)
					{
						if(map[j][k]!=-1 && k!=i)
						{
							++opCC;
							if(map[j][k]==1)
								opWin++;
						}
					}
					owp[i]+=(double)opWin/opCC;
				}
			}
			owp[i]/=cc;	
		}
		for(int i=0;i<n;++i)
		{
			int cc=0;
			oowp[i]=0;
			for(int j=0;j<n;++j)
			{
				if(map[i][j]!=-1)
				{
					++cc;
					oowp[i]+=owp[j];
				}	
			}	
			oowp[i]/=cc;
		}
		printf("Case #%d:\n",++t);
		for(int i=0;i<n;++i)
		{
			printf("%.8f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}	
}
