#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int C;

int N;

fstream in, out;

double xpos[100];
double ypos[100];
double radius[100];

double dist(int i, int j) {
	return sqrt((xpos[i] - xpos[j])*(xpos[i] - xpos[j]) + (ypos[i] - ypos[j])*(ypos[i] - ypos[j]));
}

double max(double x, double y) {
	if (x > y) {
		return x;
	}
	return y;
}

double min(double x, double y) {
	if (x < y) {
		return x;
	}
	return y;
}


int main() {
	in.open("prob4.in", fstream::in);
	out.open("prob4.out", fstream::out);
	out.precision(10);
	in >> C;

    for (int i = 0; i < C; i++) {
		in >> N;

		for (int j = 0; j < N; j++) {
			in >> xpos[j] >> ypos[j] >> radius[j];
		}
		
		double ans = 0;
		if (N <= 2) {
			for (int ii = 0; ii < N; ii++) {
				if (radius[ii] > ans) {
					ans = radius[ii];
				}
			}
		} else if (N == 3) {
			double test[4];
			test[2] = max((dist(0, 1) + radius[0] + radius[1])/2.0, radius[2]);
			test[0] = max((dist(1, 2) + radius[1] + radius[2])/2.0, radius[0]);
			test[1] = max((dist(2, 0) + radius[2] + radius[0])/2.0, radius[1]);
			ans = min(test[0], min(test[1], test[2]));
		}

		out << "Case #" << i + 1 << ": " << ans << endl;
    }
    
	in.close();
	out.close();

	return 0;
}
