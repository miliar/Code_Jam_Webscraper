#include <iostream>
#include <algorithm>
#include<functional>
#include <string>
#include <stdio.h>
using namespace std;
int arr[200];
int main()
{
	//freopen("D:\\Visual Studio 2008\\google code jam\\B-large.in", "r", stdin ) ;

	//freopen("D:\\Visual Studio 2008\\google code jam\\B-large.out", "w", stdout ) ;


	int t,N,S,P;
	scanf("%d ",&t);
	for(int k=1;k<=t;++k)
	{
		int ans=0;
		cin>>N>>S>>P;
		for(int i=0;i<N;++i)
			cin>>arr[i];
		sort(arr,arr+N);
		for(int i=N-1;i>=0;--i)
		{
			if(P==0)
				ans++;
			else if(P==1)
			{
				if(arr[i]>=1)
					ans++;
			}
			else 
			{
				if(arr[i]>=3*P-2)
					ans++;
				else if(arr[i]>=3*P-4&&S>0)
				{
					S--;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}