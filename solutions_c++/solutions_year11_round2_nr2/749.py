#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <stack>
#include <string>
#include <cctype>
using namespace std;

#define sz(a) int((a).size())
#define dump(a) cerr << #a << " = " << a << endl
#define rep(i, b, e) for((i) = (b); (i) < (e); ++(i))

double dabs(double a) {
	return (a < 0)? -a : a;
}

typedef unsigned long long ull;
typedef long long ll;
const int INF = 10000000;
const double EPS = 10e-10;
vector <double> m;
double d;

bool check(double gt) {
	double prev = -INF, x;
	for (int i = 0; i < sz(m); ++i) {
		if (prev + d <= m[i]) 
		{ // Go to left
			x = m[i] - gt;
			if (x < prev + d) x = prev + d;
		} else {
			x = m[i] + gt;
			if (x > prev + d) x = prev + d;
			if (x < prev + d) return false;
		}
		prev = x;
	}
	return true;
}

int main()
{
	int tests, test;
	cin >> tests;
	cout.setf(ios::fixed);
	cout.precision(13);
	rep(test, 1, tests + 1) {
		int c, i, j;
		cin >> c >> d;
		m.clear();
		rep(i, 0, c) {
			int p, v;
			cin >> p >> v;
			rep(j, 0, v)
				m.push_back(p);
		}
		sort(m.begin(), m.end());
		double l = 0, r = 10e18;
		while (dabs(l - r) > EPS) {
			double m = (l + r) / 2;
			if (check(m))
				r = m;
			else
				l = m;
		}
		cout << "Case #" << test << ": " << l << endl;
	}
	return 0;
}
