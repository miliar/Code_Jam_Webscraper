#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <assert.h>
#include <complex>
#include <cctype>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef complex<double> tComp;

const double EPS = 1e-9;

struct paint {
	int col, a, b;
}P[300];

bool operator<(const paint &a, const paint &b) {
	return a.a < b.a;
}

typedef vector<paint> VP;
vector<paint> bc[300];

int main() {
	int tc;
	scanf("%d",&tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int n;
		cin >> n;
		for (int i=0; i<n; ++i)
			bc[i].clear();
		map<string, int> col;
		for (int i=0; i<n; ++i) {
			string cname;
			cin >> cname >> P[i].a >> P[i].b;
			assert(P[i].a >= 1 && P[i].a <= P[i].b && P[i].b <= 10000);
			int ts = col.size();
			if (col.find(cname) == col.end())
				col[cname] = ts;
			P[i].col = col[cname];
			bc[P[i].col].push_back(P[i]);
		}
		int best = n + 1;
		for (int c1=0; c1<(int)col.size(); ++c1)
			for (int c2=c1; c2<(int)col.size(); ++c2)
				for (int c3=c2; c3<(int)col.size(); ++c3) {
					VP tmp;
					tmp.insert(tmp.end(), bc[c1].begin(),
					bc[c1].end());
					tmp.insert(tmp.end(), bc[c2].begin(),
					bc[c2].end());
					tmp.insert(tmp.end(), bc[c3].begin(),
					bc[c3].end());
					sort(tmp.begin(), tmp.end());
					map<int, int> visit;
					visit[0] = 0;
					for (VP::iterator itv=tmp.begin();
itv!=tmp.end(); ++itv) {
						// find min value in interval [itv->a-1, 10000]
						map<int, int>::iterator it=visit.lower_bound(itv->a-1);
						if (it == visit.end())
							continue;
						int v = it->second + 1;
						map<int, int>::iterator it2=visit.upper_bound(itv->b);
						assert(it2 != visit.begin());
						if (it2 != visit.end() && it2->second <= v)
							continue;
						--it2;
						assert(it2->first <= itv->b);
						if (it2->first == itv->b && it2->second <= v)
							continue;
						map<int, int>::iterator it3 = it2;
						++it2;
						while(it3 != visit.begin() && it3->second >= v)
							--it3;
						if (it3 == visit.begin() && it3->second >= v)
							visit.erase(it3, it2);
						else
							visit.erase(++it3, it2);
						visit[itv->b] = v;
						int last = -1;
						for (map<int, int>::iterator it=visit.begin(); it!=visit.end(); ++it) {
							assert(it->second > last);
							last = it->second;
						}
					}
					if (visit.find(10000) != visit.end())
						best = min(best, visit[10000]);
				}
		if (best > n) puts("IMPOSSIBLE");
		else printf("%d\n", best);
	}
	return 0;
}
