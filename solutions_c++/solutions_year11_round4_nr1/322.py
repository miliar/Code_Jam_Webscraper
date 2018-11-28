#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const long double eps = 1e-9;

vector <pair<int, int> > a;
int t;
int ds;
int x;

void Load()
{
	int s, n, r;
	cin >> x >> s >> r >> t >> n;
	ds = max(0, r - s);
	int i;
	a.clear();
	int prev = 0;
	for (i = 0; i < n; i++) {
		int b, e, w;
		cin >> b >> e >> w;
		if (b > prev) {
			a.push_back(make_pair(s, b-prev));
		}
		a.push_back(make_pair(w+s,e-b));
		prev = e;
	}
	if (prev < x) {
		a.push_back(make_pair(s,x-prev));
	}
	sort(a.begin(), a.end());
}

void Solve()
{
	long double ans = 0;
	long double lt = t;
//	cerr << "\n";
	for (int i = 0; i < (int)a.size(); i++) {
		long double spd = a[i].first;
		long double len = a[i].second;
		long double cl = (spd+ds)*lt;
//		cerr << len << ' ' << spd << '\n';
		if (cl > len + eps) {
			long double cur = len / (spd+ds);
			ans += cur;
			lt -= cur;
		} else {
			long double cur = lt + (len - cl) / spd;
			lt = 0;
			ans += cur;
		}
	}
//	cerr << "\n";
	cout << ans << "\n";
}

int main()
{
	int nt, tt;
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
