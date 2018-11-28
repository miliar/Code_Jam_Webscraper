#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <climits>
#include <cfloat>
#include <ctime>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
using namespace std;

typedef long long LL;
#define TT(s, b) template<class T> T s { return b; }
TT(minimize(T& a, T b), a = min(a, b))
TT(maximize(T& a, T b), a = max(a, b))
TT(bit(T i), 1<<i)
TT(sqr(T x), x*x)

int C[501][501];

int memo[501][501];

int f(int n, int r) {
	if (memo[n][r] >= 0) return memo[n][r];
	if (r == 1) return 1;
	int ans = 0;
	for (int i = 1; i < r; ++i) {
		ans += (LL(f(r, i)) * C[n - r - 1][r - i - 1]) % 100003;
	}
	return memo[n][r] = ans % 100003;
}


void solve() {
	int n;
	cin>>n;
	for (int i = 0; i < 501; ++i) {
		for (int j = 0; j < 501; ++j) {
			memo[i][j]=-1;
		}
	}
	int ans = 0;
	for (int i = 1; i < n; ++i) {
		ans += f(n, i);
	}
	cout<<(ans % 100003)<<endl;
}

int main() {
	freopen("solution.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	C[0][0] = 1;
	for (int i = 1; i <= 500; ++i) {
		C[0][i] = 0;
	}
	for (int i = 1; i <= 500; ++i) {
		C[i][0] = 1;
		for (int j = 1; j <= 500; ++j) {
			C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % 100003;
		}
	}

	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
}
