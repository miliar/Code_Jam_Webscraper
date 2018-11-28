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


void run()
{
	int n, q;
	vector<string> v;
	map<string, int> ind;
	scanf("%d %d", &n, &q);
	
	for (int i = 0; i < n; ++i) {
		char s[16];
		scanf("%s", s);
		v.push_back(s);
		ind[s] = i;
	}
	for (int i = 0; i < q; ++i) {
		char ord[32];
		scanf("%s", ord);
		vector<vector<string> > vv;
		vector<int> score;

		map<int, vector<string> > mm;
		for (int j = 0; j < n; ++j) {
			mm[sz(v[j])].push_back(v[j]);
		}
		for (map<int, vector<string> >::iterator mi = mm.begin(); mi != mm.end(); ++mi) {
			if (sz(mi->second) != 1) {
				vv.push_back(mi->second);
				score.push_back(0);
			}
		}
		if (sz(vv) == 0) {
			printf(" %s", v[0].c_str());
			continue;
		}
		int bestres = 0;
		string beststr = v[0];
		for (int j = 0; j < 26 && !vv.empty(); ++j) {
			vector<vector<string> > next;
			vector<int> nextscore;
			for (int k = 0; k < sz(vv); ++k) {
				vector<string> &cur = vv[k];
				int curscore = score[k];
				map<vector<int>, vector<string> > mp;
				for (int l = 0; l < sz(cur); ++l) {
					string &curs = cur[l];
					vector<int> v;
					int pp = 0;
					while (1) {
						int nm = curs.find(ord[j], pp);
						if (nm == -1) break;
						v.push_back(nm);
						pp = nm + 1;
					}
					mp[v].push_back(curs);
				}
				if (sz(mp) == 1 && ((mp.begin())->first).empty()) {
					next.push_back(cur);
					nextscore.push_back(curscore);
				}
				else {
					for (map<vector<int>, vector<string> >::iterator mi = mp.begin(); mi != mp.end(); ++mi) {
						if (sz(mi->second) != 1) {
							next.push_back(mi->second);
							nextscore.push_back(curscore + (mi->first).empty());
						}
						else {
							string &sss = (mi->second)[0];
							int sc = curscore;
							if ((mi->first).empty()) {
								++sc;
							}
							if (sc > bestres || (sc == bestres && ind[sss] < ind[beststr])) {
								beststr = sss;
								bestres = sc;
							}
						}
					}
				}
			}
			vv = next;
			score = nextscore;
		}
		printf(" %s", beststr.c_str());
	}
}

int main()
{
	freopen("B1.in", "r", stdin);
	freopen("B1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d:", i);
		run();
		puts("");
	}
	return 0;
}