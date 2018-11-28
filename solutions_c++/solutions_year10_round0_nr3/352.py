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

vector<LL> g;

pair<int, LL> getNext(int i, LL k) {
	LL c = 0;
	while (c+g[i]<=k) {
		c+=g[i];
		++i;
		if (i>=g.size()) {
			i=0;
		}
	}
	return make_pair(i, c);
}

void solve() {
	LL r, k, n;
	cin>>r>>k>>n;
	g.resize(n);
	LL s=0;
	for (int i=0; i<n; ++i) {
		cin>>g[i];
		s+=g[i];
	}
	if (k>s) {
		k=s;
	}
	vector<int> next(n);
	vector<LL> val(n);
	for (int i=0; i<n; ++i) {
		pair<int, LL> t = getNext(i, k);
		next[i]=t.first;
		val[i]=t.second;
	}
	vector<int> vis(n,-1);
	vector<LL> sum(n);
	int i=0;
	LL v=0;
	int c=0;
	while (vis[i]<0) {
		vis[i]=c;
		sum[i]=v;
		++c;
		v+=val[i];
		i=next[i];
	}
	LL ans = 0;
	int j = 0;
	if (vis[i]<=r) {
		r -= vis[i];
		ans += sum[i];
		int cs = c - vis[i];
		LL cv = v - sum[i];
		ans += r / cs * cv;
		r %= cs;
		j = i;
	}
	for (i=0; i<r; ++i) {
		ans += val[j];
		j = next[j];
	}
	cout<<ans<<endl;
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
