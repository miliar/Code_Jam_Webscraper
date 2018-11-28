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

const int max_n = 1024;

long long ans;
int T, I;
int R, k, n;
int a[max_n], b[max_n], pos[max_n];
int money[max_n], next[max_n];

void input() {
	scanf("%d %d %d", &R, &k, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
}

void solve() {
	for (int i = 0; i < n; i++) {
		int sum = 0;
		int j = i;
		while (sum + a[j] <= k) {
			sum += a[j];
			j = (j + 1) % n;
			if (j == i)
				break;
		}
		money[i] = sum;
		next[i] = j;
	}
	memset(pos, -1, sizeof pos);
	ans = 0;
	int i = 0;
	for (int r = 0; r < R; r++) {
		pos[i] = r;
		b[r] = i;
		ans += money[i];
		i = next[i];
		if (pos[i] != -1) {
			int j = pos[i];
			long long sum = 0;
			for (int t = j; t <= r; t++)
				sum += money[b[t]];
			int len = r - j + 1;
			int num = (R - 1 - r) / len;
			ans += (long long)num * sum;
			R -= num * len;
			memset(pos, -1, sizeof pos);
		}
	}
}

void output() {
	printf("Case #%d: %lld\n", I + 1, ans);
}

int main() {
	scanf("%d", &T);
	for (I = 0; I < T; ++I) {
		input();
		solve();
		output();
	}
	return 0;
}

