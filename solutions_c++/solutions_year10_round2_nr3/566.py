#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

const int MODULO=100003;

__int64 c[503][503];
int ans[502];
int f[502][502];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int i,j;
	int n,k;
	c[0][0]=1;
	for (i=1; i<=501; ++i)
	{
		c[i][0]=1;
		for (j=1; j<=501; ++j)
			c[i][j]=c[i-1][j]+c[i-1][j-1];
	}
	for (n=2; n<=500; ++n)
	{
		f[n][1]=1;
		for (k=2; k<n; k++)
		{
			for (i=1; i<k; ++i)
			{
				f[n][k]=(c[n-k-1][k-i-1]*f[k][i]+f[n][k])%MODULO;
			}
		}
		for (k=1; k<n; ++k)
			ans[n]=(ans[n]+f[n][k])%MODULO;
	}
	int tt,T;
	scanf("%d",&T);
	for (tt=0; tt<T; ++tt)
	{
		scanf("%d",&n);
		printf("Case #%d: %d\n",tt+1,ans[n]);
	}
	return 0;
}