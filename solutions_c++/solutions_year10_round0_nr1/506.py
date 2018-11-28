
#include <cstdio>
#include <vector>
#include <cassert>
#include <iostream>
using namespace std;

vector<pair<int, int> > tests;

int main() {
	int cases;
	cin >> cases;
	for (int cas = 0; cas < cases; ++cas) {
		pair<int, int> test;
		cin >> test.first >> test.second;
		tests.push_back(test);
	}
	vector<int> order;
	for (int cas = 0; cas < cases; ++cas)
		order.push_back(cas);
	for (int i = 0; i < int(order.size()); ++i)
		for (int j = i + 1; j < int(order.size()); ++j)
			if (tests[order[i]] > tests[order[j]]) {
				swap(order[i], order[j]);
			}
	
	int at = 0;
	vector<int> ans(cases, -1);
	for (int N = 1; N <= 30; ++N) {
		fprintf(stderr, "N = %d\n", N);
		fflush(stdout);
		int on = 1;
		int power = 1;
		int K = 0;
		do {
			while (at < int(order.size()) && tests[order[at]].first == N && tests[order[at]].second == K) {
				ans[order[at]] = ((on & (1 << N)) != 0 && (power & (1 << N)) != 0) ? 1 : 0;
				++at;
			}
			int next_on = on;
			int next_power = 1;
			
			for (int j = 1; j <= N; ++j)
				if ((power & (1 << (j - 1))) != 0 && (on & (1 << (j - 1))) != 0) {
					next_on ^= 1 << j;
				} else
					break;
			for (int j = 1; j <= N; ++j)
				if ((next_on & (1 << (j - 1))) != 0) {
					next_power |= 1 << j;
				} else
					break;
			on = next_on;
			power = next_power;
			++K;
		} while (K <= 100000005);
	}
	
	for (int cas = 0; cas < cases; ++cas) {
		printf("Case #%d: %s\n", cas + 1, ans[cas] ? "ON" : "OFF");
		assert(ans[cas] == 0 || ans[cas] == 1);
	}
	return 0;
}
