#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

int T, n, e, q, a[2], p[2];
char c;
vector<pii> v;

int main() {
	ifstream in("A-large.in");
	freopen("A-large.out", "w", stdout);
	in >> T;
	for (int t = 0; t < T; t++) {
		in >> n;
		v.clear();
		for (int i = 0; i < n; i++) {
			in >> c >> e;
			v.push_back(make_pair(c == 'B', e));
		}
		a[0] = a[1] = 0;
		p[0] = p[1] = 1;
		q = v[0].first;
		int ans = 0;
		for (int i = 0; i < n; ) {
			int st = 0, pr = 0;
			do {
				if (pr == 0)
					st += max(0, abs(v[i].second - p[q]) - a[q]) + 1;
				else
					st += abs(v[i].second - p[q]) + 1;
				p[q] = v[i].second;
				pr ++;
				i++;
			} while (i < n && v[i].first == v[i-1].first);
			ans += st;
			a[q] = 0;
			q ^= 1;
			a[q] = st;
		}
		printf("Case #%d: %d\n", t+1, ans);
	}
}