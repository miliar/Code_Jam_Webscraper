#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

const int BUF_SIZE = 2111111;
char buf[BUF_SIZE];

string nextString() {
	scanf("%s", buf);
	return buf;
}

struct Point {
	double x, y;
	Point () : x(0), y(0) {}
	Point (double x, double y) : x(x), y(y) {}
	Point operator - (Point op) { return Point(x - op.x, y - op.y); }
	Point operator + (Point op) { return Point(x + op.x, y + op.y); }
	Point operator * (double op) { return Point(x * op, y * op); }
	double operator % (Point op) { return x * op.y - y * op.x; }
	double operator * (Point op) { return x * op.x + y * op.y; }
};

template<class T>
T sqr(T x) {
	return x * x;
}

const double eps = 1e-9;

int cmp(double x, double y) {
	return x - y < -eps ? -1 : x - y > eps ? 1 : 0;
}

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a % b);
}

///////////////////////////////////////////////////////////

bool canExpand(vector<int> P, vector<int> V, double R, int D) {
	const double INF = 1e100;
	double minPos = -INF;
	vector<pair<int, int> > a(P.size());
	for (int i = 0; i < a.size(); ++i) {
		a[i] = make_pair(P[i], V[i]);
	}
	sort(a.begin(), a.end());
	for (int i = 0; i < a.size(); ++i) {
		double lo = max(minPos, a[i].first - R);
		double hi = lo + (double)D * (a[i].second - 1);
		if (hi > a[i].first + R + eps) {
			return false;
		}
		minPos = max(minPos, hi + D);
	}
	return true;
}

int main() {
	//if (false) {
	//	freopen("stdin.txt", "wt", stdout);
	//	int n = 200;
	//	printf("1\n%d 1000000\n", n);
	//	for (int i = 0; i < n; ++i) {
	//		printf("%d 1000000\n", -100000);
	//	}
	//	return 0;
	//}
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		int C = nextInt();
		int D = nextInt();
		vector<int> P(C), V(C);
		for (int i = 0; i < C; ++i) {
			P[i] = nextInt();
			V[i] = nextInt();
		}
		double res = 1e16, dr = 0.5 * res;
		while (dr > 1e-12) {
			if (canExpand(P, V, res, D)) {
				res -= dr;
			} else {
				res += dr;
			}
			dr *= 0.5;
		}
		cerr << cas << endl;
		cout.precision(20);
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}


