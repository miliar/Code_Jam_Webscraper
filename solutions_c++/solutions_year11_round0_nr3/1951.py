#include<iostream>
#include<stdio.h>
using namespace std;

long long int arr[1001];
int main()
{
	int T,N,j=0;
	long long int C,S,min=0;
	scanf("%d",&T);
	while(T--)
	{
		j++;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		scanf("%lld",&arr[i]);
		C=S=min=0;
		for(int i=0;i<N;i++)
		{
			C=C^arr[i];
			S+=arr[i];
			if(i==0)
			min=arr[i];
			if(arr[i]<min)
			min=arr[i];
		}
		if(C==0)
		printf("Case #%d: %lld\n",j,S-min);
		else
		printf("Case #%d: NO\n",j);
	}
}
