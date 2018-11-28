#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdio.h>

using namespace std;

#define alpha 0.1

vector<long> arms;
vector<long> students;


bool comp (int i, int j) { return (arms[i] > arms[j]);}

bool intersects(double x0, double y0, double r0, double x1, double y1, double r1) {
	return (x0-x1)*(x0-x1)+(y0-y1)*(y0-y1) <= (r0+r1)*(r0+r1);
}

void solve(int tc) {
	long n, w, l; cin >> n >> w >> l;
	arms.clear(); students.clear();

	double x[n]; double y[n];
	
	for (int s = 0; s < n; s++) {
		long al; cin >> al;
		arms.push_back(al);
		students.push_back(s);
	}

	sort(students.begin(), students.end(), comp);

	cout << "Case #" << (tc+1) << ":";

	for (int s = 0; s < n; s++) {
		bool ints = true;
		while(ints) {
			x[students[s]] = ((double)rand()/(double)RAND_MAX) * w;
			y[students[s]] = ((double)rand()/(double)RAND_MAX) * l;
			ints = false;
			for (int ps = 0; ps < s; ps++) {
				if (intersects(x[students[ps]], y[students[ps]], arms[students[ps]], x[students[s]], y[students[s]], arms[students[s]])) {ints = true; break;}
			}
		}
	}

	for (int s = 0; s < n; s++) {
		printf(" %f %f", x[s], y[s]);
	}

	cout << endl;
}

int main() {
    int ntc; cin >> ntc;
	cout.precision(15);

    for (int tc = 0; tc < ntc; tc++) solve(tc);
	return 0;
}
