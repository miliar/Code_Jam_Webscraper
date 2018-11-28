#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

double run()
{
	int x, s, r, t, n;
	scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
	double sumt = 0;
	vector<pair<int, int> > vp;
	int sumlen = 0;
	for (int i = 0; i < n; ++i) {
		int b, e, w;
		scanf("%d %d %d", &b, &e, &w);
		vp.push_back(make_pair(w, e - b));
		sumlen += (e - b);
	}
	vp.push_back(make_pair(0, x - sumlen));
	sort(all(vp));
	double tt = t;
	for (int i = 0; i < sz(vp); ++i) {
		double needt = vp[i].second / double(r + vp[i].first);
		if (needt < tt) {
			sumt += needt;
			tt -= needt;
		}
		else {
			double runlen = tt * (r + vp[i].first);
			double leftt = (vp[i].second - runlen) / double(s + vp[i].first);
			sumt += (leftt + tt);
			tt = 0;
		}
	}
	return sumt;
}

int main()
{
	freopen("A2.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %.10f\n", i, run());
	}
	return 0;
}