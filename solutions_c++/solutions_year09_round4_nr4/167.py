#include <iostream>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <list>
#include <map>
#include <cmath>

#include <memory.h>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define FORE(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FIR(k) FOR(i,0,k)
#define FJR(k) FOR(j,0,k)
#define FI FIR(n)
#define FJ FJR(n)
#define ALL(v) v.begin(), v.end()
#define LL long long

typedef vector<int> VI;
typedef pair<int, int> PI;

int X[10], Y[10], R[10];

double solve(int n) {
	if (n == 1) return R[0];
	if (n == 2) return max(R[0], R[1]);

	double res = 1e100;
	for (int i = 0; i < 3; ++i)
		for (int j = i+1; j < 3; ++j) {
			double dist = hypot(X[i] - X[j], Y[i] - Y[j]);
			double r = (dist + R[i] + R[j])/2.0;

			res = min(res, max(r, (double)R[3-i-j]));
		}

		return res;
}


int main() {
static const string FILENAME = "D-small-attempt0";
freopen((FILENAME + ".in").c_str(), "rt", stdin);
freopen((FILENAME + ".out").c_str(), "w", stdout);	
	
	int ncase; cin >> ncase;
	FORE(caze, 1, ncase) {
		int n;cin >> n;
		FI cin >> X[i] >> Y[i] >> R[i];
		double res = solve(n);

		printf("Case #%d: %.7lf\n", caze, res);
	}

}