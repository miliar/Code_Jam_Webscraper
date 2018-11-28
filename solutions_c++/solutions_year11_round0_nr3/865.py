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

const int MAXN = 1005;

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		int n, a[MAXN], s = 0, sum = 0, mn = 1000000000;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			s ^= a[i];
			sum += a[i];
			mn = min(mn, a[i]);
		}
		if (s != 0)
			printf("Case #%d: NO\n", t);
		else
			printf("Case #%d: %d\n", t, sum - mn);
	}
	return 0;
}

