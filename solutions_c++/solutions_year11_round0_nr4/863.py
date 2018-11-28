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
		int n, a[MAXN], b[MAXN];
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			b[i] = a[i];
		}
		sort(b, b + n);
		int k = 0;
		for (int i = 0; i < n; i++)
			if (a[i] != b[i])
				k++;
		printf("Case #%d: %.6lf\n", t, (double)k);
	}
	return 0;
}

