#include "stdio.h"
#include "string.h"
#include "math.h"
#include <algorithm>
using namespace std;
#define M 103

char s[M][M];
int n;
double wp[M],owp[M],oowp[M];

int main()
{
	int i,j,k,t,tc=1;
	int p1,p2,p3;
	double pp;
	freopen("gcj/2011.5.22/A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",s[i]);
		for(i=0;i<n;i++)
		{
			p1=0;p2=0;
			for(j=0;j<n;j++)
			{
				if(s[i][j]=='.')
					continue;
				if(s[i][j]=='1')
					p1++;
				p2++;
			}
			wp[i]=p1*1.0/p2;
		}
		for(i=0;i<n;i++)
		{
			pp=0;p3=0;
			for(j=0;j<n;j++)
			{
				if(s[j][i]=='.')
					continue;
				p1=0;p3++;p2=0;
				for(k=0;k<n;k++)
				{
					if(k==i)
						continue;
					if(s[j][k]=='.')
						continue;
					if(s[j][k]=='1')
						p1++;
					p2++;
				}
				pp+=p1*1.0/(p2);
			}
			owp[i]=pp/p3;
		}
		for(i=0;i<n;i++)
		{
			pp=0;p2=0;
			for(j=0;j<n;j++)
			{
				if(s[i][j]=='.')
					continue;
				pp+=owp[j];
				p2++;
			}
			oowp[i]=pp/p2;
		}
		printf("Case #%d:\n",tc++);
		for(i=0;i<n;i++)
			printf("%.7lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 *oowp[i]);
	}
	return 0;
}
/*
3
1 100 50
10 10 100
9 80 56
*/

