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

double getWP(vector<string> &a, int i, int ex) {
	int total = 0;
	int wins = 0;
	int n = a.size();
	for (int j = 0; j < n; ++j) {
		if (j != ex && a[i][j] != '.') {
			++total;
			wins += a[i][j] == '1';
		}
	}
	double res = wins;
	if (total > 0) {
		res /= total;
	}
	return res;
}

double getOWP(vector<string> &a, vector<vector<double> > &wp, int i, int ex) {
	double sum = 0;
	int cnt = 0;
	int n = a.size();
	for (int j = 0; j < n; ++j) {
		if (j != ex && a[i][j] != '.') {
			++cnt;
			sum += wp[j][i];
		}
	}
	return sum / cnt;
}

double getOOWP(vector<string> &a, vector<vector<double> > &owp, int i) {
	double sum = 0;
	int cnt = 0;
	int n = a.size();
	for (int j = 0; j < n; ++j) {
		if (a[i][j] != '.') {
			++cnt;
			sum += owp[j][n];
		}
	}
	return sum / cnt;
}


int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		int n = nextInt();
		vector<string> a(n);
		for (int i = 0; i < a.size(); ++i) {
			a[i] = nextString();
		}
		vector<vector<double> > wp(n, vector<double>(n + 1));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < wp[i].size(); ++j) {
				wp[i][j] = getWP(a, i, j);
			}
		}
		/*for (int i = 0; i < n; ++i) {
			cerr << "wp[" << i << "] = " << wp[i] << endl;
		}*/
		vector<vector<double> > owp(n, vector<double>(n + 1));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < wp[i].size(); ++j) {
				owp[i][j] = getOWP(a, wp, i, j);
			}
		}
		//for (int i = 0; i < n; ++i) {
		//	cerr << "owp[" << i << "] = " << owp[i] << endl;
		//}
		vector<double> oowp(n);
		for (int i = 0; i < n; ++i) {
			oowp[i] = getOOWP(a, owp, i);
		}
		vector<double> rpi(n);
		for (int i = 0; i < n; ++i) {
			rpi[i] = 0.25 * wp[i][n] + 0.5 * owp[i][n] + 0.25 * oowp[i];
		}
		cout.precision(20);
		cerr << cas << endl;
		cout << "Case #" << cas << ":" << endl;
		for (int i = 0; i < n; ++i) {
			cout << rpi[i] << endl;
		}
	}
	return 0;
}


