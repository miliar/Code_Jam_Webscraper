#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
#define y1 botva23
typedef long long int64;
typedef long double ld;

const int inf = 2000000000;
const ld eps = 1e-07;

int n;
ld w, l;
ld r[2000];
pair <ld, ld> res[2000];

void solve() {
	int n;
	scanf("%d", &n);
	ld w, l;
	cin >> w >> l;
	for (int i = 0; i < n; ++i)
		cin >> r[i];
	bool f = true;
	bool rev = false;
	
	ld curh = 0;
	ld dist = 0;
	ld maxr = 0;
	
	cout.precision(4);
	int i = 0;

	while (i < n) {
		if (!f && (dist + r[i] > w)) {
			f = true;
			curh = maxr;
			continue;
		}
		if (f) {
			f = false;
			res[i] = mp(0, min(curh + r[i], l));
			dist = r[i];
			maxr = curh + 2 * r[i];
		}
		else {
			res[i] = mp(dist + r[i], min(curh + r[i], l));
			dist += 2 * r[i];
			maxr = max(maxr, curh + 2 * r[i]);
		}
		++i;
	}

	for (int i = 0; i < n; ++i) {
		if (rev)
			swap(res[i].first, res[i].second);
		cout << fixed << res[i].first << " ";
		cout << fixed << res[i].second << " ";
	}
	cout << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		cerr << i << endl;
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}