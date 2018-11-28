#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct Point {
	Point():x(0),y(0) {}
	Point(long long a, long long b):x(a),y(b) {}
	long long x, y;
};

int main(int argc, char **argv) {
	int numCases;
	cin >> numCases;

	for (int curCase = 0; curCase < numCases; curCase++) {
		vector<Point> points;

		int numChecked = 0;
		int numTriangles = 0;
		long long n, A, B, C, D, x0, y0, M;
		long long x, y;

		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		x = x0;
		y = y0;
		points.push_back(Point(x, y));
		for (int i = 1; i < n; i++) {
			x = (A * x + B) % M;
			y = (C * y + D) % M;
			points.push_back(Point(x, y));
		}

		for (int a = 0; a < points.size(); a++) {
			for (int b = a + 1; b < points.size(); b++) {
				for (int c = b + 1; c < points.size(); c++) {
					long long cx = points[a].x + points[b].x + points[c].x;
					long long cy = points[a].y + points[b].y + points[c].y;

					if ((cx % 3 == 0) && (cy % 3 == 0)) {
						numTriangles++;
					}
				}
			}
		}

		cout << "Case #" << curCase + 1 << ": " << numTriangles << endl;
	}
}
