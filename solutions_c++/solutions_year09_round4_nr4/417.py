#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

struct Point {
	double X, Y, R;
};

double Dist(Point a, Point b) {
	double dX = a.X - b.X;
	double dY = a.Y - b.Y;
	return sqrt(dX * dX + dY * dY);
}

void Solve() {
	int N;
	cin >> N;
	vector<Point> points;
	for(int i = 0; i < N; ++i) {
		Point p;
		cin >> p.X >> p.Y >> p.R;
		points.push_back(p);
	}
	if (N == 1) {
		cout << points[0].R << endl;
		return;
	}
	if (N == 2) {
		cout << max(points[0].R, points[1].R) << endl;
		return;
	}
	double Answer = 1000000000;
	for(int i = 0; i < 3; ++i) {
		int p1 = i;
		int p2 = (i + 1) % 3;
		int p3 = 3 - p1 - p2;
		Answer = min(Answer,
				max(points[p1].R + points[p2].R + Dist(points[p1], points[p2]),
						points[p3].R * 2));
		
	}
	cout << Answer / 2 << endl;
}

void Init() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		Solve();
	}
}

int main() {
	Init();
	return 0;
}
