#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;

const int nmax = 10000;
typedef pair<int, int> pi;
pi v[nmax];

int main() {
	int nt, it;

	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int n, i, t;

		cin >> n;
		for (i = 0; i < n; i++) cin >> t;
		for (i = 0; i < n; i++) cin >> v[i].first, v[i].first = -v[i].first, v[i].second = i;

		sort(v, v + n);

		cout << "Case #" << it << ':';
		for (i = 0; i < n; i++) cout << ' ' << v[i].second;
		cout << endl;
	}

	return 0;
}
