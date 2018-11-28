#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int a[10001];
	int b[10001];
	int k=1;
	
	while(t>0)
	{
		long long int ct=0;
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&a[i],&b[i]);
		}

		for (int i=0;i<n;i++)
		{
			for (int j=i+1;j<n;j++)
			{
				if((a[i]<a[j] && b[i]>b[j]) || (a[i]>a[j] && b[i]<b[j]))
				{
					ct++;
				}
			}
		}
		cout<<"Case #"<<k<<": "<<ct<<endl;
		k++;
		t--;
	}
	return 0;
}
	
