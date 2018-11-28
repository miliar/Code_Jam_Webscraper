#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
#include <ctime>
using namespace std;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

long long nextLong() {
	long long x;
	scanf("%I64d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf);
	return buf;
}
string nextLine() {
	gets(buf);
	return buf;
}

int stringToInt(string s) {
	stringstream in(s);
	int x;
	in >> x;
	return x;
}

struct Point {
	typedef double T;
	T x, y;
	Point () : x(0), y(0) {}
	Point (T x, T y) : x(x), y(y) {}
	Point operator - (Point op) const { return Point(x - op.x, y - op.y); }
	Point operator + (Point op) const { return Point(x + op.x, y + op.y); }
	Point operator * (T op) const { return Point(x * op, y * op); }
	T operator * (Point op) const { return x * op.x + y * op.y; }
	T operator % (Point op) const { return x * op.y - y * op.x; }
	T length2() { return x * x + y * y; }
	double length() { return sqrt(length2()); }
};

Point nextPoint() {
	double x = nextDouble();
	double y = nextDouble();
	return Point(x, y);
}

typedef vector<vector<int> > Adj;

struct Square {
	int x, y, r;
	Square(int x, int y, int r) : x(x), y(y), r(r) {}
};

vector<Square> s;

void putSquare(int x, int y, int r) {
	s.push_back(Square(x, y, r));
}

bool intersect(int a, int b, int x, int y) {
	int p = max(a, x);
	int q = min(b, y);
	return p < q;
}

int getMinY(int x, int r) {
	int lo = x - r, hi = x + r;
	int res = 0;
	for (int i = 0; i < s.size(); ++i) {
		int from = s[i].x - s[i].r;
		int to = s[i].x + s[i].r;
		if (intersect(from, to, lo, hi)) {
			res = max(res, s[i].y + s[i].r + r);
		}
	}
	return res;
}

int main() {
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		cerr << "Case #" << cas << "... time = " << clock() << endl;
		int n = nextInt();
		int w = nextInt();
		int len = nextInt();
		vector<int> r(n);
		for (int i = 0; i < n; ++i) {
			r[i] = nextInt();
		}
		vector<pair<int, int> > p(n);
		for (int i = 0; i < n; ++i) {
			p[i] = make_pair(r[i], i);
		}
		s.clear();
		sort(p.begin(), p.end());
		vector<pair<int, int> > res(n);
		for (int i = 0; i < p.size(); ++i) {
			int lo = 0;
			int hi = w;
			while (lo <= hi) {
				int mid = (lo + hi) / 2;
				int y = getMinY(mid, p[i].first);
				if (y <= len) {
					hi = mid - 1;
				} else {
					lo = mid + 1;
				}
			}
			int x = lo;
			int y = getMinY(x, p[i].first);
			res[p[i].second] = make_pair(x, y);
			putSquare(x, y, p[i].first);
		}
		printf("Case #%d:", cas);
		for (int i = 0; i < res.size(); ++i) {
			printf(" %d %d", res[i].first, res[i].second);
		}
		printf("\n");
	}
	return 0;
}
