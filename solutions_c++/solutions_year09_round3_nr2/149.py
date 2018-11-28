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

void solve() {
	int n;
	scanf("%d", &n);
	double x = 0, y = 0, z = 0;
	double vx = 0, vy = 0, vz = 0;
	for (int i = 0; i < n; i++) {
		int cx, cy, cz, cvx, cvy, cvz;
		scanf("%d%d%d%d%d%d", &cx, &cy, &cz, &cvx, &cvy, &cvz);		
		x += cx;
		y += cy;
		z += cz;
		vx += cvx;
		vy += cvy;
		vz += cvz;
	}
	x /= n;
	y /= n;
	z /= n;
	vx /= n;
	vy /= n;
	vz /= n;
	
	double A = vx * vx + vy * vy + vz * vz;
	double B = x * vx + y * vy + z * vz;
	double C = x * x + y * y + z * z;
	double dmin, tmin;
	if (A == 0) {
		tmin = 0;
		dmin = sqrtl(C);
	}
	else  {
		tmin = -B / A;
		if (tmin < 0)
			tmin = 0;
		dmin = A * tmin * tmin + 2 * B * tmin + C;
		dmin = sqrtl(dmin);
	}
	printf("%.15lf %.15lf\n", dmin, tmin);
}

int main () {
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++) {
		printf("Case #%d: ", T);
		solve();
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
