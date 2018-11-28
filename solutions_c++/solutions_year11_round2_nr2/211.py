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

using namespace std;

#define For(i, a, b) for (int i = (a); i < (b); ++i)
#define Fod(i, a, b) for (int i = (a); i >= (b); --i)
#define Rep(i, a) for (int i = 0; i < (a); ++i)
#define sz(a) ((int)((a).size()))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(a) (a).begin(), (a).end()
#define Sort(a) sort(all(a))

typedef long long ll;
typedef pair <int, int> pii;

bool test(const vector <pii> &a, double d, double t) {
	double left = -1e+15;
	Rep(i, sz(a)) {
		double leftMost = max(left, a[i].X - t);
		if (leftMost - t > a[i].X + 1e-9)
			return false;
		left = leftMost + d * a[i].Y;
		if (left - d - a[i].X > t + 1e-9)
			return false;
	}
	return true;
}

int main(int argc, char ** argv)
{
	if (argc > 1)
		freopen(argv[1], "r", stdin);
	int T;
	scanf("%d", &T);
	Rep(tt, T) {
		printf("Case #%d: ", tt + 1);
		int d, c;
		scanf("%d%d", &c, &d);
		vector <pii> a(c);
		Rep(i, c) {
			scanf("%d%d", &a[i].X, &a[i].Y);
		}
		Sort(a);
		long double low = 0.0, up = 1e+13;
		while (up - low > 1e-7) {
			long double t = (low + up) / 2.0;
			if (test(a, d, t))
				up = t;
			else
				low = t;
		}
		printf("%.6lf\n", (double)up);
	}
	return 0;
}

