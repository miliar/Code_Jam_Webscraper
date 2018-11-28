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
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define ALL(a) (a).begin(),(a).end()
#define PB(a) push_back(a)
#define MP(a,b) make_pair((a),(b))
#define sqr(a) ((a)*(a))
typedef long long i64;
typedef unsigned long long u64;

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

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf);
	return buf;
}

const int N = 511;

long long getSum(long long SUM[N][N], int x, int y) {
	if (x < 0 || y < 0) {
		return 0;
	}
	return SUM[x][y];
}

long long getSum(long long SUM[N][N], long long VAL[N][N], int x1, int y1, int x2, int y2) {
	long long res = getSum(SUM, x2, y2) - getSum(SUM, x1 - 1, y2) - getSum(SUM, x2, y1 - 1) + getSum(SUM, x1 - 1, y1 - 1);
	res -= VAL[x1][y1] + VAL[x1][y2] + VAL[x2][y1] + VAL[x2][y2];
	return res;
}

long long SUM[N][N], XSUM[N][N], YSUM[N][N];
long long VAL[N][N], XVAL[N][N], YVAL[N][N];


int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		double X = nextDouble();
		double S = nextDouble();
		double R = nextDouble();
		double t = nextDouble();
		int N = nextInt();
		double rem = X;
		vector<pair<double, double> > segs;
		for (int i = 0; i < N; ++i) {
			double b = nextDouble();
			double e = nextDouble();
			double w = nextDouble();
			segs.push_back(make_pair(S + w, e - b));
			rem -= e - b;
		}
		segs.push_back(make_pair(S, rem));
		vector<pair<double, double> > runs;
		while (t > 0 && segs.size() > 0) {
			sort(segs.begin(), segs.end());
			double runSpeed = segs[0].first - S + R;
			double runTime = segs[0].second / runSpeed;
			if (runTime >= t - 1e-9) {
				runs.push_back(make_pair(runSpeed, runSpeed * t));
				segs[0].second -= runSpeed * t;
				t = 0;
			} else {
				runs.push_back(make_pair(runSpeed, segs[0].second));
				segs.erase(segs.begin());
				t -= runTime;
			}
		}
		double totalTime = 0;
		for (int i = 0; i < segs.size(); ++i) {
			totalTime += segs[i].second / segs[i].first;
		}
		for (int i = 0; i < runs.size(); ++i) {
			totalTime += runs[i].second / runs[i].first;
		}
		cerr << cas << endl;
		printf("Case #%d: %.15lf\n", cas, totalTime);
	}
	return 0;
}
