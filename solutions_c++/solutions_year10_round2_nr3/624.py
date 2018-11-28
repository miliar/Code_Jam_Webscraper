#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/foreach.hpp>
#include <boost/math/special_functions/binomial.hpp>


using namespace std;
namespace ublas = boost::numeric::ublas;

typedef long long ll;

long count(int size, int last) {
	if (size == 1) return 1;
	long res = 0;
	for (int i = 1; i <= last - size && i <= size - 1; ++i) {
		if (i == 1) res += count(size - 1, size);
		else res += (long)boost::math::binomial_coefficient<double>(last - size - 1, i - 1) * count(size - i, size);
	}
	return res;
}

void solve() {
	int n;
	cin >> n;
	long res = 0;
	for (int i = 1; i < n; ++i) {
		res += count(i, n);
	}
	cout << res % 100003 << endl;
}

int main(int argc, char* argv[]) {
	int Tests;
	cin >> Tests;
	for (int test = 1; test <= Tests; ++test) {
		cout << "Case #" << test << ": ";
		solve();
	}
	return 0;
}
