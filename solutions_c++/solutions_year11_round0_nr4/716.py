#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		cerr << test << " from " << tests << " completed!\n";
		int n;
		cin >> n;
		vector<int> permutation(n);
		for (int i = 0; i < n; ++i) {
			cin >> permutation[i];
			--permutation[i];
		}
		int amount_of_moves = 0;
		vector<bool> used(n, false);
		for (int i = 0; i < n; ++i) {
			if (!used[i]) {
				int cur = i;
				int cycle_lenght = 0;
				while(!used[cur]) {
					++cycle_lenght;
					used[cur] = true;
					cur = permutation[cur];
				}
				if (cycle_lenght > 1)
					amount_of_moves += cycle_lenght;
			}
		}
		printf("Case #%d: %lf\n", test + 1, 1.0 * amount_of_moves);
	}
	return 0;
}