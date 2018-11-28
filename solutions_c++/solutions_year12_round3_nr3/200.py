#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <map>
#include <vector>
#include <queue>
#include <memory.h>
using namespace std;
int A[102], B[102];
long long ai[102], bi[102];
int n, m;
long long dp[102][102];

long long f(int  op, int  oq,int i, int j) 
{
	if (i >= n || j >= m) 
	{
		dp[i][j] = 0;
		return 0;
	}
	if (op && oq && dp[i][j] != -1)
		return dp[i][j];
	long long ans = -1;
	if (A[i] != B[j]) 
	{
		long long tmp;
		tmp=f(1,oq,i+1, j);
		if(ans<tmp)
			ans=tmp;
		tmp=f(op,1,i, j+1);
		if(ans<tmp)
			ans=tmp;

	}
	else
	{
		long long k;
		if (ai[i] >bi[j])
		{
			k = bi[j];
			ai[i] -= k;
			ans = f(0,1,i, j+1) + k;
			ai[i] += k;

		}
		else if (ai[i] < bi[j])
		{
			k = ai[i];
			bi[j] -= k;
			ans = f(1,0,i+1, j) + k;
			bi[j] += k;
		}
		else 
		{
			k = ai[i];
			ans = f(1,1,i+1, j+1) + k;
		}
	}
	if (op && oq) 
		dp[i][j] = ans;
	return ans;
}



int main() 
{

	//freopen("D:\\visual studio 2008\\google code jam\\C-large (1).in", "r", stdin ) ;

	//freopen("D:\\visual studio 2008\\google code jam\\C-large (1).out", "w", stdout ) ;

	int cases;
	cin>>cases;
	for (int kk = 1; kk <= cases; ++kk)
	{
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			cin >> ai[i] >> A[i];
		for(int i = 0; i < m; i++)
			cin >> bi[i] >> B[i];
		memset(dp, -1, sizeof(dp));
		f(1,1,0, 0);
		printf("Case #%d: %lld\n", kk,dp[0][0]);
	}
	return 0;
}
