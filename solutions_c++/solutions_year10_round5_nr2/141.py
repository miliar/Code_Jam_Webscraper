#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-8;
const Real pi = acos(-1.0);
const long long oo = 0x7fffffffffffffffLL;

const int max_n = 128;
const int max_m = 100000 * 3;

long long ans, L;
int n;
int a[max_n];
int c[max_m];
int T, I;

int gcd(int a, int b) {
	if (b == 0)
		return a;
	return gcd(b, a % b);
}

void input() {
	scanf("%lld", &L);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
}

void solve() {
	int g = 0;
	for (int i = 0; i < n; i++) {
		g = gcd(g, a[i]);
	}
	if (L % g != 0) {
		ans = -1;
		return;
	}
	memset(c, -1, sizeof c);
	c[0] = 0;
	for (int k = 1; k < max_m; k++) {
		for (int i = 0; i < n; i++) {
			if (k < a[i])
				continue;
			int k1 = k - a[i];
			if (c[k1] == -1)
				continue;
			int tmp = c[k1] + 1;
			if (c[k] == -1 || c[k] > tmp)
				c[k] = tmp;
		}
	}
	ans = oo;
	for (int k = 0; k < max_m; k++) {
		if (c[k] == -1)
			continue;
		for (int i = 0; i < n; i++) {
			if ((L - k) % a[i] == 0) {
				long long cur = c[k] + (L - k) / a[i];
				if (cur < ans)
					ans = cur;
			}
		}
	}
	assert(ans != oo);
}

void output() {
	printf("Case #%d: ", I + 1);
	fprintf(stderr, "Case #%d: \n", I + 1);
	if (ans == -1) {
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("%lld\n", ans);
}

int main() {
	scanf("%d", &T);
	for (I = 0; I < T; I++) {
		input();
		solve();
		output();
	}
	return 0;
}

