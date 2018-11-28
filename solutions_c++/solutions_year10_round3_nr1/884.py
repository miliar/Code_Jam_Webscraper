#include <cstdlib>

#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <limits>
#include <exception>

#include <cmath>
#include <cstring>
#include <cassert>
#include <ctime>

#include <string>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <deque>
#include <list>

#define ALL(container) (container).begin(), (container).end()
#define MP std::make_pair
#define SZ(x) int((x).size())

#define X first
#define Y second

typedef long long i64;
typedef unsigned long long u64;

typedef std::pair<int, int> pii;

template<typename t>
inline t sqr(const t x) {
	return x * x;
}

#define FILE_NAME "test"
std::ifstream fin(FILE_NAME ".in");
std::ofstream fout(FILE_NAME ".out");

int t, n;

const int XX = 1000;

inline int sign(int x) {
	if (x < 0)
		return -1;
	else if (x > 0)
		return 1;
	else
		return 0;
}

int main() {
	assert(fin && fout);
	std::ios_base::sync_with_stdio(false);

	fin >> t;
	for (int testIdx = 1; testIdx <= t; ++testIdx) {
		fin >> n;
		std::vector<pii> data(n);
		for (int i = 0; i < n; ++i)
			fin >> data[i].first >> data[i].second;

		int ans = 0;
		for (int i = 0; i < n; ++i) {
			int a, b, c;
			a = data[i].second - data[i].first;
			b = -XX;
			c = -b * data[i].first;

			for (int j = i + 1; j < n; ++j) {
				int d1 = a * 0 + b * data[j].first + c;
				int d2 = a * XX + b * data[j].second + c;
				if (sign(d1) * sign(d2) == -1)
					++ans;
			}
		}

		fout << "Case #" << testIdx << ": " << ans << '\n';
	}
	
	return 0;
}
