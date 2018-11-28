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

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		long long n, pd, pg;
		cin >> n >> pd >> pg;
		bool res = false;
		int d = 100 / gcd(100, pd);
		int wd = d * pd / 100;
		if (d <= n) {
			int x = 100 / gcd(100, pg);
			int y = x * pg / 100;
			if (y != 0 || wd == 0) {
				if (x != y || d == wd) {
					res = true;
					//cerr << wd << " " << d << " " << (0.01 * pd - (double)wd / d) << endl;
					//cout << wd << " " << d << endl;
				}
			}
		}
		cout << "Case #" << cas << ": " << (res ? "Possible" : "Broken") << endl;
	}
	return 0;
}


