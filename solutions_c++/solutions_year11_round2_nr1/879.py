#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <math.h>
#include <string.h>

using namespace std;

int a[110][110];
double wp[110];
double rt[110];
double owp[110];
double oowp[110];
double hl[110],hw[110];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,n,kol,win,i,j;
	double s;
	char ch;
	scanf("%d",&t);
	for (int cnt=1;cnt<=t;cnt++)
	{
		printf("Case #%d:\n",cnt);
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%c",&ch);
			for (j=0;j<n;j++)
			{
				scanf("%c",&ch);
				if (ch=='1') a[i][j]=1;
				if (ch=='0') a[i][j]=0;
				if (ch=='.') a[i][j]=-1;
			}
			
		}
		for (i=0;i<n;i++)
		{
			win=0;
			kol=0;
			for (j=0;j<n;j++)
			{
				if (a[i][j]>=0) kol++;
				if (a[i][j]==1) win++;
			}
			wp[i]=(double)win/kol;
			hl[i]=(double)win/(kol-1);
			hw[i]=(double)(win-1)/(kol-1);
		}
		for (i=0;i<n;i++)
		{
			kol=0;
			s=0;
			for (j=0;j<n;j++)
			{
				if (a[i][j]==0)
				{
					kol++;
					s+=hw[j];
				}
				if (a[i][j]==1)
				{
					kol++;
					s+=hl[j];
				}
			}
			s/=kol;
			owp[i]=s;
		}
		for (i=0;i<n;i++)
		{
			kol=0;
			s=0;
			for (j=0;j<n;j++)
			{
				if (a[i][j]>=0)
				{
					kol++;
					s+=owp[j];
				}
			}
			s/=kol;
			oowp[i]=s;
			rt[i]=wp[i]/4+owp[i]/2+oowp[i]/4;
			printf("%0.8lf\n",rt[i]);
		}
	}
	return 0;
}