#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)

using namespace std;

const int INF = 1000000000;

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		int n, o = 1, b = 1, u = 0, v = 0, ans = 0;
		vector< pair< int, int > > O, B;
		cin >> n;
		for (int i = 0; i < n; i++) {
			char r;
			int x;
			cin >> r >> x;
			if (r == 'O')
				O.push_back(make(x, i));
			else
				B.push_back(make(x, i));
		}
		O.push_back(make(INF, INF));
		B.push_back(make(INF, INF));
		for (int i = 0; i < n; i++) {
			if (O[u].second < B[v].second) {
				int x = O[u].first, y = B[v].first, m = abs(o - x) + 1;
				o = x;
				if (b < y)
					b = min(y, b + m);
				else
					b = max(y, b - m);
				ans += m;
				++u;
			}
			else {
				int y = O[u].first, x = B[v].first, m = abs(b - x) + 1;
				b = x;
				if (o < y)
					o = min(y, o + m);
				else
					o = max(y, o - m);
				ans += m;
				++v;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

