#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <ctype.h>
#include <queue>
using namespace std;

const long long MOD = 100003;

vector <vector <long long> > dp;
vector <vector <long long> > c;

long long C(int n, int k)
{
	if (n < k )
		return 0;
	if (n == k || k == 0 || n == 0)
		return 1;
	if (c[n][k] != -1)
		return c[n][k];
	return c[n][k] = (C(n-1,k-1)+C(n-1,k))%MOD;
}

long long DP(int n, int k)
{
	if (k == 1)
		return 1;
	if (dp[n][k] != -1)
		return dp[n][k];
	long long ans = 0;
	for (int r = 1; r < k; r ++)
		ans = (ans + DP(k,r)* C(n-k-1,k-r-1))%MOD;
	if (ans < 0)
		throw 4242;
	return dp[n][k] = ans;
}

long long Solve(int n)
{
	int ans = 0;
	dp.assign(n+1, vector <long long>(n+1,-1));
	for (int k = 1; k < n; k ++)
		ans = (ans + DP(n,k))%MOD;
	return ans;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t ;
	cin >> t;
	c.assign(501, vector <long long>(501,-1));
	for (int test = 0; test < t ; test ++)
	{
		int n;
		cin >> n;
		cout << "Case #" << test+1 << ": " << Solve(n) << endl;
	}
	return 0;
}
