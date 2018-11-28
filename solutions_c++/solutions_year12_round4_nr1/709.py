#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <deque>
#include <queue>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <ctime>
#include <sstream>
#include <numeric>
#include <functional>
#include <bitset>

using namespace std;

#define all(v) (v).begin(), (v).end()
#define MP make_pair

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = (1 << 31) - 1;
const long long LLINF = (1LL << 63) - 1;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

const int maxN = 1e4 + 10;
//const int maxN = 10;

char dp[maxN][maxN];

bool solve(const vector<int>& l, const vector<int>& d, int dist) {
	int n = l.size();
	for (int i = 0; i <=n ;++i) {
		for (int j = 0; j <= n; ++j) {
			dp[i][j] = 0;
		}
	}
	for (int i = n - 1; i >= 0; --i) {
		vector<int> p(n);
		for (int k = i + 1; k < n; ++k) {
			p[k] = int(p[k - 1]) | int(dp[k][i]);
		}
		for (int j = 0; j < i; ++j) {
			int len = d[i] - d[j];
			if (len > l[j])
				continue;
			len = min(l[i], len);
			if (len + d[i] >= dist) {
				dp[i][j] = 1;
				continue;
			}
			int b = distance(d.begin(), upper_bound(all(d), len + d[i]));
			if (b && p[b - 1]) {
				dp[i][j] = 1;
			}
		}
	}
	return dp[1][0];
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("o.txt", "w", stdout);
	int T;
	cin >> T;
	int sumN = 0;
	for (int tt = 0; tt < T; ++tt) {

		cout << "Case #" << tt + 1 << ": ";
		int n;
		cin >> n;

		cerr << tt << " from " << T << "\n";
		cerr << "n = " << n << "\n";
		sumN += n;
		cerr << "sumN = " << sumN << "\n";
		cerr << 0.001 * clock() << " sec.\n";

		vector<int> d(n+1);
		vector<int> l(n+1);
		d[0]= 0;
		l[0] = 1e9+10;
		for (int i = 1; i < n+1; ++i) {
			scanf("%d%d", &d[i], &l[i]);
		}
		int D;
		cin >> D;
		bool ok = solve(l, d, D);
		if (ok)
			cout << "YES";
		else
			cout << "NO";
		cout << "\n";
	}
	return 0;
}