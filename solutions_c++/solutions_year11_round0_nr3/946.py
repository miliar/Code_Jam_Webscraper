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
#include <list>
#include <ctime>
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
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }


const int maxn = 1 << 20;
int dp1[maxn];
int dq1[maxn];
int *dp = dp1, *dq = dq1;
int a[maxn];
int main()
{
	time_t tStart = clock();
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%d", &a[i]);

		int sum = 0;
		int allXor = 0;
		for(int i = 0; i < n; ++i)
		{
			sum += a[i];
			allXor ^= a[i];
		}

		dp = dp1;
		dq = dq1;
		memset(dp, -1, sizeof(dp[0]) * maxn);
		dp[0] = 0;

		for(int i = 0; i < n; ++i)
		{
			memcpy(dq, dp, sizeof(dq[0]) * maxn);
			int cur = a[i];
			for(int j = 0; j < maxn; ++j)
				if(dp[j] != -1 && dp[j] + cur < sum)
				{
					int nj = j ^ cur;
					if(dq[nj] == -1 || dq[nj] < dp[j] + cur)
					{
						dq[nj] = dp[j] + cur;
					}
				}
			//memcpy(dp, dq, sizeof dp);
			swap(dp, dq);
		}

		int res = 0;
		for(int i = 0; i < maxn; ++i)
			if(dp[i] != -1 && (allXor ^ i) == i)
				res = max(res, dp[i]);

		if(res)
			cout << "Case #" << z + 1 << ": " << res << endl;
		else
			cout << "Case #" << z + 1 << ": NO" << endl;
	}

	time_t tEnd = clock();
	dbg((tEnd - tStart) / LD(CLOCKS_PER_SEC));
	return 0;
}
#endif

