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
	LL n, k;
	cin>>n>>k;
	cout<<((k+1)&((1<<n)-1) ? "OFF" : "ON")<<endl;
}

int main() {
	freopen("gcj.in", "rt", stdin);
	freopen("gcj.out", "wt", stdout);
	int n;
	cin>>n;
	for (int i=1; i<=n; ++i) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
}
