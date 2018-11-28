#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <math.h>
using namespace std;

int n,k;

int int_Pow(int t)
{
	int tmp;
	int i;
	if(t==0)
	{
		return 1;
	}
	else
	{
		tmp=int_Pow(t/2);
		if(t&1)
			return 2*tmp*tmp;
		else
			return tmp*tmp;
	}
}

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int i,j;
	int test;
	scanf("%d",&test);
	for (i=1;i<=test;i++)
	{
		scanf("%d %d",&n,&k);
		int temp = int_Pow(n);
		int ans = k%temp;
		if (ans == temp-1)
		{
			printf("Case #%d: ON\n",i);
		}
		else
		{
			printf("Case #%d: OFF\n",i);
		}
	}
	return 0;
}