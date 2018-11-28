#include<iostream>
#include<stdio.h>
#include<limits.h>
using namespace std ;
int a[2000];
int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int N;
		cin>>N;
		int xora=0;
		int min=INT_MAX;
		long long int sum=0;
		for(int n=0;n<N;n++)
		{
			scanf("%d",&a[n]);
			if(a[n]<min)
				min=a[n];
			xora^=a[n];
			sum+=a[n];
		}
		printf("Case #%d: ",t+1);
		if(!xora)
		{
			printf("%lld\n",sum-min);
		}
		else
			printf("NO\n");
	}
	return 0;
}
