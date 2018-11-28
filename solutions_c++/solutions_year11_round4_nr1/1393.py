#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool ok;
struct ddd {
	int b,e,w;
	bool operator < (const ddd &ot) const {
		if (ok) return b < ot.b;
		return w < ot.w;
	}
};

ddd d[1111];

int main() {

	freopen("input.txt.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; cin >> t;
	for (int e=1; e<=t; e++) {
		int x,s,t,n;
		double r;
		cin >> x >> s >> r >> t >> n;

		int mx = 0;
		for (int i=0; i<n; i++) {
			cin >> d[i].b >> d[i].e >> d[i].w;
			mx = max(mx, d[i].e);
		}

		ok = true;
		sort(d, d+n);

		ok = false;
		d[n].b = mx;
		d[n].e = x;
		d[n].w = 0;

		++n;

		multiset<ddd> run;

		double ans = 0;

		int prv = 0;
		double sp = 0;
		double lft = t;

		for (int i=0; i<n; i++) {
			int cur = d[i].b;
			ddd tmp;
			tmp.b = prv;
			tmp.e = cur;
			tmp.w = sp;
			run.insert(tmp);

			double needRunTime = (double)(cur - prv) / (sp + r);
			if (needRunTime > lft + 1e-11) {
				double can = (sp + r) * lft;
				ans += lft;
				ans += (cur - prv - can) / (sp + s);
				lft = 0;
			} else {
				ans += (double)(cur - prv) / (sp + r);
				lft -= (double)(cur - prv) / (sp + r);
			}

			prv = cur;
			sp = d[i].w;

			cur = d[i].e;

			tmp.b = prv;
			tmp.e = cur;
			tmp.w = sp;
			run.insert(tmp);

			needRunTime = (double)(cur - prv) / (sp + r);
			if (needRunTime > lft + 1e-11) {
				double can = (sp + r) * lft;
				ans += lft;
				ans += (cur - prv - can) / (sp + s);
				lft = 0;
			} else {
				ans += (double)(cur - prv) / (sp + r);
				lft -= (double)(cur - prv) / (sp + r);
			}

			prv = cur;
			sp = 0;
		}

		ans = 0;

		lft = t;

		while (!run.empty()) {
			ddd now = *run.begin();
			run.erase(run.begin());

			double needRunTime = (double)(now.e - now.b) / (now.w + r);
			if (needRunTime > lft + 1e-11) {
				double can = (now.w + r) * lft;
				ans += lft;
				ans += (now.e - now.b - can) / (now.w + s);
				lft = 0;
			} else {
				ans += (double)(now.e - now.b) / (now.w + r);
				lft -= (double)(now.e - now.b) / (now.w + r);
			}
		}
			
		printf("Case #%d: %0.9lf\n", e, ans);

	}	

	return 0;
}
