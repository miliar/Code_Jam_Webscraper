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

void solve() {
	int n, k, b, T;
	cin>>n>>k>>b>>T;
	vector<pair<int, int> > a(n);
	for (int i = 0; i < n; ++i) {
		cin>>a[i].first;
	}
	for (int i = 0; i < n; ++i) {
		cin>>a[i].second;
	}
	sort( a.begin(), a.end());
	reverse( a.begin(), a.end());

	int ans = 0;
	int c = 0;
	int p = 0;
	for (int i = 0; i < n; ++i) {
		if (c >= k) {
			break;
		}
		int d = b - a[i].first;
		int s = a[i].second;
		int t = (d + s - 1) / s;
		if (t <= T) {
			ans += p;
			++c;
		}
		else {
			++p;
		}
	}
	if (c < k) {
		cout<<"IMPOSSIBLE"<<endl;
	}
	else {
		cout<<ans<<endl;
	}
}

int main() {
	freopen("solution.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
}
