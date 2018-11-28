#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <iomanip>
#include <cmath>
#include <sstream>

using namespace std;

#define pie pair <int, int>
#define ff first
#define ss second

const int maxN = 10000 + 10;

int n, D;
int d[maxN], l[maxN];
bool c[maxN][maxN], e[maxN];

void solve_small() {
	for (int i = n - 1; i >= 0; i--) {
		for (int j = i - 1; j >= 0; j--) if (l[i] >= d[i] - d[j]) {
			if (D - d[i] <= d[i] - d[j]) c[i][j] = true;
			for (int k = i + 1; k < n; k++) if (d[k] - d[i] <= d[i] - d[j])
				if (l[k] > d[k] - d[i]) {
					if (c[k][i]) c[i][j] = 1;
				}
				else if (e[k]) c[i][j] = 1;
		}
		if (l[i] >= D - d[i]) e[i] = 1;
		for (int k = i + 1; k < n; k++) if (d[k] - d[i] <= l[i])
			if (l[k] > d[k] - d[i]) {
				if (c[k][i]) e[i] = 1;
			}
			else if (e[k]) e[i] = 1;
	}
	cout << (e[0] ? "YES" : "NO") << endl;
}

void solve () {
	for (int i = n - 1; i >= 0; i--) {
		int find = 0, p = i + 1;
		for (int j = i - 1; j >= 0 && d[i] - d[j] < l[i]; j--) {
			if (d[i] - d[j] >= D - d[i]) find = true;
			while (p < n && d[p] - d[i] <= d[i] - d[j]) {
				if (l[p] > d[p] - d[i]) find |= c[p][i];
				else find |= e[p];
				p++;
			}
			c[i][j] = find;
		}
		if (l[i] >= D - d[i]) find = true;
		while (p < n && d[p] - d[i] <= l[i]) {
			if (l[p] > d[p] - d[i]) find |= c[p][i];
			else find |= e[p];
			p++;
		}
		e[i] = find;
	}

	cout << (e[0] ? "YES" : "NO") << endl;
}

int main()
{
	ios::sync_with_stdio (false);

	int tests; cin >> tests;
	for (int i = 1; i <= tests; i++) {
		memset (e, 0, sizeof e);
		memset (c, 0, sizeof c);
		cin >> n;
		for (int j = 0; j < n; j++) cin >> d[j] >> l[j];
		l[0] = d[0];
		cin >> D;
		cout << "Case #" << i << ": ";
		solve();
	}
		
	return 0;
}
