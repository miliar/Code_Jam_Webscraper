#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

#define MAXN 110

int n;

char g[MAXN][MAXN];

double res[MAXN];
double WP[MAXN],OWP[MAXN],OOWP[MAXN];

int main()
{
	int ct,text;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&text);
	for(ct=1;ct<=text;ct++)
	{
		int i,j,k;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			double win=0,lose=0;
			scanf("%s",g[i]);
			for(j=0;j<n;j++)
			{
				if(g[i][j]=='1')
				{
					win++;
				}
				if(g[i][j]=='0')
				{
					lose++;
				}
			}
			res[i]=win/(win+lose);
		}	
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{	
				double win=0,lose=0;
				for(k=0;k<n;k++)
				{
					if(g[j][k]!='.' && k!=i)
					{
						if(g[j][k]=='1')
						{
							win++;
						}
						else
						{
							lose++;
						}
					}
				}
				WP[j]=win/(win+lose);
			}
			double cnt=0,num=0;
			for(j=0;j<n;j++)
			{
				if(g[i][j]!='.')
				{
					cnt+=WP[j];
					num++;
				}
			}
			OWP[i]=cnt/num;
		}
		for(i=0;i<n;i++)
		{
			double cnt=0,num=0;
			for(j=0;j<n;j++)
			{
				if(g[i][j]!='.')
				{
					num++;
					cnt+=OWP[j];
				}
			}
			OOWP[i]=cnt/num;
		}
		printf("Case #%d:\n",ct);
		for(i=0;i<n;i++)
		{
			printf("%.10lf\n",0.25*res[i]+0.50*OWP[i]+0.25*OOWP[i]);
		}
	}
	return 0;
}
/*
1
4
.11.
0.00
01.1
.10.

*/
