#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <numeric>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define ss stringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vii vector<pii >
#define vs vector<string>
#define LD long double

using namespace std;

//always reset global variables!

vi s[110];
int n, k;
int g[110][110];
int deg[110];

bool intersect(int I, int J) {
	fr(i, k - 1) {
		if(s[I][i] >= s[J][i] && s[I][i + 1] <= s[J][i + 1]) return true;
		if(s[I][i] <= s[J][i] && s[I][i + 1] >= s[J][i + 1]) return true;
	}
	return false;
}

int calc(vi& v) {
	bool complete = true;
	fr(i, sz(v)) fr(j, sz(v)) if(i != j) complete &= g[v[i]][v[j]];
	if(complete) {
		fprintf(stderr, "Complete!\n");
		return sz(v);
	}
	bool oddcycle = true;
	fr(i, sz(v)) oddcycle &= deg[v[i]] == 2;
	oddcycle &= (sz(v) % 2 == 1);
	if(oddcycle) {
		fprintf(stderr, "Odd cycle!\n");
		return 3;
	}
	int mxd = 0;
	if(sz(v) == 1) return 1;
	fr(i, sz(v)) mxd >?= deg[v[i]];
	return mxd;
}

int kiek(vi v) {
	int m = sz(v);
	int mn = beg;
	if(sz(v) == 0) return 0;
	fr(mask, 1 << m) if(mask) {
		vi w;
		fr(i, m) if(mask & 1 << i) {
			w.pb(v[i]);
		}
		bool ok = true;
		fr(i, sz(w)) fr(j, i) if(g[w[i]][w[j]]) ok = false;
		if(!ok) continue;
		vi t;
		fr(i, m) if(mask & 1 << i) ; else t.pb(i);
		mn <?= 1 + kiek(t);
	}
	return mn;
}

void solveCase() {
	fr(i, 110) s[i].clear();
	memset(deg, 0, sizeof(deg));
	cin >> n >> k;
	fr(i, n) {
		fr(j, k) {
			int t;
			cin >> t;
			s[i].pb(t);
		}
	}
	memset(g, 0, sizeof(g));
	fr(i, n) fr(j, n) if(i != j) g[i][j] = intersect(i, j);
	fr(i, n) fr(j, n) deg[i] += g[i][j];
	bool comp[110];
	memset(comp, false, sizeof(comp));
	int mn = 0;
//	cout << endl;
//	fr(i, n) fr(j, n) cout << g[i][j] << (j == n - 1 ? '\n' : '\t');
/*	fr(i, n) if(comp[i] == false) {
		vi v;
		v.pb(i);
		int ind = 0;
		comp[i] = true;
		while(ind < sz(v)) {
			fr(j, n) if(g[v[ind]][j] && comp[j] == false) {
				comp[j] = true;
				v.pb(j);
			}
			ind++;
		}
//		cout << sz(v) << endl;
		mn >?= calc(v);
	} */
//	vi v;
//	fr(i, n) v.pb(i);
//	mn = kiek(v);
	int mx = 0;
	fr(masks, 1 << n) {
		bool ok = true;
		fr(i, n) fr(j, i) if(masks & (1 << i)) if(masks & (1 << j)) {
			if(!g[i][j]) ok = false;
		}
		if(ok) {
			int kiek = 0;
			fr(i, n) if(masks & (1 << i)) kiek++;
			mx >?= kiek;
		}
	}
	cout << mx << endl;
}

int main() {
	int t;
	cin >> t;
	fr(i, t) {
		cout << "Case #" << i + 1 << ": ";
		solveCase();
	}
	return 0;
}
