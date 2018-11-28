#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;

const LL mod = 100003;
const int maxn = 501;
LL dp[maxn][maxn];
LL cnk[maxn][maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	memset(cnk, 0, sizeof cnk);
	for(int i = 0, j; i < maxn; ++i)
		for(cnk[i][0] = j = 1; j <= i; ++j)
			cnk[i][j] = (cnk[i - 1][j] + cnk[i - 1][j - 1]) % mod;

	memset(dp, 0, sizeof dp);
	for(int i = 2; i < maxn; ++i)
	{
		dp[i][1] = 1;
		
		for(int j = 2; j < i; ++j)
		{
			
			for(int k = 1; k < j; ++k)
			{
				if(j - k <= i - j)
				{
					dp[i][j] += (dp[j][k] * cnk[i - j - 1][j - k - 1]) % mod;
					dp[i][j] %= mod;
				}
			}
		}
	}

	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n; scanf("%d", &n);
		int ans = 0;
		for(int i = 0; i < maxn; ++i)
			ans += dp[n][i],
			ans %= mod;
		printf("Case #%d: %d\n", z + 1, ans);

	}
	return 0;
}
#endif