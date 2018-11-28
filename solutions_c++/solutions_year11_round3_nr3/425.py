#include <stdio.h>
#include <cmath>
#include <string>
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int t,T;
int n,l,h;
int a[1000];
int i,j;

int main()
{
	freopen("D:\\C-small-attempt0.in", "r", stdin);
	freopen("D:\\C-small-attempt0.out", "w", stdout);

	scanf("%d", &T);
	for(t=1; t<=T; t++)
	{
		scanf("%d%d%d", &n, &l, &h);
		for(i=0; i<n; i++)
		{
			scanf("%d", &a[i]);
		}
		printf("Case #%d: ", t);
		for(i=l; i<=h; i++)
		{
			for(j=0; j<n; j++)
			{
				if (a[j]%i!=0 && i%a[j]!=0)
				{
					break;
				}
			}
			if (j==n)
			{
				printf("%d\n", i);
				break;
			}
		}
		if(i>h)
		{
			printf("NO\n");
		}
	}

	return 0;
}