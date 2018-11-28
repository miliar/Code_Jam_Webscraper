#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<utility>
#include<climits>
#include<complex>
#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>

using namespace std;

char s[120][120];
int n;
double wp[120],owp[120],oowp[120];
int main()
{
	freopen("C:\\1\\out.txt","w",stdout);
	int i,j,k;
	int _;
	int T=0;
	scanf("%d",&_);
	while (_--)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)scanf("%s",s[i]);
		for (i=0;i<n;i++)
		{
			int w=count(s[i],s[i]+n,'1');
			int tt=n-count(s[i],s[i]+n,'.');
			wp[i]=w*1.0/tt;
		}
		for (i=0;i<n;i++)
		{
			int opp=0;
			double p1=0;
			double opo[120]={0};
			for (j=0;j<n;j++)
			{
				int o1=0,o2=0;
				if (i==j)continue;
				for (k=0;k<n;k++)
				{
					if (k==i)continue;
					if (s[j][k]!='.')
					{
						o1++;
					}
					if (s[j][k]=='1')
					{
						o2++;
					}
				}
				opo[j]=o2*1.0/(o1*1.0);
				//if (i==3)printf("%d,%lf\n",j,opo[j]);
			}
			for (j=0;j<n;j++)
			{
				if (s[i][j]!='.')
				{
					opp++;
					p1+=opo[j];
				}
			}
			if (!opp)owp[i]=0;
			else owp[i]=p1/(opp*1.0);
			//printf("%lf\n",owp[i]);
		}
		for (i=0;i<n;i++)
		{
			int opp=0;
			double p1=0;
			for (j=0;j<n;j++)
			{
				if (s[i][j]!='.')
				{
					opp++;
					p1+=owp[j];
				}
			}
			if (!opp)oowp[i]=0;
			else oowp[i]=p1/(opp*1.0);
		}
		printf("Case #%d:\n",++T);
		for (i=0;i<n;i++)
		{
			printf("%.10lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
			
		
					
			
	
