#include<iostream>
#include<stdio.h>
using namespace std;
int a[1001],p[1001];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int t,n;
	scanf("%d",&t);
	for(int tt = 0; tt < t; tt++)
	{
		scanf("%d",&n);
		double res = 0.0;
		for(int i = 1; i <= n; i++)
		{
			scanf("%d",&a[i]);
			if (i != a[i]) res = res + 1.0;
		}
		printf("Case #%d: %.6lf\n",tt + 1,res);
	}
	return 0;
}
