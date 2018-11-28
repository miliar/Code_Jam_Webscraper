#include <fstream>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

#define PB push_back
#define SZ(a) ((int)a.size())
#define PI 3.1415926535897932384626433832795

const double eps = 1e-8;

struct point {
	double x, y;
	point() {}
	point(double x, double y) {
		this->x = x;
		this->y = y;
	}
};

class Solver {
	double R;
	double r;
	double g;
	double t;
	double f;
public:
	Solver(double f, double R, double t, double r, double g) {
		this->R = R - t - f;
		this->g = g - 2*f;
		if (this->g < 0)
			this->g = 0;
		this->r = r + f;
		this->t = t;
		this->f = f;
	}
	bool inCircle(double x, double y) {
		return x*x + y*y <= R*R;
	}
	bool segmentIntersect(point p1, point p2, point &p) {
		if (!((inCircle(p1.x, p1.y) ^ inCircle(p2.x, p2.y))))
			return false;
		if (abs(p1.x - p2.x) < eps) {
			p.x = p1.x;
			p.y = sqrt(R*R - p.x*p.x);
		}
		else {
			p.y = p1.y;
			p.x = sqrt(R*R - p.y*p.y);
		}
		return true;
	}
	double squareIntersect(double x, double y) {
		vector <point> square;
		square.PB(point(x, y));
		square.PB(point(x + g, y));
		square.PB(point(x + g, y + g));
		square.PB(point(x, y + g));
		square.PB(square[0]);
		vector <point> figure;
		vector <point> arc;
		for (int i = 0; i < SZ(square) - 1; i++) {
			if (inCircle(square[i].x, square[i].y))
				figure.PB(square[i]);
			point p;
			if (segmentIntersect(square[i], square[i + 1], p)) {
				figure.PB(p);
				arc.PB(p);
			}
		}
		if (SZ(figure) == 0)
			return 0;
		figure.PB(figure[0]);
		double poly = 0;
		for (int i = 0; i < SZ(figure) - 1; i++)
			poly += (figure[i].x * figure[i + 1].y - figure[i + 1].x * figure[i].y) / 2;
		poly = abs(poly);
		double segment = 0;
		if (SZ(arc) == 2) {
			double angle = acos((arc[0].x*arc[1].x + arc[0].y*arc[1].y) / (R*R));
			double sector = angle * R*R / 2;
			double triangle = abs(arc[0].x * arc[1].y - arc[1].x * arc[0].y) / 2;
			segment = sector - triangle;
		}
		return poly + segment;
	}
	double solve() {
		double area = 0;
		double k = ceil(R / (2*r + g)) - 1;
		double x = (2*k + 1)*r + k*g;
		double y = r;
		while (x + eps > 0 && y < R) {
			area += squareIntersect(x, y);
			if (x - 2 * r < 0 || inCircle(x - 2*r, y + g)) {
				y += 2*r + g;
				double l = (x - r) / (2*r + g);
				area += l * g*g;
			}
			else
				x -= 2*r + g;
		}
		double ans = 1 - area*4 / (PI * (R + t + f)*(R + t + f));
		if (ans < 0 && ans + eps > 0)
			ans = 0;
		if (ans > 1 && ans - eps < 1)
			ans = 1;
		if (ans < 0 || ans > 1)
			fout << "ERROR!!!" << endl;
		return ans;
	}
};

int main() {
	int n;
	fin >> n;
	for (int i = 0; i < n; i++) {
		double f, R, t, r, g;
		fin >> f >> R >> t >> r >> g;
		if (t >= R || f >= R || r >= R) {
			fout << "Case #" << (i + 1) << ": " << "INVALID INPUT" << endl;
			cerr << "Case #" << (i + 1) << ": " << "INVALID INPUT" << endl;
			continue;
		}
		Solver solver(f, R, t, r, g);
		fout.precision(8);
		fout << "Case #" << (i + 1) << ": " << fixed << solver.solve() << endl;
		cerr << "Case #" << (i + 1) << ": " << fixed << solver.solve() << endl;
	}
	return 0;
}