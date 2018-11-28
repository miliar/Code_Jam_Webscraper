#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

const int N = 128;
const double eps = 1e-19;
int x[N];
int y[N];
int r[N];

double best(int i, int j) {	
	double dist = hypot(x[i] - x[j], y[i] - y[j]);
	double r1 = r[i];
	double r2 = r[j];
	if (dist + r1 < r2 - eps)
		return r2;
	if (dist + r2 < r1 - eps)
		return r1;
	return 0.5 * (dist + r1 + r2);
}

double solve() {
	int n;
	scanf("%d", &n);
	if (n > 3)
		return -1;
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &x[i], &y[i], &r[i]);
	}
	if (n == 1)
		return r[0];
	if (n == 2)
		return max(r[0], r[1]);
	double res = max(best(0, 1), (double)r[2]);
	res = min(res, max(best(0, 2), (double)r[1]));
	res = min(res, max(best(1, 2), (double)r[0]));
	return res;
}

int main () {
	freopen("d.in", "r", stdin); freopen("d.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %.15lf\n", T, solve());
	fclose(stdin); fclose(stdout);
	return 0;
}
