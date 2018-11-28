//============================================================================
// Name        : ProblemB.cpp
//============================================================================

#include <algorithm>
#include <bitset>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <utility>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

inline void skipNL() {
	string line;
	getline(cin, line);
}

pair<double, double> readAndSolve() {
	double min_t = 0.0, min_d = 0.0;

	int n;
	cin >> n;
	skipNL();
	double sx = 0.0 , sy = 0.0 , sz = 0.0 , vx = 0.0 , vy = 0.0 , vz = 0.0 ;
	for (int i = 0; i < n; i++) {
		double tsx = 0.0, tsy = 0.0, tsz = 0.0, tvx = 0.0, tvy = 0.0, tvz = 0.0 ;
		cin >> tsx >> tsy >> tsz >> tvx >> tvy >> tvz;
		skipNL();
		sx += tsx;
		sy += tsy;
		sz += tsz;
		vx += tvx;
		vy += tvy;
		vz += tvz;
	}
	sx /= (double) n;
	sy /= (double) n;
	sz /= (double) n;
	vx /= (double) n;
	vy /= (double) n;
	vz /= (double) n;

	double vsq = (vx * vx + vy * vy + vz * vz);
	if (vsq < 1e-12) {
		min_t = 0.0;
	} else {
		min_t = - (sx * vx + sy * vy + sz * vz) / vsq;
	}
	if (min_t < 0.0) min_t = 0.0;
	double tsx = sx + vx * min_t;
	double tsy = sy + vy * min_t;
	double tsz = sz + vz * min_t;
	min_d = sqrt(tsx * tsx + tsy * tsy + tsz * tsz);
	return make_pair<double, double>(min_d, min_t);
}

int main(int argc, const char *argv[]) {

	int testCount;
	cin >> testCount;
	skipNL();

	cout.precision(8);

	for (int testNo = 1; testNo <= testCount; testNo++) {
		cout << "Case #" << testNo << ": ";
		pair<double, double> result = readAndSolve();
		cout << result.first << " " << result.second << endl;
	}

	return 0;
}
