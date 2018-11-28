#include<iostream>
#include<stdio.h>
using namespace std;
#define N 110
int a[N];
int main()
{
	int tc,i,j,n,l,h;
	scanf("%d",&tc);
	for(int t=0;t<tc;t++)
	{
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[j]%i==0 || i%a[j]==0)
					continue;
				else 
					break;
			}
			if(j==n) break;
		}
		printf("Case #%d: ",t+1);
		if(i==h+1)
			printf("NO\n");
		else
			printf("%d\n",i);
	}	
	return 0;
}
