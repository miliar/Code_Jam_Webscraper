#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <string>
#include <boost/random.hpp>
#include <boost/random/uniform_int.hpp>

using namespace std;

ifstream fin;
ofstream fout;

int main() {
	fin.open("/home/chris/Download/B-small-attempt6.in");
	cout.precision(9);
	fout.precision(9);
	fout.open("/home/chris/Desktop/results.txt");

	int T;
	double N;
	fin >> T;
	double x,y,z,vx,vy,vz;
	double x2,y2,z2,vx2,vy2,vz2;
	for (int i = 0; i < T; i++) {
		fin >> N;
		x2 = 0;
		y2 = 0;
		z2 = 0;
		vx2 = 0;
		vy2 = 0;
		vz2 = 0;

		for (int j = 0; j < N; j++) {
			fin >> x >> y >> z >> vx >> vy >> vz;
			cout << x << " " << y << " " << z << endl;
			x2 += x;
			y2 += y;
			z2 += z;
			vx2 += vx;
			vy2 += vy;
			vz2 += vz;
		}
		x2 = x2;
		y2 = y2;
		z2 = z2;
		
		double rmin = sqrt(pow(x2,2) + pow(y2,2) + pow(z2,2));
		double r = rmin + 1;
		double timestep = 1;
		double tolerance = pow(10,-5);
		x = x2 + vx2;
		y = y2 + vy2;
		z = z2 + vz2;
		
		cout << vx2 << " " << vy2 << " " << vz2 << endl;

		double t,d;
		
		if ((vx2 != 0) || (vy2 != 0) || (vz2 != 0)) {
			t = - ((x2 * (x - x2)) + (y2 * (y - y2)) + (z2 * (z - z2)))/(pow(x - x2,2) + pow(y - y2,2) + pow(z - z2,2));
			d = sqrt(pow((x2 + vx2 * t)/N,2) + pow((y2 + vy2 * t)/N,2) + pow((z2 + vz2 * t)/N,2));
		}
		else {
			t = 0;
			d = rmin/N;
		}
		if (t < 0) {
			t = 0;
			d = rmin/N;
		}
		cout << "t = " << t << " " << "d = " << d << endl;
		fout << "Case #" << i + 1<< ": " << d << " " << t << endl;
	}
	fout.close();
	cout << "Done!" << endl;
	return 0;
}
		
		
		
