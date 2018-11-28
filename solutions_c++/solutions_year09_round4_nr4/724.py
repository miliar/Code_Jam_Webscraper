#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <list>
#include <cmath>

using namespace std;

struct Circle {
	int x, y;
	int radius;

	double minDist(Circle& c)
	{
		double dx = x - c.x;
		double dy = y - c.y;
		return sqrt(dx*dx + dy*dy) + double(radius + c.radius);
	}
};

typedef vector<Circle> Circles;

void processCase(int lineN, istream& in, ostream& out)
{
	int n;
	in >> n;

	Circles circles(n, Circle());
	for (int i=0; i<n; i++) {
		in >> circles[i].x >> circles[i].y >> circles[i].radius;
	}

	double result = 0;

	if (n == 3) {
		list<double> dists;
		for (int i=0; i<n; i++) {
			dists.push_back(circles[i].minDist(circles[(i+1)%n]));
		}
		dists.sort();
		result = dists.front() / 2.0;
	} else if (n == 2) {
		double r1 = circles[0].radius;
		double r2 = circles[1].radius;
		result = r1 > r2 ? r1 : r2;
	} else if (n == 1) {
		result = circles[0].radius;
	}

	// Print result
	out << "Case #" << lineN << ": ";
	out << result;
	out << endl;
}

int main()
{
	ifstream in("D-small-attempt1.in");
	//ostream& out = cout;
	ofstream out("D-small-attempt1.out", std::ios_base::out | std::ios_base::binary);

	out.precision(6);
	out.setf(ios::fixed,ios::floatfield);

	int nCases;
	in >> nCases;
	for (int i=0; i<nCases; i++) {
		processCase(i+1, in, out);
	}

	out.flush();
}
