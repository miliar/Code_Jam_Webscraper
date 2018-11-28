#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;
template <class A, class B> void CONV(A &x, B &y) { stringstream s; s << x; s >> y; }
int CMP(double a, double b) { return a < b-1e-7 ? -1 : a > b+1e-7 ? 1 : 0; }
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

int main() {
	int t;
	cin >> t;
	FOR(i, 0, t) {
		LL r, k, n;
		cin >> r >> k >> n;
		vector<LL> g(n);
		FOR(j, 0, n) cin >> g[j];
		cout << "Case #" << i+1 << ": ";
		LL sum = accumulate(g.begin(), g.end(), 0LL);
		if (sum <= k) cout << r*sum << endl;
		else {
			int pos = 0;
			vector<LL> v, ind(n);
			vector<bool> vis(n, false);
			for(;;) {
				if (vis[pos]) break;
				vis[pos] = true;
				ind[pos] = v.size();
				sum = 0;
				for(;;) {
					if (sum+g[pos] > k) break;
					sum += g[pos];
					pos = (pos+1)%n;
				}
				v.push_back(sum);
			}
			pos = ind[pos];
			if (r < pos) cout << accumulate(v.begin(), v.begin()+r, 0LL) << endl;
			else {
				r -= pos;
				LL res = accumulate(v.begin(), v.begin()+pos, 0LL);
				v.erase(v.begin(), v.begin()+pos);
				res += (r/v.size())*accumulate(v.begin(), v.end(), 0LL);
				int rem = r%v.size();
				FOR(j, 0, rem) res += v[j];
				cout << res << endl;
			}
		}
	}
}
