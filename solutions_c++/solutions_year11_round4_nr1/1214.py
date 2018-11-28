#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const double eps = 1e-8;

int x, s, r, t, n;

int dcmp(double x) {
	if (x < -eps) return -1;
	else return x > eps;
}

void solve() {
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	double tim = t;
	r -= s;
	int b, e, w;
	map<int, int> mp;
	for (int i = 0; i < n; ++i) {
		scanf("%d%d%d", &b, &e, &w);
		x -= e - b;
		if (mp.find(w + s) == mp.end()) {
			mp[w + s] = e - b;
		} else {
			mp[w + s] += e - b;
		}
	}
	mp[s] = x;
	map<int, int>::iterator it;
	double ans = 0;
	for (it = mp.begin(); it != mp.end(); ++it) {
		double len = it->second;
		double v = it->first;
		if (dcmp(tim) <= 0) {
			ans += len / v;
		} else {
			double z = (v + r) * tim;
			if (dcmp(z - len) <= 0) {
				ans += tim + (len - z) / v;
				tim = 0;
			} else {
				tim -= len / (v + r);
				ans += len / (v + r);
			}
		}
	}
	printf("%.9lf\n", ans);
}

int main() {
//	freopen("in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
