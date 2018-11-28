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
		cout << "Case #" << test + 1 << ": ";
		int candies_amount;
		cin >> candies_amount;
		vector<int> weights(candies_amount);
		int xor = 0;
		for (int i = 0; i < weights.size(); ++i) {
			cin >> weights[i];
			xor ^= weights[i];
		}
		if (xor == 0)
			cout << accumulate(all(weights), 0) - *min_element(all(weights)) << "\n";
		else 
			cout << "NO\n";
	}
	return 0;
}