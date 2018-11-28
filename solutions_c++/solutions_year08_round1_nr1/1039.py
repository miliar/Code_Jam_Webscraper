// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "cstdio"
#include "cstdlib"

int cmp(const void *lhs,const void *rhs)
{
	return *(int *)lhs-*(int *)rhs;
}

int solve()
{
	int i,j,jf,je,jf2,je2;
	int x[800],y[800];
	int ans = 0;
	int n;

	scanf("%d",&n);
	for (i = 0; i < n; i++)
		scanf("%d",&x[i]);
	for (i = 0; i < n; i++)
		scanf("%d",&y[i]);

	qsort(x,n,sizeof(int),cmp);
	qsort(y,n,sizeof(int),cmp);

	jf2 = 0,je2 = n-1;
	for (i = 0; i < n; i++)
	{
		if (x[i] < 0)
		{
			ans += x[i]*y[je2--];
		}
		else
			break;
	}
	for (j = n-1; j >= i; j--)
		ans += x[j]*y[jf2++];
	return ans;
}

int main()
{
	freopen("s.txt","r",stdin);
	freopen("a.txt","w",stdout);
	int t;

	scanf("%d",&t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}

