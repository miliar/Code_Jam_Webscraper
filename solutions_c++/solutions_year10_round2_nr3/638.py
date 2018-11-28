

#include "stdafx.h"
#include <algorithm>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include <map>
#include<vector>
using namespace std;

int n,m;
int dp[505][505];

__int64 C(int nn,int mm)
{
	if(mm == 0) return 1;
	if(nn == 0 || mm>nn) return 0;
	__int64 res=1;
	if(mm> nn/2) mm = nn-mm;
	for(int i=1;i<=mm;++i)
	{
		res *= nn-mm+i;
		res /= i;
	}
	res %=100003;
	return res;
}
int cal(int x,int y)
{
	if(x == 0) return 0;
	if(dp[x][y] != -1) return dp[x][y];
	int res = 0;
	for(int i=x-1;i>=1 ; --i)
	{
		res += cal(i,x) * C((y-x-1),(x-i-1));
		res %=100003;
	}
	dp[x][y] = res;
	return res;
}
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	int fib[500];
	fib[1] = 1;fib[2] = 2;
	for(int i=3;i<=30;++i)
		fib[i] = fib[i-1] + fib[i-2];
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		scanf("%d",&n);
		memset(dp,-1,sizeof(dp));
		for(int i=2;i<=n;++i)
			dp[1][i] = 1;
		//cal(4,6);
		int res=0;
		for(int i=1;i<=n-1;++i)
		{res += cal(i,n);
		res%=100003;
		}
		printf("Case #%d: %d\n",x,res);
	}
	return 0;
}