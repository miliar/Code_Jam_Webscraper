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

vector<int> p10;

int shift(int x, int s, int len) {
	return x / p10[s] + x % p10[s] * p10[len - s];
}

int main() {
	p10.resize(20);
	p10[0] = 1;
	for (int i = 1; i < p10.size(); ++i) {
		p10[i] = p10[i - 1] * 10;
	}
	vector<int> group(2000001, -1);
	int gCount = 0;
	for (int len = 1; len <= 7; ++len) {
		cerr << "len = " << len << endl;
		for (int i = p10[len - 1]; i < p10[len] && i < group.size(); ++i) {
			if (group[i] != -1) {
				continue;
			}
			for (int j = 0; j < len; ++j) {
				int x = shift(i, j, len);
				if (p10[len - 1] <= x && x < group.size()) {
					group[x] = gCount;
				}
			}
			++gCount;
		}
	}
	cerr << "gCount = " << gCount << endl;
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		int a = nextInt();
		int b = nextInt();
		vector<int> cnt(gCount, 0);
		for (int i = a; i <= b; ++i) {
			++cnt[group[i]];
		}
		long long res = 0;
		for (int i = 0; i < cnt.size(); ++i) {
			res += (long long)cnt[i] * (cnt[i] - 1) / 2;
		}
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}