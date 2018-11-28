#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

int num[1005];

int main()
{
	//freopen("e:\\B-large.in", "r", stdin);	//freopen("e:\\B-large.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int n;
		int res=0;
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			scanf("%d",&num[j]);
		}
		sort(num,num+n);
		int add=0;
		for(int j=1;j<n;j++)
		{
			res+=num[j];
			add=add^num[j];
		}
		printf("Case #%d: ",i+1);
		if(add == num[0])
			printf("%d\n",res);
		else
			printf("NO\n");
	}
	return 0;
}