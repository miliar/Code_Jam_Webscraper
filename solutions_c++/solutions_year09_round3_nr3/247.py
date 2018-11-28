// qa.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "memory.h"
using namespace std;

int p,q;
int ans;
int a[1000];

void back(int t)
{
	if (t == q)
	{
		int b[1000] = {0};
		int count = 0;
		for (int i = 0; i < q; i++)
		{
			b[a[i]] = 1;
			
			for (int j = a[i]-1; j >= 0 && b[j] == 0; j--)
				count++;
			for (int j = a[i]+1; j < p && b[j] == 0; j++)
				count++;
		}
		ans = ans < count ? ans : count;
		return;
	}

	for (int i = t; i < q; i++)
	{
		swap(a[i],a[t]);
		back(t+1);
		swap(a[i],a[t]);
	}
}

int main()
{
	freopen("e:\\C-small-attempt0.in","r",stdin);
	freopen("a.txt","w",stdout);
	int zz;
	int i,j;

	scanf("%d",&zz);

	for (int z = 1; z <= zz; z++)
	{		
		ans = 0x7fffffff;
		scanf("%d%d",&p,&q);
		
		for (i = 0; i < q; i++)
		{
			scanf("%d",&a[i]);
			a[i]--;
		}

		back(0);

		printf("Case #%d: %d\n",z,ans);
	}

	return 0;
}