#include <iostream>
#include <cstdio>
#include <vector>

#define SIZE(c) (int) (c).size()

using namespace std;

void go(int& i, int x) {
	if (i < x)
		i++;
	else
		i--;
}

void solve(int test) {
	int n;
	cin >> n;
	vector<pair<char, int> > a(n);
	vector<int> x, y;
	for (int i = 0; i < n; i++)
		cin >> a[i].first >> a[i].second;
	for (int i = 0; i < n; i++)
		if (a[i].first == 'O')
			x.push_back(a[i].second);
		else
			y.push_back(a[i].second);
	int res = 0, i, j;
	i = j = 1;
	while (SIZE(a) > 0) {
		res++;
		if (SIZE(x) > 0 && SIZE(y) > 0) {
			int k = 0;
			if (i != x[0]) {
				go(i, x[0]);
			} else {
				if (a[0].first == 'O' && a[0].second == x[0]) {
					x.erase(x.begin());
					a.erase(a.begin());
					k = 1;
				}
			}
			if (j != y[0]) {
				go(j, y[0]);
			} else {
				if (k == 0 && a[0].first == 'B' && a[0].second == y[0]) {
					y.erase(y.begin());
					a.erase(a.begin());
				}
			}
		} else if (SIZE(x) > 0) {
			if (i != x[0]) {
				go(i, x[0]);
			} else {
				if (a[0].first == 'O' && a[0].second == x[0]) {
					x.erase(x.begin());
					a.erase(a.begin());
				}
			}
		} else if (SIZE(y) > 0) {
			if (j != y[0]) {
				go(j, y[0]);
			} else {
				if (a[0].first == 'B' && a[0].second == y[0]) {
					y.erase(y.begin());
					a.erase(a.begin());
				}
			}
		}
	}
	cout << "Case #" << test << ": " << res << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;
	cin >> nTest;

	for (int i = 0; i < nTest; i++)
		solve(i + 1);

	return 0;
}
