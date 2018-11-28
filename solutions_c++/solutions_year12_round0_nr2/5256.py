#include <iostream>
#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <utility>
#include <cmath>
#include <cctype>
#include <sstream>
#include <ctime>
#include <numeric>
#include <functional>
#include <string.h>

#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <bitset>
#include <string>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define x_p first
#define y_p second
#define sqr(a) ((a) * (a))

using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("bstsimple.in", "rt", stdin);
	freopen("bstsimple.out", "wt", stdout);
#endif	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		int s, n, p, a, temp, ans = 0;
		cin >> n >> s >> p;
		for (int i = 0; i < n; i++) {
			cin >> a;
			temp = (a / 3) + (a % 3? 1 : 0);
			if (temp >= p) {
				ans++;
			} else if (a >= 2 && temp == p - 1 && s > 0) {
				s--;
				ans++;
			}
		}
		cout << "Case #" << tt + 1 << ": " << ans << '\n';
	}
	return 0;
}
