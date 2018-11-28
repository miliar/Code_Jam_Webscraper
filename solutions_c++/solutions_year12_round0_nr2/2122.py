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
	double lengt() { return sqrt(length2()); }
};

Point nextPoint() {
	double x = nextDouble();
	double y = nextDouble();
	return Point(x, y);
}

typedef vector<vector<int> > Adj;

const int INF = INT_MAX / 2;
const int N = 100;

struct Score {
	int s1, s2, s3;
	int total;
	bool isSurprising;
	Score (int s1, int s2, int s3, bool isSurprising)
		: s1(s1),
		s2(s2),
		s3(s3),
		total(s1 + s2 + s3),
		isSurprising(isSurprising)
	{
	}
	bool isGood(int p) {
		return s1 >= p || s2 >= p || s3 >= p;
	}
};
vector<Score> scores;

int _n;
int _p;
vector<int> _t;
int _dp[N][N + 1];

int solve(int at, int s) {
	if (at == _t.size()) {
		return s == 0 ? 0 : -INF;
	}
	int &res = _dp[at][s];
	if (res != -1) {
		return res;
	}
	res = -INF;
	for (int i = 0; i < scores.size(); ++i) {
		if (scores[i].total == _t[at]) {
			if (scores[i].isSurprising) {
				if (s >= 1) {
					int am = solve(at + 1, s - 1);
					if (am != -INF) {
						res = max(res, am + scores[i].isGood(_p));
					}
				}
			} else {
				int am = solve(at + 1, s);
				if (am != -INF) {
					res = max(res, am + scores[i].isGood(_p));
				}
			}
		}
	}
	return res;
}

int main() {
	for (int i = 0; i <= 10; ++i) {
		for (int j = 0; j <= 10; ++j) {
			for (int k = 0; k <= 10; ++k) {
				int mx = max(i, max(j, k));
				int mn = min(i, min(j, k));
				if (mx - mn > 2) {
					continue;
				}
				scores.push_back(Score(i, j, k, mx - mn == 2));
			}
		}
	}
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		_n = nextInt();
		int s = nextInt();
		_p = nextInt();
		_t = vector<int>(_n);
		for (int i = 0; i < _t.size(); ++i) {
			_t[i] = nextInt();
		}
		memset(_dp, -1, sizeof(_dp));
		int res = solve(0, s);
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}