/*
 * D.cpp
 *
 *  Created on: 2010-6-5
 *      Author: Allie
 */

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <utility>
#include <complex>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>

using namespace std; 

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;
const double EPS = 1e-9;

int N;
int M;
int PX[5000];
int PY[5000];
int QX[1000];
int QY[1000];
double A[1000];

inline double getArea(double r, double alpha)
{
	return (alpha + sin(2 * M_PI - alpha)) / 2 * r * r;
}

void solve()
{
	for (int i = 0; i < M; ++i) {
		int x0 = QX[i];
		int y0 = QY[i];
		int x1 = PX[0];
		int y1 = PY[0];
		int x2 = PX[1];
		int y2 = PY[1];
		double r1 = hypot(x1 - x0, y1 - y0);
		double r2 = hypot(x2 - x0, y2 - y0);
		double d = hypot(x1 - x2, y1 - y2);
		assert(r1 - r2 < d && d < r1 + r2);
		double alpha1 = acos((r1 * r1 + d * d - r2 * r2) / (2 * d * r1));
		double alpha2 = acos((r2 * r2 + d * d - r1 * r1) / (2 * d * r2));
		A[i] = getArea(r1, alpha1 + alpha1) + getArea(r2, alpha2 + alpha2);
	}
}

int main() 
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++icase) {
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; ++i)
			scanf("%d%d", &PX[i], &PY[i]);
		for (int i = 0; i < M; ++i)
			scanf("%d%d", &QX[i], &QY[i]);
		solve();
		printf("Case #%d:", icase);
		for (int i = 0; i < M; ++i)
			printf(" %.7f", A[i]);
		printf("\n");
	}
	return 0;
}
