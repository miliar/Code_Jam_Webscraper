#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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

double dist(double x0, double x1, double y0, double y1) {
	return sqrt( (x0-x1)*(x0-x1) + (y0-y1)*(y0-y1) );
}

#define X 0
#define Y 1
const double EPS=1e-9;
const int MAX=100;
double A[MAX][2];
double R[MAX];
double D[MAX][MAX];
int N;

double solve1(int i) {
	return R[i];
}

double solve2(int i, int j) {
	double ret =  (D[i][j] + R[i] + R[j])/2;
	return ret;
}

double solve() {
	if (N==1) return solve1(0);
	if (N==2) {
		return max(R[0],R[1]);
	}

	if (N==3) {
		double opt1 = max(solve2(0,1), solve1(2));
		double opt2 = max(solve2(0,2), solve1(1));
		double opt3 = max(solve2(1,2), solve1(0));
		return min(opt1, min(opt2, opt3));
	}
	return -1;
}


int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		cin >> N;
		for (int i=0;i<N;++i) {
			cin >> A[i][X] >> A[i][Y] >> R[i];
		}
		for (int i=0;i<N;++i) {
			for (int j=0;j<N;++j) {
				D[i][j] = dist(A[i][X], A[j][X], A[i][Y], A[j][Y]);
			}
		}
		printf("Case #%d: %.10lf\n", z, solve());
	}
}
