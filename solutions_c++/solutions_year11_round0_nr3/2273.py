
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
using namespace std;
int c[1000005];
int main()
{
	int t,n,v,i,ca=1;
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",ca++);
		scanf("%d",&n);
		v=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",c+i);
			v=v^c[i];
		}
		if(v)
		{
			puts("NO");
			continue;	
		}
		sort(c,c+n);
		for(v=0,i=1;i<n;i++)v+=c[i];
		printf("%d\n",v);
	}	
}
