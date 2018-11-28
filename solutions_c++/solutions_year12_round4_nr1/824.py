#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N = 10001;

int n;
pair<int, int> r[MAX_N];//d, l

int from[MAX_N];

bool possible() {
	for (int i = 0; i < n; i++)
		from[i] = -1;
	from[0] = 0;
	
	int pos = 1;
	for (int i = 0; i < n && from[i] != -1; i++) {
		while (pos < n && 2 * r[i].first - from[i] >= r[pos].first) {
			from[pos] = max(r[i].first, r[pos].first - r[pos].second);
			pos++;
		}
	}
	return from[n-1] != -1;
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> r[i].first >> r[i].second;
		int dist;
		cin >> dist;
		r[n].first = dist;
		r[n].second = 0;
		n++;
		sort(r, r+n);
		cout << "Case #" << test << ": ";
		if (possible())
			cout << "YES" << endl;
		else
			cout <<  "NO" << endl;
	}
	return 0;
}
