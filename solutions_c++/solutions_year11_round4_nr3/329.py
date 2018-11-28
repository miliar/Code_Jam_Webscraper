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

int fact[MAXN][MAXN];

void factorize(int x) {
	int y = x;
	for (int i = 2; i * i <= x; i++)
		while (x % i == 0) {
			fact[y][i]++;
			x /= i;
		}
	if (x > 1)
		fact[y][x]++;
}

int main() {
	for (int i = 1; i < MAXN; i++)
		factorize(i);
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		int n, mn = 1, mx = 0, lcm[MAXN] = {0};
		scanf("%d", &n);
		for (int i = 2; i <= n; i++) {
			bool add = false;
			for (int j = 2; j <= i; j++)
				if (fact[i][j] > lcm[j]) {
					lcm[j] = fact[i][j];
					add = true;
				}
			mn += add;
		}
		bool vis[MAXN] = {false};
		for (int i = 2; i <= n; i++) {
			if (vis[i])
				continue;
			for (int j = i; j <= n; j += i)
				vis[j] = true;
			mx++;
		}
		mx = max(mx, 1);
		printf("Case #%d: %d\n", t, mn - mx);
	}
	return 0;
}

