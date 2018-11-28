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

int t, n, k;

int main() {
	assert(fin && fout);
	std::ios_base::sync_with_stdio(false);

	fin >> t;
	for (int test = 0; test < t; ++test) {
		fin >> n >> k;
		++k;
		k %= 1 << n;
		
		fout << "Case #" << test + 1 << ": " << (k == 0 ? "ON" : "OFF") << '\n';
	}
	
	return 0;
}
