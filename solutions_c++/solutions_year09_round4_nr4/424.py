#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

template <class A, class B> void CONV(A& x, B& y) { stringstream s; s << x; s >> y; }
typedef long long LL;
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define FORU(i, a) for (int i = a; ; ++i)
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

double dist(int x1, int y1, int x2, int y2) {
	return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
}

int main() {
	int c;
	cin >> c;
	FOR(i, 0, c) {
		int n;
		cin >> n;
		vector<int> x(n), y(n), r(n);
		FOR(j, 0, n) cin >> x[j] >> y[j] >> r[j];
		double res = INT_MAX;
		//cout << max((double)r[0], dist(x[1], y[1], x[2], y[2])+r[1]+r[2]) << endl;
		if (n == 1) res = r[0];
		else if (n == 2) res = max(r[0], r[1]);
		else {
			res <?= max((double)r[0], (dist(x[1], y[1], x[2], y[2])+r[1]+r[2])/2);
			res <?= max((double)r[1], (dist(x[0], y[0], x[2], y[2])+r[0]+r[2])/2);
 			res <?= max((double)r[2], (dist(x[0], y[0], x[1], y[1])+r[0]+r[1])/2);
		}
 		cout << "Case #" << i+1 << ": " << res << endl;
	}
}
