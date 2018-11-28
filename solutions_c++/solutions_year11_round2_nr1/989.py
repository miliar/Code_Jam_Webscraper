#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
#define max(a,b) (a)>(b)?(a):(b) 
#define min(a,b) (a)<(b)?(a):(b)
char a[101][101];
double b[101],c[101];
int win[101],lose[101];
int main()
{
	int repeat,i,j,n,m,ri=1,ct;
	double wp,owp,oowp,sum;
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		memset(win,0,sizeof(win));
		memset(lose,0,sizeof(lose));
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",a[i]);
			for(j=0;a[i][j];j++)
			{
				if( a[i][j]=='1')
				{
					win[i]++;
					lose[j]++;
				}
			}
		}
		for(i=0;i<n;i++)
		{
			wp=1.0*win[i]/(win[i]+lose[i]);
			c[i]=wp;
			ct=0;
			owp=0;
			for(j=0;j<n;j++)
			{
				if( a[i][j]!='.')
				{
					ct++;
					if(a[j][i]=='0') owp+=1.0*win[j]/(win[j]+lose[j]-1);
					else owp+=1.0*(win[j]-1)/(win[j]+lose[j]-1);
				}
			}
			owp/=ct;
			b[i]=owp;
		}
		printf("Case #%d: \n",ri++);
		for(i=0;i<n;i++)
		{
			sum=0;
			ct=0;
			for(j=0;j<n;j++)
			{
				if( a[i][j]!='.')
				{
					ct++;
					sum+=b[j];
				}
			}
			printf("%.12lf\n",0.25*c[i]+0.5*b[i]+0.25*sum/ct);
		}
		
	}
	return 0;
}