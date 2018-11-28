#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
#define MAXN 2000
int arr[MAXN];

int main()
{
	//freopen("in.txt","r",stdin);
	int T;
	scanf("%d",&T);
	int caseN=1;
	while(T--)
	{
		int N;
		scanf("%d",&N);
		int sum=0;
		int ans=0;
		int mmin=1000000000;
		for(int i=0;i<N;i++)
		{
			scanf("%d",arr+i);
			sum^=arr[i];
			ans+=arr[i];
			mmin=min(mmin,arr[i]);
		}
		if(sum!=0)
		{
			printf("Case #%d: NO\n",caseN++);
		}
		else
		{
			printf("Case #%d: %d\n",caseN++,ans-mmin);
		}
		
	}
	return 0;
}