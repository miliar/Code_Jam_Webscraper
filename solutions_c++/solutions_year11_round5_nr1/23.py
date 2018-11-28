#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int W, L, U, G;
struct s_dot {
	double x, y;
} low[200], up[200];

double area(double x) {
	double res = 0.0;
	REP(i, U-1) {
		if (up[i].x > x) break;
		double xleft = up[i].x;
		double xright = up[i+1].x;
		double yleft = up[i].y;
		double yright = up[i+1].y;
		if (xright > x) {
			yright = yleft + (yright-yleft)*(x-xleft)/(xright-xleft);
			xright = x;
		}
		res += (yleft + yright) * (xright - xleft) / 2.0;
	}
	REP(i, L-1) {
		if (low[i].x > x) break;
		double xleft = low[i].x;
		double xright = low[i+1].x;
		double yleft = low[i].y;
		double yright = low[i+1].y;
		if (xright > x) {
			yright = yleft + (yright-yleft)*(x-xleft)/(xright-xleft);
			xright = x;
		}
		res -= (yleft + yright) * (xright - xleft) / 2.0;
	}
	return res;
}

int main() {
	int casos, res;
	cin >> casos;
	REP(caso, casos) {
		cin >> W >> L >> U >> G;
		REP(i, L) cin >> low[i].x >> low[i].y;
		REP(j, U) cin >> up[j].x >> up[j].y;
		cout << "Case #" << caso+1 << ":" << endl;
		double total = area(W);
		REP(i, G-1) {
			double target = (total*(i+1))/G;
			double l = 0.0, r = W;
			while (r-l > 1e-8) {
				double m = (l+r)/2;
				if (area(m) < target) {
					l = m;
				} else {
					r = m;
				}
			}
			cout << fixed << setprecision(6) << l << endl;
		}
	}
	return 0;
}
