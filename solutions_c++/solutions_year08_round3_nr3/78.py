#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

int dp[1002][1002];
int A[1002];
int arr[1002];
int n;
const int MOD = 1000000007;

int dfs(int ind, int last)
{
	if(ind == n)
		return 0;

	int& ret=dp[ind][last];
	if(ret>=0)
	{
		return ret;
	}
	ret=0;
	if(last>n || arr[ind]>arr[last])
	{
		ret = (ret + dfs(ind+1,ind)+1)% MOD;
	}
	ret = (ret + dfs(ind+1, last)) % MOD;

	return ret;
}
int main(void)
{
	freopen("C-small-attempt0.in","r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int numCase;
	cin >> numCase;

	
	long long X,Y,Z;
	int m;

	for(int c=1; c<=numCase; c++)
	{
		memset(dp,-1,sizeof(dp));
		cin >> n >> m >> X >> Y >> Z;
		for(int i=0; i<m; ++i)
			cin >> A[i];

		for(int i=0; i<n; i++)
		{
			arr[i]=A[i%m];
			A[i%m]=(X*A[i%m]+Y*(i+1))%Z;
		}

		int ret=dfs(0,1001);

		printf("Case #%d: %d\n", c, ret); 
		
	}
	return 0;
}