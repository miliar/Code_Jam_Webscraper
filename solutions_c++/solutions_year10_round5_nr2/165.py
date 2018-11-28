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

const int maxw = 100000;
int dp[maxw];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		LL len;
		int n;
		cin >> len >> n;
		vector<int> a(n);
		for(int i = 0; i < n; ++i)
			cin >> a[i];
		memset(dp, -1, sizeof dp);
		dp[0] = 0;
		for(int i = 0; i < n; ++i)
			for(int j = a[i]; j < maxw; ++j)
				if(dp[j - a[i]] != -1)
				{
					if(dp[j] == -1 || dp[j] > dp[j - a[i]] + 1)
						dp[j] = dp[j - a[i]] + 1;
				}
		LL res = -1;
		for(int i = 1; i < maxw; ++i)
			if(dp[i] != -1 && dp[len % i] != -1)
			{
				if(res == -1 || res > dp[i] * LL(len/i) + dp[len % i])
					res = dp[i] * LL(len/i) + dp[len % i];
			}
		if(res == -1)
			cout << "Case #" << z + 1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << z + 1 << ": " << res << endl;
	}
	
	return 0;
}
#endif