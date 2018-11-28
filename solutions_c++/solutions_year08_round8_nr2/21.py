#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;

string c[10];
int a[10], b[10];
int N;

void read_data () {
	cin >> N;

	for (int i = 0; i < N; ++i) {
		cin >> c[i];
		cin >> a[i];
		cin >> b[i];
	}
}

void solve () {
	int mn = 1000;

	for (int mask = 0; mask < (1 << N); ++mask) {
		set< string > q;
		int cur = 0;

		for (int i = 0; i < N; ++i)
			if (mask & (1 << i)) { q.insert (c[i]); ++cur; }

		if (q.size () > 3) continue;

		bool flag = true;
		for (int i = 1; i <= 10000; ++i) {
			bool c = false;

			for (int j = 0; j < N; ++j)
				if ((mask & (1 << j)) && a[j] <= i && b[j] >= i) { c = true; break; }

			if (!c) { flag = false; break; }
		}

		if (flag && mn > cur) mn = cur;
	}

	if (mn == 1000)
		cout << "IMPOSSIBLE" << endl;
	else cout << mn << endl;
}

int main () {
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int t = 0; t < T; ++t) {
		cout << "Case #" << t+1 << ": ";

		read_data ();
		solve ();
	}

	return 0;
}
