//#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int a[1001] = {0};
//int dp[1001];
long long res = -1;
int m;
void rec(int i,long long sum1 = 0,long long sum2 = 0,long long xor1 = 0,long long xor2 = 0)
{
	if(i >= m)
	{
		if(xor1 == xor2 && sum1 != 0 && sum2 != 0)
		{
			long long mx = max(sum1,sum2);
			res = max(mx,res);
		}
		return;
	}
	rec(i + 1,sum1 + a[i],sum2,       xor1 ^ a[i],xor2);
	rec(i + 1,sum1,       sum2 + a[i],xor1,       xor2 ^ a[i]);
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int n;
	scanf("%d",&n);
	for(int i = 0; i < n; i++)
	{
		scanf("%d",&m);
		for(int j = 0; j < m; j++)
		{
			scanf("%d",&a[j]);
		}
		rec(0);
		if(res == -1)
			printf("Case #%d: NO\n",i + 1);
		else
			printf("Case #%d: %d\n",i + 1,res);
		res = -1;
	}

	return 0;
}
