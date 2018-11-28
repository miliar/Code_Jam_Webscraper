// Alex Fetisov

#include <cstdio>

void initf() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
}

#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <string>
#include <cassert>

using namespace std;

const int maxn = 1004;

int n, w, h;
int r[maxn], idx[maxn];

bool cmp(int a, int b) {
	return r[a] < r[b];
}

void solve() {
	scanf("%d%d%d", &n, &w, &h);
	for (int i = 0; i < n; ++i) {
		scanf("%d", r + i);
		idx[i] = i;
	}
	sort(idx, idx + n, cmp);
	int ptr = 0;
	int past = 0;
	vector < int > x(n, 0), y(n, 0);
	int hei = 0, ma = 0;
	while (ptr < n) {
		if (past == 0) {
			x[idx[ptr]] = (0);
			y[idx[ptr]] = (hei == 0 ? 0 : hei + r[idx[ptr]]);
			ma = max(ma, r[idx[ptr]]);
			past += r[idx[ptr]];
			++ptr;
		} else {
			if (past + r[idx[ptr]] <= w) {
				x[idx[ptr]] = (past + r[idx[ptr]]);
				ma = max(ma, r[idx[ptr]]);
				y[idx[ptr]] = (hei == 0 ? 0 : hei + r[idx[ptr]]);
				past += 2 * r[idx[ptr]];
				++ptr;
			} else {
				hei += 2 * ma;
				past = 0;
				ma = 0;
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		if (!(x[i] >= 0 && x[i] <= w) || !(y[i] >= 0 && y[i] <= h)) {
			throw 42;        
        }
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < i; ++j) {
			long long dst = (x[i] - x[j]) * 1ll * (x[i] - x[j]) + (y[i] - y[j]) * 1ll * (y[i] - y[j]);
			long long val = r[i] * 1ll * r[i] + 2LL * r[i] * r[j] + r[j] * 1ll * r[j];
			if (!(dst >= val)) {
				throw 42;  
			}

		}
	}
    for (int i = 0; i < n-1; ++i) {
		printf("%d %d ", x[i], y[i]);
	}
	printf("%d %d\n", x[n-1], y[n-1]);
}

int main() {
	initf();
	int Test;
	scanf("%d", &Test);
	for (int i = 1; i <= Test; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}