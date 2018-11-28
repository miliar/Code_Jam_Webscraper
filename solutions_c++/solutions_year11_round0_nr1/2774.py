#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cassert>

#define vv vector
#define pb push_back
#define mp make_pair
#define px first
#define py second
#define in cin
#define out cout
#pragma warning(disable: 4996)

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cases;
	in >> cases;

	for (int tcase = 0; tcase < cases; ++tcase) {
		int n;
		in >> n;
		vv< pair<bool, int> > seq(n);
		for (int i = 0; i < n; ++i) {
			char c;
			in >> c >> seq[i].py;
			seq[i].px = (c == 'B');
		}
		int l = 1, r = 1, time = 0, time_l = 0, time_r = 0, cost;
		for (int i = 0; i < n; ++i) {
			if (seq[i].px) {
				cost = max(0, abs(l - seq[i].py) - time_l);
				l = seq[i].py;
				time += cost + 1;
				time_l = 0;
				time_r += cost + 1;
			} else {
				cost = max(0, abs(r - seq[i].py) - time_r);
				r = seq[i].py;
				time += cost + 1;
				time_r = 0;
				time_l += cost + 1;
			}
		}
		out << "Case #" << tcase + 1 << ": " << time << endl;
	}

	return 0;
}