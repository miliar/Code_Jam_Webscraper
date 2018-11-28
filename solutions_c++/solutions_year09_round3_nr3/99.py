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

#define FILE_NAME "C-large"

std::map<std::pair<int, int>, int> memo;
std::vector<int> place;

int Solve(const int left, const int right, const int lp, const int rp) {
	if (left > right || lp > rp)
		return 0;

	if (memo.find(MP(left, right)) == memo.end()) {
		int ans = INT_MAX;
		for (int i = lp; i <= rp; ++i) {
			int na = right - left;
			na += Solve(left, place[i] - 1, lp, i - 1);
			na += Solve(place[i] + 1, right, i + 1, rp);

			ans = std::min(ans, na);
		}

		return memo[MP(left, right)] = ans;
	}

	return memo[MP(left, right)];
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
		int n, q;
		fin >> n >> q;

		place.clear();
		for (int i = 0; i < q; ++i) {
			int x;
			fin >> x;
			place.PB(x - 1);
		}

		int ans = 0;
		std::sort(ALL(place));

		memo.clear();
		ans = Solve(0, n - 1, 0, q - 1);

		fout << "Case #" << testIdx << ": " << ans << "\n";
	}

#ifdef FILE_NAME
	fin.close();
	fout.close();
#endif

	return 0;
}


/*
		int ans = INT_MAX;
		//std::vector<int> var(q);
		//for (int i = 0; i < q; ++i)
		//	var[i] = i;
		//
		//do {
		//	int res = 0;
		//	std::vector<bool> a(n, false);
		//	for (int i = 0; i < q; ++i) {
		//		int wh = place[var[i]];
		//		a[wh] = true;
		//		for (int j = wh - 1; j >= 0 && !a[j]; --j)
		//			++res;
		//		for (int j = wh + 1; j < n && !a[j]; ++j)
		//			++res;
		//	}

		//	ans = std::min(ans, res);
		//} while (std::next_permutation(ALL(var)));

		fout << "Case #" << testIdx << ": " << ans << "\n";
*/

/*
		std::set<int> place;
		for (int i = 0; i < q; ++i) {
			int x;
			fin >> x;
			place.insert(x - 1);
		}

		int ans = 0;
		std::set<piii> intervals;
		intervals.insert(MP(n, MP(0, n - 1)));

		for (int i = 0; !place.empty(); ++i) {
			piii interval = *intervals.begin();
			intervals.erase(intervals.begin());
			std::set<int>::iterator it = place.lower_bound(interval.second.first);

			if (it != place.end() && *it <= interval.second.second) {
				int wh = *it;
				ans += interval.first - 1;
				if ((wh - 1) - interval.second.first + 1 > 0)
					intervals.insert(MP((wh - 1) - interval.second.first + 1, MP(interval.second.first, wh - 1)));
				if (interval.second.second - (wh + 1) + 1 > 0)
					intervals.insert(MP(interval.second.second - (wh + 1) + 1, MP(wh + 1, interval.second.second)));
				place.erase(it);
			}
		}
*/