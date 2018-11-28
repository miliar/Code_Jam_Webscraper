#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;

const double pi = acos(-1.0);
const int inf = numeric_limits<int>::max();

#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

struct interval {
	double runTime, walkTime, dist;
	interval() {}
	interval(double runTime, double walkTime, double dist) : runTime(runTime), walkTime(walkTime), dist(dist) {}
	bool operator < (const interval &i) const {
		return (walkTime - runTime) / dist > (i.walkTime - i.runTime) / i.dist;
	}
};

void solve() {
	int x, s, r, n; double t; cin >> x >> s >> r >> t >> n;
	
	vector<interval> time; time.reserve(1000);
	int totLen = 0;
	for(int i = 0; i < n; i++) {
		double a, b, w; cin >> a >> b >> w;
		time.push_back(interval((b - a) / (w + r), (b - a) / (w + s), b - a));
		totLen += b - a;
	}
	
	if(totLen < x) {
		time.push_back(interval((1.0 * x - totLen) / r, (1.0 * x - totLen) / s, x - totLen));
		n++;
	}
	
	sort(time.begin(), time.end());
	
//	for(int i = 0; i < n; i++)
//		cout << time[i].runTime << ' ' << time[i].walkTime << ' ' << time[i].dist << endl;
	
	double minTime = 0;
	for(int i = 0; i < n; i++) {
		if(t > 0) {
			if(t >= time[i].runTime) {
				minTime += time[i].runTime;
				t -= time[i].runTime;
			} else {
				minTime += t + (1 - t / time[i].runTime) * time[i].walkTime;
				t = 0;
			}
		} else {
			minTime += time[i].walkTime;
		}
	}

	//for(int i = 0; i < x; i++)
	//	cout << time[i].first << ' ' << time[i].second << endl;
	cout << fixed;
	cout << setprecision(10) << minTime << endl;
}

int main ( )
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t; cin >> t;
	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}