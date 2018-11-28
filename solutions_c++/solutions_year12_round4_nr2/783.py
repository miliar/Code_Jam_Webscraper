#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int N, W, L;
vector<int> r;

double randd() {
	return rand() / (RAND_MAX + 1.0);
}

vector<pair<double,double> > func() {
	vector<pair<double,double> > ans(N);
	for (;;) {
		for (int i = 0; i < N; ++ i) {
			ans[i].first = randd() * W;
			ans[i].second = randd() * L;
		}
		for (int i = 1; i < N; ++ i) {
			for (int j = 0; j < i; ++ j) {
				double dx = ans[i].first-ans[j].first;
				double dy = ans[i].second-ans[j].second;
				if (sqrt(dx*dx + dy*dy) <= r[i]+r[j]+1e-2) goto next;
			}
		}
		return ans;
		next:;
	}
}

int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++ tt) {
		cin >> N >> W >> L;
		r = vector<int>(N);
		for (int i = 0; i < N; ++ i) {
			cin >> r[i];
		}
		vector<pair<double,double> > ans = func();
		printf("Case #%d:", tt);
		for (int i = 0; i < N; ++ i) {
			printf(" %f %f", ans[i].first, ans[i].second);
		}
		printf("\n");
	}
}
