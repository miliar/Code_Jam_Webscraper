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

const int OPEN = 0;
const int SELF = 1;
const int CLOSE = 2;

typedef pair<double, double> pdd;

double randDouble(int B) {
	double b = B;
	ll r = 0;
	for (int i = 0; i < 4; ++i) {
		r = (r << 15) + rand();
	}
	ll max1 = (1Ll << 60) - 1;
	return min(b, max(0.0, b * r / max1));
}

inline double sqr(double x) {
	return x * x;
}

inline double dist2(const pdd& A, const pdd& B) {
	return sqr(A.first - B.first) + sqr(A.second - B.second);
}

vector<pdd> solve(int L, int W, const vector<int>& r) {
	int n = r.size();
	vector<pdd> res;
	for (int i = 0; i < n; ++i) {
		bool ok = 0;
		int inters = 0;
		while(!ok) {
			++inters;
			if (inters > 10) {
				cerr << "iters more then ten  " << inters << "\n";
			}
			double x = randDouble(W);
			double y = randDouble(L);
			ok = x >= 0.0 && y >= 0 && x <= W && y <= L;
			for (int j = 0; j < i; ++j) {
				double d = r[i] + r[j];
				if (dist2(res[j], MP(x,y)) < 1.0 * d * d)
					ok = false;
			}
			if (ok)
				res.push_back(MP(x,y));
		}
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int tt = 0; tt < T; ++tt) {
		int n;
		int W;
		int L;
		cin >> n >> W >> L;
		vector<int> r(n);
		cout << "Case #" << tt + 1 << ": ";
		for (int i =0 ; i < n; ++i ){
			scanf("%d", &r[i]);
		}
		vector<pdd> s = solve(L, W, r);
		for (int i = 0; i < n; ++i) {
			printf("%0.18lf ", s[i].first);
			printf("%0.18lf ", s[i].second);
		}
		cout << "\n";
	}
	return 0;
}