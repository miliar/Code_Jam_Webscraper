#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<string>
#include<stdlib.h>
#include<vector>
#include<math.h>
using namespace std;
int a[210];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ans.out","w",stdout);
	int t,k=0;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		k++;
		scanf("%d",&n);
		int sum=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			sum+=a[i];
		}
		printf("Case #%d: ",k);
		for(int i=0;i<n;i++)
		{
			double l=0.0,r=1.0;
			while(r-l>=1e-10)
			{
				double mid=(l+r)/2;
				double x1=a[i]+sum*mid;
				double x2=0;
				double nn=0;
				for(int j=0;j<n;j++)
				{
					if(j!=i&&a[j]<x1+1e-10)
					{
						nn++;
						x2+=a[j];
					}
				}
				if(x2+sum*(1.0-mid)>x1*nn)
					l=mid;
				else
					r=mid;
			}
			printf("%.6lf",100*(l+r)/2);
			printf("%c",i==n-1?'\n':' ');
		}
	}
}