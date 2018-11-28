#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	long long int r;
	long long int k;
	long long int a[1001];
	long long int till[1001];
	long long int cost[1001];
	long long int p;

	int t;
	int n;
	int m;
	int flag;
	long long int answer=0;
	scanf("%d",&t);
	for (int i=0;i<t;i++)
	{
		flag=0;
		answer=0;
		scanf("%lld%lld%d",&r,&k,&n);
		for (int j=0;j<n;j++)
		{
			scanf("%lld",&a[j]);
		}

		for (int j=0;j<n;j++)
		{
			long long int c=0;
			for (p=0;p<j+n;p++)
			{
				c=c+a[(j+p)%n];
				if(c>k)
				{
					flag=1;
					break;
				}
			}
			if(flag==1)
				c=c-a[(j+p)%n];
			if(c==0)
				till[j]=j+1;
			else 
				till[j]=(j+p)%n;
			cost[j]=c;
		}

		int b=0;

		for (long long int j=0;j<r;j++)
		{
			answer=answer+cost[b];
			b=till[b];
		}

		cout<<"Case #"<<i+1<<": "<<answer<<endl;
	}
	return 0;
}









