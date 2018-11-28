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

#define FILE_NAME "C-small"

const int maxn = 16;

bool a[maxn][maxn];
int in[maxn][25];
int memo[1 << maxn]; //ololo
std::bitset<(1 << maxn)> compat; //ololo
std::bitset<(1 << maxn)> compatComputed; //ololo
int n, k;

inline bool isCompat(int x, int y) {
	if (in[x][0] < in[y][0])
		std::swap(x, y);

	for (int i = 0; i < k; ++i)
		if (in[x][i] <= in[y][i])
			return false;

	return true;
}

int Brute(int s) {
	if (s == 0)
		return 0;

	else if (memo[s] == 0) {
		int ans = (1 << maxn) + 5;

		if (compat[s])
			ans = 1;

		else {
			for (int t = s; t > 0; t = (t - 1) & s) {
				if (compat[t])
					ans = std::min(ans, Brute(s ^ t) + 1);
			}
		}

		memo[s] = ans;
	}

	return memo[s];
}

bool CalcCompat(int m) {
	if (m == 0)
		return true;
	if (compatComputed[m])
		return compat[m];

	bool ans = false;

	for (int i = 0; i < n; ++i) {
		if ((m & (1 << i)) && CalcCompat(m ^ (1 << i))) {
			bool ok = true;
			for (int j = 0; j < n; ++j) {
				if (i != j && (m & (1 << j)) && !a[i][j]) {
					ok = false;
					break;
				}
			}

			if (ok)
				ans = true;
		}
	}
	
	compatComputed[m] = true;
	return compat[m] = ans;
}

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
		fin >> n >> k;

		memset(memo, 0, sizeof memo);
		compatComputed = std::bitset<(1 << maxn)>();

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < k; ++j)
				fin >> in[i][j];
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				a[i][j] = a[j][i] = isCompat(i, j);
			}
		}

		CalcCompat((1 << n) - 1);

		int ans = Brute((1 << n) - 1);
		fout << "Case #" << testIdx << ": " << ans << "\n";
	}

#ifdef FILE_NAME
	fin.close();
	fout.close();
#endif

	return 0;
}
