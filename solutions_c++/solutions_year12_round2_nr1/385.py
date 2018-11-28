#pragma comment(linker, "/STACK:128000000")

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>

using namespace std;

int n;
int s[1000];
int sum;

double Score(int id, double share) {
	return 1. * s[id] + sum * share / 100.;
}

bool Eliminate(int id, double share) {
	double score = Score(id, share);
	share = 100. - share;
	for (int i = 0; i < n; ++i) {
		if (i == id) {
			continue;
		}

		double x = (1. * score - s[i]) / sum * 100;
		if (x < 0) {
			x = 0;
		}
		share -= x;
	}

	return (share >= -1e-7);
}

void Out(int id) {
	double L = 0, R = 100;
	for (int step = 0; step < 100; ++step) {
		double mid = (L + R) / 2.;
		if (Eliminate(id, mid)) {
			L = mid;
		} else {
			R = mid;
		}
	}
	printf("%lf ", (L + R) / 2.);
}

void Solve() {
	sum = 0;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> s[i];
		sum += s[i];
	}

	for (int i = 0; i < n; ++i) {
		Out(i);
	}
	printf("\n");
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}