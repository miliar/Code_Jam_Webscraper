#pragma comment (linker, "/STACK:16000000")
#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

vector<long long> a;
int n;

int getmin(int a, int b)
{
	if (a == -1 || b == -1)
		return max(a, b);
	return min(a, b);
}

int solve(int rest)
{
		int dp[2000000];
		memset(dp, -1, sizeof(dp));
		dp[0] = 0;
		for (int i = 0; i < rest; i++)
			if (dp[i] + 1)
				for (int j = 0; j < n; j++)
					dp[i + a[j]] = getmin(dp[i + a[j]], dp[i] + 1);
		return dp[rest];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		long long sum;
		scanf("%lld%d", &sum, &n);
		a = vector<long long>(n);
		for (int i = 0; i < n; i++)
			scanf("%lld", &a[i]);
		sort(a.begin(), a.end());
		long long dd = (sum - 10000) / a[n - 1] * a[n - 1];
		long long rest = sum - dd;
		int res = solve(rest);
		if (res + 1)
			printf("Case #%d: %lld\n", testCount + 1, res + dd / a[n - 1]);
		else
			printf("Case #%d: IMPOSSIBLE\n", testCount + 1);			
	}
	return 0;
}