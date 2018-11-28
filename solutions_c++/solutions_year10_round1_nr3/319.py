#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
static const double PI2 = 8.0 * atan(1.0);
typedef long long ll;

bool check(int a, int b) {
	bool result = true;
	for (;;) {
		if (a == b) {
			return !result;
		}
		if (a >= b * 2) {
			return result;
		}
		a %= b;
		swap(a, b);
		result ^= true;
	}

	return result;
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;
		int answer = 0;
		for (int a = A1; a <= A2; ++a) {
			for (int b = B1; b <= B2; ++b) {
				answer += check(max(a, b), min(a, b));
			}
		}

		printf("Case #%d: %d\n", t, answer);
	}
}
