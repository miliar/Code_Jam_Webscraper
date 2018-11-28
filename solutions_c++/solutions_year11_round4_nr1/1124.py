#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <tr1/unordered_set>
#include <tr1/unordered_map>
#include <gmpxx.h>

using namespace std;
using namespace tr1;

typedef mpz_class number;

#define EPS 1e-9

struct Walkway {
	int from, to, w;
	bool operator <(const Walkway &w) const {
		return from < w.from;
	}
};

int main () {
	int T, test = 1;
	
	cin >> T;
	while (T--) {
		int X, S, R, t, n;
		
		cin >> X >> S >> R >> t >> n;
		
		vector <Walkway> walk(n);
		
		for (int i=0; i < n; i++) {
			cin >> walk[i].from >> walk[i].to >> walk[i].w;
		}
		
		sort(walk.begin(), walk.end());
		
		vector < pair <int,int> > steps; // speed, distance
		
		for (int now=0, i=0; now < X; ) {
			if (i == n) {
				steps.push_back(make_pair(S, X-now));
				now = X;
			}
			else {
				if (walk[i].from > now) {
					steps.push_back(make_pair(S, walk[i].from-now));
					now = walk[i].from;
				}
				steps.push_back(make_pair(S+walk[i].w, walk[i].to-walk[i].from));
				now = walk[i].to;
				i++;
			}
		}
		
		sort(steps.begin(), steps.end());
		
		double ans = 0.0;
		double left = t;
		
		for (int i=0; i < steps.size(); i++) {
			//printf("%lf %d %d\n",left,steps[i].first,steps[i].second);
			if (left > EPS) {
				int s2 = steps[i].first + R - S;
				if (left+EPS < steps[i].second / (double) s2) {
					double run = s2 * left;
					ans += left + (steps[i].second - run) / (double) steps[i].first;
					left = 0.0;
				}
				else {
					ans += steps[i].second / (double) s2;
					left -= steps[i].second / (double) s2;
				}
			}
			else {
				ans += steps[i].second / (double) steps[i].first;
			}
		}
		
		printf("Case #%d: %.9lf\n", test++, ans);
	}
	
	return 0;
}
