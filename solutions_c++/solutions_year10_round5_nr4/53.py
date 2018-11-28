#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;

map<pair<int, int>, int> res;

int ans;
int k;

int a[100], cnt, b[100];

inline bool check() {
	int n = 0, t = a[cnt-1];
	while (t) {
		b[n++] = t % k;
		t /= k;
	}
	for (int i = 0; i < cnt-1; ++i) {
		t = a[i];
		for (int j = 0; j < n; ++j) {
			if (t % k == b[j]) return false;
			t /= k;
		}
	}
	return true;
}

void search(int n) {
	if (n == 0) {
		++ ans;
		return;
	}
	int last;
	if (cnt) last = a[cnt-1] - 1;
	else last = n;
	for (int i = min(n, last); i >= 1; --i) {
		a[cnt++] = i;
		if (check())
			search(n - i);
		--cnt;
	}
}

int solve() {
	int n;
	scanf("%d%d", &n, &k);
	map<pair<int, int>, int>::iterator iter;
	iter = res.find(make_pair(n, k));
	if (iter != res.end())
		return iter->second;
	ans = cnt = 0;
	search(n);
	res[make_pair(n, k)]=ans;
	return ans;
}

int main() {
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T -- > 0) {
		printf("Case #%d: %d\n", ++tc, solve());
		cerr << tc << endl;
	}
	return 0;
}
