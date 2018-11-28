#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <cmath>
#include <set>

using namespace std;

class node {
public:
	double x;
	double y;
	double r;
	node() { }
	node(double _x, double _y, double _r) : x(_x), y(_y), r(_r) { }
};

double calcDist(double x1, double y1, double x2, double y2) {
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

double solve1(const node& v1) {
	return v1.r;
}

double solve2(const vector<node>& v2, int i = 0, int j = 1) {
	return (calcDist(v2[i].x, v2[i].y, v2[j].x, v2[j].y) + v2[i].r + v2[j].r)/2.0;
}

int main() {
	int C; cin >> C;
	for (int i = 0; i < C; i++) {
		int N; cin >> N;
		double x, y, r;
		vector<node> vec;
		for (int j = 0; j < N; j++) {
			cin >> x >> y >> r;
			node n(x,y,r);
			vec.push_back(n);
		}
		if (N == 1) { 
			cout << "Case #" << (i+1) << ": " << solve1(vec[0]) << "\n";
			continue;
		}
		if (N == 2) {
			double res = solve2(vec);
			res = max(solve1(vec[0]),solve1(vec[1]));
			cout << "Case #" << (i+1) << ": " << res << "\n";
			continue;
		}
		if (N == 3) {
			double res1 = max(solve2(vec,0,1), solve1(vec[2]));
			//cout << "res1: " << res1 << "\n";
			double res2 = max(solve2(vec,1,2), solve1(vec[0]));
			//cout << "res2: " << res2 << "\n";
			double res3 = max(solve2(vec,0,2), solve1(vec[1]));
			//cout << "res3: " << res3 << "\n";
			double tot = min(res1, min(res2, res3));
			cout << "Case #" << (i+1) << ": " << tot << "\n";
			continue;
		}
	}
	return 0;
}