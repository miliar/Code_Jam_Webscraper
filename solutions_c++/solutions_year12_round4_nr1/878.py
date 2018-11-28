#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int N, D;
vector<int> d, l;
set<pair<int,int> > visited;

bool f(int p, int q) {
	if (!visited.insert(make_pair(p, q)).second) return false;
	if (D <= d[p]+q) return true;
	for (int i = 0; i < N; ++ i) if (i != p) {
		if (d[p]-q <= d[i] && d[i] <= d[p]+q) {
			if (f(i, min(l[i], abs(d[i]-d[p])))) return true;
		}
	}
	return false;
}

bool func() {
	visited.clear();
	return f(0, d[0]);
}

int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++ tt) {
		cin >> N;
		d = vector<int>(N);
		l = vector<int>(N);
		for (int i = 0; i < N; ++ i) {
			cin >> d[i] >> l[i];
		}
		cin >> D;
		printf("Case #%d: %s\n", tt, func() ? "YES" : "NO");
	}
}
