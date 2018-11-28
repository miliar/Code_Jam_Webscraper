#include <climits>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(iter, cont) \
	for (typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)

double solve()
{
	int x, s, r, n;
	double t;
	cin >> x >> s >> r >> t >> n;
	r -= s;

	vector < pair<int, int> > speed;
	speed.reserve(n);
	int a[n+1], b[n+1], w[n+1];
	b[0] = 0;
	for (int i = 1; i <= n; ++i) {
		cin >> a[i] >> b[i] >> w[i];
		if (b[i-1] != a[i]) {
			speed.push_back(make_pair(s, a[i] - b[i-1]));
		}
		speed.push_back(make_pair(s+w[i], b[i]-a[i]));
	}
	if (b[n] != x) {
		speed.push_back(make_pair(s, x - b[n]));
	}

	sort(speed.begin(), speed.end());

	double res = 0.0;
	foreach(it, speed) {
		if (abs(t) < 1e-6) {
			res += (it->second+0.0) / it->first;
			continue;
		}

		double l = it->second;
		double run_time = min(l / (it->first + r), t);

		t -= run_time;
		res += run_time;
		l -= run_time * (it->first + r);
		res += l / it->first; // walk
	}

	return res;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i+1 << ": ";
		printf("%.7lf\n", solve());
	}
}
