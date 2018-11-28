#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

const int N=110;
int a[N], n, l, h, t, t1;

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	int i, j, k, flag, ans;
	scanf("%d", &t);
	for(t1=1; t1<=t; t1++)
	{
		scanf("%d%d%d", &n, &l, &h);
		for(i=0; i<n; i++)
			scanf("%d", &a[i]);
		for(i=l; i<=h; i++)
		{
			flag = 1;
			for(j=0; j<n; j++)
			{
				if(i>a[j] && i%a[j]!=0)
				{
					flag = 0;
					break;
				}
				if(a[j]>=i && a[j]%i!=0)
				{
					flag = 0;
					break;
				}
			}
			if(flag==1)
				break;
		}
		ans = i;
		printf("Case #%d: ", t1);
		if(flag)
			printf("%d\n", ans);
		else
			printf("NO\n");
	}

	return 0;
}
