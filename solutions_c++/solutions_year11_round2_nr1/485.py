#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int T,t,n,i,j,k,l,w,c;
double wp[200],owp[200],oowp[200];
char a[200][200];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",&a[i]);
			w=l=0;
			for(j=0;j<n;j++)
			{
				if(a[i][j]=='1')
					w++;
				if(a[i][j]=='0')
					l++;
			}
			wp[i]=1.0*w/(w+l);
		}
		for(i=0;i<n;i++)
		{
			c=0;
			owp[i]=0;
			for(j=0;j<n;j++)
			{
				if(a[i][j]=='.')
					continue;
				w=l=0;
				c++;
				for(k=0;k<n;k++)
				{
					if(k==i)
						continue;
					if(a[j][k]=='1')
						w++;
					if(a[j][k]=='0')
						l++;
				}
				owp[i]+=1.0*w/(w+l);
			}
			owp[i]/=c;
		}
		for(i=0;i<n;i++)
		{
			c=0;
			oowp[i]=0;
			for(j=0;j<n;j++)
			{
				if(a[i][j]=='.')
					continue;
				oowp[i]+=owp[j];
				c++;
			}
			oowp[i]/=c;
		}
		printf("Case #%d:\n",++t);
		for(i=0;i<n;i++)
			printf("%.12lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}