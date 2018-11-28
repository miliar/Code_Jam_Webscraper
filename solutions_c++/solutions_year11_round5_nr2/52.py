#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

typedef pair<int, int> P;

P cs[1010];
int fr[1010], ff[1010];

bool ok(int num, int p) {
	for(int i = 0; i < p; ++i) {
		fr[i] = cs[i].second;
		ff[i] = 0;
	}
	for(int i = 0; i < p; ++i) {
		if(ff[i] != 0) {
			int ne = min(fr[i], ff[i]);
			fr[i] -= ne;
			if(i != p - 1 && cs[i].first == cs[i + 1].first - 1) ff[i + 1] += ne;
		}
		if(!fr[i]) continue;
		int len = 0;
		for(int j = i; j < p; ++j) {
			if(cs[i].first + num - 1 >= cs[j].first && fr[i] <= fr[j]) ++len;
		}
		if(len < num) return false;
		for(int j = i + 1; j < p; ++j) {
			if(cs[i].first + num - 1 >= cs[j].first) fr[j] -= fr[i];
			if(cs[i].first + num == cs[j].first) ff[j] += fr[i];
		}
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	for(int c = 1; c <= T; ++c) {
		int n;
		cin >> n;
		vector<int> num(10010, 0);
		for(int i = 0; i < n; ++i) {
			int a;
			cin >> a;
			++num[a];
		}
		int p = 0;
		for(int i = 0; i < 10001; ++i) if(num[i]) {
			cs[p++] = P(i, num[i]);
		}
		int left = 0, right = n + 1;
		while(right - left > 1) {
			int half = (right + left) / 2;
			if(ok(half, p)) left = half;
			else right = half;
		}
		printf("Case #%d: %d\n", c, left);
	}
	return 0;
}
