#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char p[105][105];
double wp[105];
double owp[105];
double oowp[105];
int main()
{
	int i,j,k,t,cas = 1,n,cnt,res,num;
	double r,e;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		printf("Case #%d:\n",cas++);
		scanf("%d",&n);
		getchar();
		for(i = 0;i < n;i++)
			gets(p[i]);
		for (i = 0;i < n;i++)
		{
			res = cnt = 0;
			for (j = 0;j < n;j++)
			{
				if (p[i][j] == '1')
					res++,cnt++;
				else if(p[i][j] == '0')
					cnt++;
			}
			wp[i] = (res + 0.0) / cnt;
		}
		for (i = 0;i < n;i++)
		{
			r = 0;
			num = 0;
			for (j = 0;j < n;j++)
			{
				if (i == j)
					continue;
				if (p[j][i] == '.')
					continue;
				num++;
				e = 0;
				res = cnt = 0;
				for (k = 0;k < n;k++)
				{
					if (k == i || p[j][k] == '.')
						continue;
					if (p[j][k] == '1')
						res++,cnt++;
					else if(p[j][k] == '0')
						cnt++;
				}
				e = (res + 0.0) / cnt;
				r += e;
			}
			r /= num;
			owp[i] = r;
		}
		for (i = 0;i < n;i++)
		{
			r = 0;
			num = 0;
			for (j = 0;j < n;j++)
			{
				if (i == j)
					continue;
				if (p[i][j] == '.')
					continue;
				num++;
				r += owp[j];
			}
			r /= num;
			oowp[i] = r;
		}
		for (i = 0;i < n;i++)
			printf("%lf\n",wp[i] / 4 + owp[i] / 2 + oowp[i] / 4);
	}
	return 0;
}