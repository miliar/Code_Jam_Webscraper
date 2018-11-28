/*
 ID: conan.d1
 PROG: B
 LANG: C++
 */
#include <cstring>
#include <iterator>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
using namespace std;
#define SZ(v)                   (int)v.size()
#define all(v)					v.begin(), v.end()
typedef long long ll;
const int OO = 1 << 28;

int di[] = { 1, 0, -1, 0 };
int dj[] = { 0, 1, 0, -1 };

int n, s, p;
vector<int> v;
int dp[101][101];
int calc(int idx, int sleft) {
	if (idx == n)
		return 0;

	int &ret = dp[idx][sleft];
	if (ret != -1)
		return ret;

	ret = 0;
	if (!v[idx])
		return ret = calc(idx + 1, sleft) + !p;
	int s = v[idx] / 3;
	int rem = v[idx] % 3;

	if (rem == 0) {
		if (sleft)
			ret = calc(idx + 1, sleft - 1) + (s + 1 >= p);
		ret = max(ret, calc(idx + 1, sleft) + (s >= p));
	}
	if (rem == 1) {
		ret = calc(idx + 1, sleft) + (s + 1 >= p);
	}
	if (rem == 2) {
		ret = calc(idx + 1, sleft) + (s + 1 >= p);
		if (sleft)
			ret = max(ret, calc(idx + 1, sleft - 1) + (s + 2 >= p));
	}

	return ret;
}

int main() {
//	freopen("B2.in", "r", stdin);
//	freopen("B2.out", "w", stdout);
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; cs++) {
		v.clear();
		cin >> n >> s >> p;
		v.resize(n);
		for (int i = 0; i < n; ++i)
			cin >> v[i];
		memset(dp, -1, sizeof(dp));
		cout << "Case #" << cs << ": " << calc(0, s) << endl;
	}
	return 0;
}

