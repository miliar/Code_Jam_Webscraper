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
	int n, m;
	cin>>n>>m;
	set<string> exist;
	for (int i = 0; i < n; ++i) {
		string s;
		cin>>s;
		exist.insert(s);
	}
	int ans = 0;
	for (int i = 0; i < m; ++i) {
		string dir;
		cin>>dir;
		dir.push_back('/');
		for (int j = 1; j < dir.size(); ++j) {
			if (dir[j] == '/') {
				string pre = dir.substr(0, j);
				if (exist.count(pre) == 0) {
					exist.insert(pre);
					++ans;
				}
			}
		}
	}
	cout<<ans<<endl;
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
