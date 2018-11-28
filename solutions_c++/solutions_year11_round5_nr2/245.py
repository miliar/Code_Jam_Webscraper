#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)

using namespace std;

const int MAXN = 10;

int n, a[MAXN], dp[1 << MAXN];

bool good(int mask, int a[], int n) {
	vector< int > v;
	for (int i = 0; i < n; i++)
		if (mask & (1 << i))
			v.push_back(a[i]);
	for (int i = 1; i < sz(v); i++)
		if (v[i] != v[i - 1] + 1)
			return false;
	return true;
}

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		sort(a, a + n);
		same(dp, 0);
		dp[0] = n;
		for (int i = 0; i < (1 << n); i++)
			for (int j = 0; j < (1 << n); j = (i + j + 1) & ~i)
				if (good(j, a, n))
					dp[i | j] = max(dp[i | j], min(__builtin_popcount(j), dp[i]));
		printf("Case #%d: %d\n", t, dp[(1 << n) - 1]);
	}
	return 0;
}

