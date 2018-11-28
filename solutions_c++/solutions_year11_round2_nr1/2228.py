#include<stdio.h>
#include<iostream>
using namespace std;

double b[150],c[150],d[150];
int sum[150],num[150];
char a[105][105];
int main()
{
	int t,n,i,j,cas=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				cin>>a[i][j];
		for(i=0;i<n;i++)
		{
			sum[i]=num[i]=0;
			b[i]=0;c[i]=0;d[i]=0;
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if(a[i][j]!='.')
				{
					sum[i]++;
					if(a[i][j]=='1')
						num[i]++;
				}
			b[i]=num[i]*1.0/sum[i];
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[i][j]=='0')
				{
					if(num[j]>1)
						c[i]+=(num[j]-1)*1.0/(sum[j]-1);
				}
				if(a[i][j]=='1')
				{
					if(sum[j]>1)
						c[i]+=num[j]*1.0/(sum[j]-1);
				}
			}
			c[i]=c[i]/sum[i];
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if(a[i][j]!='.')
					d[i]+=c[j];
			d[i]=d[i]/sum[i];
		}
		printf("Case #%d:\n",cas++);
		for(i=0;i<n;i++)
		{
			double temp=b[i]*0.25+c[i]*0.5+d[i]*0.25;
			printf("%.12lf\n",temp);
		}
	}
	return 0;
}

