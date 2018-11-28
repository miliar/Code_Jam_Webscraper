#include <cstdio>
#include <iostream>

using namespace std;

int dist2(int x0, int y0, int x1, int y1) {
	return (x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0);
}

struct segment {
	double len, speed, inc;
	bool operator <(const segment&x) const {
		return speed < x.speed;
	}
} seg[1001];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst, T;
	cin >> T;
	for (tst = 1; tst <= T; tst++) {
		double x, s, r, t, st, e, v;
		double ans;
		int n, i, j, k;
		cin >> x >> s >> r >> t >> n;
		for (i = 0; i <= n; i++) {
			seg[i].inc = r - s;
			seg[i].speed = seg[i].len = 0;
		}
		seg[n].speed = s;
		double l = 0.0;
		for (i = 0; i < n; i++) {
			cin >> st >> e >> v;
			if (st > l)
				seg[n].len += st - l;
			seg[i].len = e - st;
			seg[i].speed = v + s;
			l = e;
		}
		if (x > l)
			seg[n].len += x - l;
		n++;
		sort(seg, seg + n);
		/*for (i = 0; i < n; i++)
		 cout << seg[i].speed << " " << seg[i].len << endl;
		 cout<<(seg[0]<seg[1])<<endl;
		 */
		ans = 0.0;
		for (i = 0; i < n; i++) {
			if (t * (seg[i].inc + seg[i].speed) >= seg[i].len) {
				ans += seg[i].len / (seg[i].inc + seg[i].speed);
				t -= seg[i].len / (seg[i].inc + seg[i].speed);
				continue;
			}
			ans += t;
			seg[i].len -= t * (seg[i].inc + seg[i].speed);
			t = 0;
			ans += seg[i].len / seg[i].speed;
		}
		printf("Case #%d: ", tst);
		printf("%.7lf\n", ans);
	}

	return 0;
}
