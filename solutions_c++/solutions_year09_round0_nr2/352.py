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

#define FILE_NAME "B-large"

const int maxn = 110 * 110;
int dsu[maxn];
int map[110][110];

int DsuFind(const int x) {
	return x == dsu[x] ? x : dsu[x] = DsuFind(dsu[x]);
}

void DsuUnite(int x, int y) {
	x = DsuFind(x);
	y = DsuFind(y);

	if (rand() & 1)
		std::swap(x, y);

	dsu[x] = y;
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
		int n, m;
		fin >> n >> m;

		for (int i = 0; i < n * m; ++i)
			dsu[i] = i;

		std::vector<std::pair<int, std::pair<int, int> > > q;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				int h;
				fin >> h;

				map[i][j] = h;
				q.push_back(MP(h, MP(i, j)));
			}
		}

		std::sort(ALL(q), std::greater<std::pair<int, std::pair<int, int> > >());

		for (int i = 0; i < n * m; ++i) {
			int ch = q[i].first;
			int ci = q[i].second.first;
			int cj = q[i].second.second;

			const int dds[][2] = {
				{-1, 0},
				{0, -1},
				{0, +1},
				{+1, 0},
			};

			int ni = -1, nj;
			for (int d = 0; d < 4; ++d) {
				int ti = ci + dds[d][0];
				int tj = cj + dds[d][1];

				if (ti < 0 || ti >= n || tj < 0 || tj >= m)
					continue;

				if (map[ti][tj] < map[ci][cj]) {
					if (ni == -1 || map[ti][tj] < map[ni][nj]) {
						ni = ti;
						nj = tj;
					}
				}
			}

			if (ni != -1)
				DsuUnite(ci * m + cj, ni * m + nj);
		} //q

		fout << "Case #" << testIdx << ":\n";

		std::map<int, char> colors;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				int pr = DsuFind(i * m + j);
				if (colors.find(pr) == colors.end()) {
					colors[pr] = 'a' + colors.size();
				}

				fout << colors[pr] << " ";
			}

			fout << "\n";
		}
	}

#ifdef FILE_NAME
	fin.close();
	fout.close();
#endif

	return 0;
}
