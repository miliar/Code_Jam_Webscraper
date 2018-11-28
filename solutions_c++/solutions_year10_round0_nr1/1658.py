#include<iostream>
#include<algorithm>
#include<cstring>
#include<stdio.h> 
#include<memory.h>
#include<math.h>
using namespace std;
#define maxnum 0x7fffffff
int twopow(int n)
{
	int a[32];
	int size=0;
	while(n!=0)
	{
		a[size++]=n%2;
		n/=2;
	}
	int out=2;
	for(int i=size-2;i>=0;i--)
	{
		out=out*out;
		if(a[i]==1)
		{
			out=out*2;
		}
	} 
	printf("out==%d\n",out);
	return out;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas,tt;
	scanf("%d",&cas);
	for(tt=1;tt<=cas;tt++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		int x=pow(2,n);
		//printf("x===%d\n",x);
		if(k%x==x-1)
		printf("Case #%d: ON\n",tt);
		else printf("Case #%d: OFF\n",tt);
	}
	return 0;
}
