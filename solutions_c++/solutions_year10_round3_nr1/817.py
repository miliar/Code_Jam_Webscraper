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

using namespace std;
namespace ublas = boost::numeric::ublas;

typedef long long ll;

void solve() {
	int N;
	cin >> N;
	int A[N];
	int B[N];
	for (int i = 0; i < N; ++i) {
		cin >> A[i] >> B[i];
	}
	long inter = 0;
	for (int i = 0; i < N; ++i) {
		for (int j = i + 1; j < N; ++j) {
			if ((A[i] < A[j] && B[i] > B[j]) || (A[i] > A[j] && B[i] < B[j])) {
				++inter;
			}
		}
	}
	cout << inter << endl;
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
