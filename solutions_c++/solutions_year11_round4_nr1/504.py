#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <string>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

//#define DBG


string spam;
int n, m;
vector <int> a;
long long st[10000], fn[10000], sp[10000];

int main() {
#ifdef DBG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int j = 0; j < t; ++j) {
		long long x;
		cin >> x;
		long long s, r;
		cin >> s >> r;
		long double tt;
		cin >> tt;
		cin >> n;
		for (int i = 0; i < n; ++i) {
			int u, v, e;
			cin >> st[i] >> fn[i] >> sp[i];
		}
		int l1 = 0;
		vector <pair <long long, long long>> pp;
		pp.clear();
		for (int i = 0; i < n; ++i) {
			pp.push_back(make_pair(s, st[i] - l1));
			pp.push_back(make_pair(s + sp[i], fn[i] - st[i]));
			l1 = fn[i];
		}
		pp.push_back(make_pair(s, x - fn[n - 1]));
		sort(pp.begin(), pp.end());
		long double ans = 0;
		long double time = 0;
		for (int i = 0; i < pp.size(); ++i) {
			if (time < tt) {
				long double gg = tt - time;
				if (pp[i].second * 1.0 / (pp[i].first - s + r) < gg) {
					ans += pp[i].second * 1.0 / (pp[i].first - s + r);
					time += pp[i].second * 1.0 / (pp[i].first - s + r);
				} else {
					ans += gg;
					time += gg;
					long double ee = gg * (pp[i].first - s + r);
					ans += (pp[i].second - ee) * 1.0 / pp[i].first;
				}
			} else {
				ans += pp[i].second * 1.0 / pp[i].first; 
			}
		}
		cout << "Case #" << j + 1 << ": " << fixed << setprecision(7) << ans << endl;
	}
	return 0;
}