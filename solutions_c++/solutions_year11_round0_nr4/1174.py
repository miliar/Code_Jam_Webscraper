#include <stdio.h>
#include <string>
#include <cstring>

int main()
{
	freopen("F:\\code\\topcoder\\compete\\compete\\codejam_2011\\D-large.in","r",stdin);
	freopen("F:\\code\\topcoder\\compete\\compete\\codejam_2011\\result.txt","w",stdout);
	double y[1005];
	double yd[1005];
	y[0] = 0;
	y[1] = 0;
	yd[0] = 1;
	yd[1] = 0;
	for (int i = 2;i<=1000;i++)
	{
		double temp = 0;
		for (int j = 1;j<=i;j++)
		{
			yd[i-j]/=j;
			temp += yd[i-j];
		}
		y[i] = 1-temp;
		yd[i] = y[i];
		//printf("%d %f\n",i,y[i]);
	}
	double f[1005];
	f[1] = 0;
	yd[1] = 0;
	for (int i = 2;i<=1000;i++)
	{
		double temp = 0;
		for(int j = 1;j<i;j++)
		{
			yd[i-j]/=j;
			temp += yd[i-j];
		}
		f[i] = (1+temp)/(1-y[i]);
		yd[i] = f[i]*y[i];
		//printf("%d %f\n",i,f[i]);
	}
	int caseNum = 0;
	int t;
	scanf("%d",&t);
	while(caseNum<t)
	{
		printf("Case #%d: ",caseNum+1);
		int n;
		scanf("%d",&n);
		int number[1005];
		double res = 0;
		for (int i = 0;i<n;i++)
		{
			scanf("%d",number+i);
		}
		for (int i = 0;i<n;i++)
		{
			if (number[i]<0)
			{
				continue;
			}
			int now = i;
			int group = 0;
			while (number[now]>0)
			{
				group ++;
				number[now] = -number[now];
				now = -number[now]-1;
			}
			res += f[group];
		}
		printf("%f\n",res);
		caseNum++;
	}
}