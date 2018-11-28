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

template<typename t>
inline t sqr(const t x) {
	return x * x;
}

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

#define FILE_NAME "A-large"

int l, d, n;
std::set<std::string> dict;

int main(int argc, char *argv[]) {
#ifdef FILE_NAME
	std::ifstream fin(FILE_NAME ".in");
	std::ofstream fout(FILE_NAME ".out");
#else
#define fin (std::cin)
#define fout (std::cout)
#endif
	
	assert(fin && fout);

	fin >> l >> d >> n;

	std::string str;
	std::getline(fin, str);

	for (int i = 0; i < d; ++i) {
		std::getline(fin, str);
		dict.insert(str);
	}

	for (int i = 0; i < n; ++i) {
		std::getline(fin, str);
		std::set<std::string> w(dict);

		int strpos = 0;
		for (int j = 0; j < l; ++j) {
			if (str[strpos] != '(') {
				char ch = str[strpos];
				++strpos;

				std::set<std::string>::iterator it = w.begin();
				for (; it != w.end(); ) {
					if ((*it)[j] != ch)
						w.erase(it++);
					else
						++it;
				}

			} else {
				std::set<char> possib;
				for (++strpos; str[strpos] != ')'; ++strpos) {
					possib.insert(str[strpos]);
				}
				++strpos;

				std::set<std::string>::iterator it = w.begin();
				for (; it != w.end(); ) {
					if (possib.find((*it)[j]) == possib.end())
						w.erase(it++);
					else
						++it;
				}
			}
		}

		fout << "Case #" << i + 1 << ": " << w.size() << "\n";
	}

#ifdef FILE_NAME
	fin.close();
	fout.close();
#endif

	return 0;
}
