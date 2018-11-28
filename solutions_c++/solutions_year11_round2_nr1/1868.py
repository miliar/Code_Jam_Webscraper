#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

char table[105][105];
int one[105][2],two[105][2],three[105][2];
double owp[105];

double res[105];

int main()
{
	//freopen("e:\\A-large.in", "r", stdin);	//freopen("e:\\A-large.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		memset(one,0,sizeof(one));
		memset(two,0,sizeof(two));
		memset(three,0,sizeof(three));
		memset(res,0,sizeof(res));
		memset(owp,0,sizeof(owp));
		int n;
		scanf("%d",&n);
		getchar();
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n;k++)
			{
				scanf("%c",&table[j][k]);
			}
			getchar();
		}
		for(int j=0;j<n;j++)
		{
			int w=0,l=0;
			for(int k=0;k<n;k++)
			{
				if(table[j][k] == '1')
					w++;
				else if(table[j][k] == '0')
					l++;
			}
			one[j][0]=w;
			one[j][1]=l+w;
			two[j][0]=one[j][0];
			two[j][1]=one[j][1];
			three[j][0]=one[j][0];
			three[j][1]=one[j][1];
			res[j]=double(w)/double(w+l)*0.25;
		}
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n;k++)
			{
				if(table[j][k] == '1')
				{
					two[k][1]--;
				}
				else if(table[j][k] == '0')
				{
					two[k][1]--;
					two[k][0]--;
				}
			}
			for(int k=0;k<n;k++)
			{
				if((k == j)||(table[j][k] == '.'))
					continue;
				owp[j]=owp[j]+double(two[k][0])/double(two[k][1]);
			}
			owp[j]=owp[j]/double(one[j][1]);
			res[j]=res[j]+owp[j]*0.50;
			for(int k=0;k<n;k++)
			{
				two[k][1]=one[k][1];
				two[k][0]=one[k][0];
			}
		}
		for(int j=0;j<n;j++)
		{
			double oowp=0.0;
			for(int k=0;k<n;k++)
			{
				if(k == j)
					continue;
				if(table[j][k] != '.')
				{
					oowp=oowp+owp[k];
				}
			}
			oowp=oowp/double(one[j][1]);
			res[j]=res[j]+oowp*0.25;
		}
		printf("Case #%d:\n",i+1);
		for(int j=0;j<n;j++)
		{
			printf("%lf\n",res[j]);
		}
	}
	return 0;
}