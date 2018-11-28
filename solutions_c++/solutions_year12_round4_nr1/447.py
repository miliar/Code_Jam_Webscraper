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

int main() {
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		cerr << "Case #" << cas << "... time = " << clock() << endl;
		int n = nextInt();
		vector<int> pos(n), len(n);
		for (int i = 0; i < n; ++i) {
			pos[i] = nextInt();
			len[i] = nextInt();
		}
		int D = nextInt();
		vector<int> bestLen(n, 0);
		bestLen[0] = pos[0];
		bool res = false;
		for (int i = 0; i < n; ++i) {
			if (D - pos[i] <= bestLen[i]) {
				res = true;
				break;
			}
			for (int j = i + 1; j < n; ++j) {
				if (pos[j] - pos[i] > bestLen[i]) {
					break;
				}
				bestLen[j] = max(bestLen[j], min(len[j], pos[j] - pos[i]));
			}
		}
		printf("Case #%d: %s\n", cas, res ? "YES" : "NO");
	}
	return 0;
}
