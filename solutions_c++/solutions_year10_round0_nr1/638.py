#include<cstdio>
#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("a.in","r",stdin);
	freopen("za.out","w",stdout);
	int z;
	scanf("%d",&z);
	int a,b;
	for(int y=1;y<=z;y++)
	{
		scanf("%d%d",&a,&b);
		b%=(1<<a);
		if(b==(1<<a)-1)
			printf("Case #%d: ON\n",y);
		else
			printf("Case #%d: OFF\n",y);
	}
	return 0;
}
