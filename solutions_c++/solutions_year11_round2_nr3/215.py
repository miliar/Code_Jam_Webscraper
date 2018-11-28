#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cassert>
#include <functional>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ctime>
#include <deque>

using namespace std;

void prepare() {
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

#define fo(a,b,c) for( a = (b); a < (c); ++ a )
#define fr(a,b) fo(a,0,(b))
#define fi(n) fr(i,(n))
#define fj(n) fr(j,(n))
#define fk(n) fr(k,(n))
#define mp make_pair
#define pb push_back
#define all(a) (a).begin( ), (a).end( )
#define _(a, b) memset( (a), (b), sizeof( a ) )
#define __(a) memset( (a), 0, sizeof( a ) )
#define sz(a) (int)(a).size( )

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair <int, int> PII;

const int INF = 2000000000;
const int MAXN = 2005;

int n, m;
int s[MAXN][2];
vector<pair<int, int> > v[MAXN];
vector<int> p;
vector<vector<int> > path;
vector<int> cycles[MAXN];
vector<set<int> > cols;
vector<set<int> > cp;
set<pair<PII, int> > q;
int answer[MAXN];

bool solveit2(int ans) {
	int i, j, k;
	_(answer, -1);
	cols.clear();
	set<int> ccq;
	for (i = 0; i < ans; ++ i) {
		ccq.insert(i + 1);
	}
	q.clear();
	cp.clear();
	for (i = 0; i < sz(path); ++ i) {
		set<int> t;
		for (j = 0; j < sz(path[i]); ++ j) {
			if (sz(cycles[path[i][j]]) > 1) {
				t.insert(path[i][j]);
			}
		}
		cp.push_back(t);
		cols.push_back(ccq);
		q.insert(mp(mp(sz(cp[i]), sz(cols[i])), i));
	}
	while (!q.empty()) {
		int id = q.begin()->second;
		int cnt = q.begin()->first.first;
		q.erase(q.begin());
		int col = 1;
		if (!cols[id].empty()) {
			col = *cols[id].begin();
		}
		if (cp[id].empty()) {
			continue;
		}
		int po = *cp[id].begin();
		answer[po] = col;
		//remove points and update it
		for (i = 0; i < sz(cycles[po]); ++ i) {
			int cid = cycles[po][i];
			q.erase(mp(mp(sz(cp[cid]), sz(cols[cid])), cid));
			cols[cid].erase(col);
			cp[cid].erase(po);
			int val = sz(cp[cid]);
			if (!cp[cid].empty()) {
				q.insert(mp(mp(val, sz(cols[cid])), cid));
			}
		}
	}
	for (i = 0; i < n; ++ i) {
		if (answer[i] < 0) {
			assert(sz(cycles[i]) == 1);
			int id = cycles[i][0];
			int col = 1;
			if (!cols[id].empty()) {
				col = *cols[id].begin();
			}
			cols[id].erase(col);
			answer[i] = col;
		}
	}
	for (i = 0; i < sz(cols); ++ i) 
	{
		if (sz(cols[i]) > 0) {
			return false;
		}
	}
	return true;
}

bool check(int ans) {
	int i, j;
	int q[10];
	for (i = 0; i < sz(path); ++ i) {
		for (j = 1; j <= ans; ++ j) {
			q[j] = 0;
		}
		for (j = 0; j < sz(path[i]); ++ j)
		{
			int c=  answer[path[i][j]];
			if (c < 0 ){ 
				return false;
			}
			q[c] = 1;
		}
		for (j = 1; j <= ans; ++ j) {
			if (q[j] == 0) {
				return false;
			}
		}
	}
	return true;
}

bool brute(int id, int ans) {
	if (id == n) {
		return check(ans);
	}
	int i; 
	for (i = 0; i < ans; ++ i) {
		answer[id] = i + 1;
		if (brute(id +1, ans)) {
			return true;
		}
	}
	return false;
}

bool solveit(int ans) {
	return brute(0, ans);
}

void solve() {
	int i, j, k;
	scanf("%d %d", &n, &m);
	for (j = 0; j < 2; ++ j) {
		for (i = 0; i < m; ++ i) {
			scanf("%d", &s[i][j]);
		}
	}
	for (i = 0; i < n; ++ i) {
		v[i].clear();
		v[i].pb(mp((i + 1) % n, 1));
	}
	for (i = 0; i < m; ++ i) {
		v[s[i][0] - 1].pb(mp(s[i][1] - 1, 1));
		v[s[i][1] - 1].pb(mp(s[i][0] - 1, 1));
	}
	bool ok = true;
	path.clear();
	for (i = 0; i < n; ++ i) {
		for (j = 0; j < sz(v[i]); ++ j) {
			if (v[i][j].second) {
				p.clear();
				int st = i;
				int ii = i;
				int jj = j;
				while (1) {
					v[ii][jj].second = 0;
					p.push_back(ii);
					int nid = v[ii][jj].first; 
					if (nid == st) {
						break;
					}
					int best = ii;
					int nj;
					for (k = 0; k < sz(v[nid]); ++ k) {
						if (v[nid][k].second) {
							int idd = v[nid][k].first;
							if (idd < ii) {
								idd += n;
							}
							if (idd > best) {
								best = idd;
								nj = k;
							}
						}
					}
					assert(best != ii);
					ii = nid;
					jj = nj;
				}
				path.pb(p);
			}
		}
	}
	int ans = n;
	for (i = 0; i < sz(path); ++ i) {
		ans = min(ans, sz(path[i]));
	}
	for (i = 0; i < n; ++ i) {
		cycles[i].clear();
	}
	for (i = 0; i < sz(path); ++ i) {
		for (j = 0; j < sz(path[i]); ++ j) {
			cycles[path[i][j]].pb(i);
		}
	}
	while (ans > 0) {
		if (solveit(ans)) {
			break;
		}
		assert(0);
	}
	printf("%d\n", ans);
	for (i = 0; i < n; ++ i) {
		if (i) {
			printf(" ");
		}
		printf("%d", answer[i]); 
	}
	printf("\n");
}

int main() {
	prepare();
	int tn;
	cin >> tn;
	int t = 0;
	while (t++ < tn) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}