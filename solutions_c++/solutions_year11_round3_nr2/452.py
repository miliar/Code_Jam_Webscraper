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
int i,j;
int b1,b2;
int l, bt, n, c;
int a[1000005];
int res, r;

int main()
{
	bool imp;
	freopen("D:\\B-small-attempt0.in", "r", stdin);
	freopen("D:\\B-small.out", "w", stdout);
	scanf("%d", &T);
	for (t=1; t<=T; t++)
	{
		res=0;
		scanf("%d%d%d%d", &l,&bt, &n, &c);
		for (i=0; i<c; i++)
		{
			scanf("%d", &a[i]);
		}
		for(;i<n; i++)
		{
			a[i]=a[i-c];
		}
		if (l==0)
		{
			for(i=0; i<n; i++)
			{
				res+=a[i];
			}
			printf("Case #%d: %d\n", t, 2*res);
		}
		if (l==1)
		{
			res = 1<<30;

			for (b1=0; b1<n; b1++)
			{
				r=0;
				for(i=0; i<n; i++)
				{
					r+=2*a[i];
					if (res>bt && i==b1)
					{
						r-=min((r-bt)/2, a[i]);
					}
				}
				if (r<res)
				{
					res = r;
				}
			}
			printf("Case #%d: %d\n", t, res);
		}
		if (l==2)
		{
			res = 1<<30;

			for (b1=0; b1<n; b1++)
			{
				for (b2=0; b2<n; b2++)
				{
					r=0;
					for(i=0; i<n; i++)
					{
						r+=2*a[i];
						if (res>bt && (i==b1 || i==b2))
						{
							r-=min((r-bt)/2, a[i]);
						}
					}
					if (r<res)
					{
						res = r;
					}
				}
			}
			printf("Case #%d: %d\n", t, res);
		}
	}

	return 0;
}

/*
2
1 4 2 2 10 4
2 20 8 2 3 5

1
1 4 2 2 10 4
*/