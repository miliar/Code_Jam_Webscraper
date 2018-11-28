#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <utility>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <bitset>
#include <list>
#include <map>
#include <valarray>
#include <numeric>
#include <cmath>
#include <complex>
#include <ctime>
#include <cassert>
#include <exception>
#include <climits>
#include <limits>
//#include <hash_map>
//#include "regex.h"

#define foreach(container, iterator) for ((iterator) = (container).begin(); (iterator) != (container).end(); ++(iterator))
#define foreachr(container, riterator) for ((riterator) = (container).rbegin(); (riterator) != (container).rend(); ++(riterator))
#define ALL(container) (container).begin(), (container).end()
#define SQR(x) ((x) * (x))

#define SIZE(x) (sizeof(x) / sizeof((x)[0]))
#define CLEAR(x, pat) memset(x, pat, sizeof(x))

#define PB push_back 
#define MP std::make_pair

#define X first
#define Y second

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

#define REP(i, n) for ((i) = 0; (i) < (n); ++(i)) 
#define FOR(i, l, h) for ((i) = (l); (i) <= (h); ++(i)) 
#define FORD(i, h, l) for ((i) = (h); (i) >= (l); --(i)) 
#define PRESENT(container, element) ((container).find(element) != (container).end())
#define CPRESENT(container, element) (find(ALL(container), (element)) != (container).end())

const double eps = 1e-9;
inline bool eq(double x, double y) {
	return std::abs(x - y) < eps;
}

inline bool eq_rel(double p1, double p2) {
    return std::abs(p1 - p2) < eps * std::min(std::abs(p1), std::abs(p2));
}

typedef double real;
typedef unsigned long ulong;
typedef unsigned int uint;

typedef long long i64;
typedef unsigned long long u64;
const u64 MOD64 = 1000000007LL;

typedef std::vector<i64> VI64;
typedef std::vector<u64> VU64;

typedef std::vector<int> VI;
typedef std::vector<uint> VU;
typedef std::vector<real> VR;
typedef std::vector<std::string> VS;
typedef std::deque<bool> DB;
typedef std::pair<int, int> PII;
typedef std::pair<long, long> PLL;

#define FILE_NAME "B-large"

int main(int argc, char *argv[]) {
#ifdef FILE_NAME
	std::ifstream fin(FILE_NAME ".in");
	std::ofstream fout(FILE_NAME ".out");
#else
#define fin (std::cin)
#define fout (std::cout)
#endif
	
	assert(fin && fout);

	int testCnt;
	fin >> testCnt;

	for (int testIdx = 1; testIdx <= testCnt; ++testIdx) {
		int n;
		fin >> n;

		std::valarray<double> a(0.L, 3), ab(0.L, 3);
		for (int i = 0; i < n; ++i) {
			double x, y, z, vx, vy, vz;
			fin >> x >> y >> z;
			fin >> vx >> vy >> vz;

			a[0] += x;
			a[1] += y;
			a[2] += z;
			ab[0] += vx;
			ab[1] += vy;
			ab[2] += vz;
		}

		a /= n;
		ab /= n;

		std::valarray<double> w(-a), v(ab);
		double len2 = SQR(v[0]) + SQR(v[1]) + SQR(v[2]);
		double time;

		const double eps = 1e-9;
		if (std::abs(len2) <= eps)
			time = 0.L; // bezrazlichno
		else
			time = (w * v).sum() * (1.L / len2);
		
		//vdal'
		if (time < 0.L)
			time = 0.L;

		std::valarray<double> res = a + ab * time;
		double d = std::sqrt(SQR(res[0]) + SQR(res[1]) + SQR(res[2]));

		fout << std::fixed << std::setprecision(8);
		fout << "Case #" << testIdx << ": " << d << " " << time << "\n";
	}

#ifdef FILE_NAME
	fin.close();
	fout.close();
#endif

	return 0;
}
