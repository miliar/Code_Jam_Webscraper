#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

const int MAXN = 50;

int _t;
int n, k, b, t, x[MAXN], s[MAXN], res, z;

int time(int i) {
	return (b - x[i]) / s[i] + ((b - x[i]) % s[i] != 0);
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	cin >> _t;
	for (int cas = 1; cas <= _t; cas++) {
		cin >> n >> k >> b >> t;
		res = 0; z = 0;
		for (int i = 0; i < n; i++) cin >> x[i];
		for (int i = 0; i < n; i++) cin >> s[i];
		for (int i = n - 1; i >= 0 && k > 0; i--) {
			int ti = time(i);
			if (ti > t) {
				z++;
			} else {
				res += z;
				k--;
			}
		}
		if (k > 0) cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}