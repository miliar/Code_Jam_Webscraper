
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;

int rec2(int L, int P, int C, int cache[1001][1001]) {
	if (L * C >= P)
		return 0;
	int &res = cache[L][P];
	if (res >= 0)
		return res;
	res = 0x3f3f3f3f;
	vector<int> ans;
	for (int i = L + 1; i < P; ++i) {
		res = min(res, max(rec2(L, i, C, cache), rec2(i, P, C, cache)) + 1);
	}
	if (L == 50 && P == 700) {
		for (int i = L + 1; i < P; ++i)
			if (max(rec2(L, i, C, cache), rec2(i, P, C, cache)) + 1 == res) {
				cout << i << " ";
			}
		cout << endl;
	}
	return res;
}

int rec(LL L, LL P, LL C, int cache[1001][1001]) {
	if (L * C >= P)
		return 0;
	LL x = LL(sqrt(0.0 + L * P + 1e-9));
	int res = 0x3f3f3f3f;
	for (LL I = x - 1; I <= x + 1; ++I)
		if (I > L && I < P) {
			res = min(res, max(rec(L, I, C, cache), rec(I, P, C, cache)) + 1);
		}
	return res;
}

int main() {
	vector<pair<int, pair<int, int> > > tests[11];
	int cases;
	cin >> cases;
	for (int cas = 0; cas < cases; ++cas) {
		int L, P, C;
		cin >> L >> P >> C;
		tests[C].push_back(make_pair(cas, make_pair(L, P)));
	}
	
	static int ans[1000];
	for (int C = 2; C <= 10; ++C) {
		static int cache[1001][1001];
		memset(cache, -1, sizeof(cache));
		for (int i = 0; i < int(tests[C].size()); ++i) {
			ans[tests[C][i].first] = rec(tests[C][i].second.first, tests[C][i].second.second, C, cache);
			fprintf(stderr, "!");
			fflush(stderr);
		}
	}
	for (int cas = 0; cas < cases; ++cas)
		printf("Case #%d: %d\n", cas + 1, ans[cas]);
	return 0;
}