#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
#include <memory.h>
#include <ctype.h>

#include <iostream>

#include <string>
#include <complex>
#include <numeric>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>

//#pragma comment(linker, "/stack:64000000")

using namespace std;

template<typename TYPE> inline TYPE sqr(const TYPE& a) { return (a) * (a); }

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1000 * 1000 * 1000;
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 10100;

int n, m;
vector<int> s[11];
string words[N];
int mask[N][27];

void gen_mask() {
	forn(i, n) {
		for(char c = 'a'; c <= 'z'; ++c) {
			forn(j, words[i].size())
				if(words[i][j] == c)
					mask[i][c - 'a'] |= (1 << j);
		}
	}
}

string ab;
int res, mav;

void rec(int k, queue<pt>& q) {
	int id = ab[k] - 'a';
	vector<pair<int, pt> > ms(q.size()); // mask, id, points
	int msi = 0;
	bool nz = false;
	while(!q.empty()) {
		int nx = q.front().first;
		int p = q.front().second;
		q.pop();
		ms[msi++] = mp(mask[nx][id], pt(nx, p));
		if(mask[nx][id]) {
			nz = true;
		}
	}
	if(!nz) {
		forn(i, ms.size())
			q.push(ms[i].second);
		rec(k + 1, q);
		return;
	}
	sort(all(ms));
	for(int i = 0; i < ms.size(); ) {
		if(i + 1 < ms.size() && ms[i].first == ms[i + 1].first) {
			int j = i;
			while(j < ms.size() && ms[i].first == ms[j].first) {
				if(ms[i].first == 0) {
					++ms[j].second.second;
				}
				q.push(ms[j].second);
				++j;
			}
			rec(k + 1, q);
			while(!q.empty())
				q.pop();
			i = j;
		} else {
			int cur_v = ms[i].second.second;
			if(ms[i].first == 0)
				++cur_v;
			int cur_i = ms[i].second.first;
			if(cur_v > mav || (cur_v == mav && cur_i < res)) {
				mav = cur_v;
				res = cur_i;
			}
			++i;
		}
	}
}

void solve(int it) {
	scanf("%d%d\n", &n, &m);
	for1(i, 10)
		s[i].clear();
	memset(mask, 0, sizeof mask);
	forn(i, n) {
		getline(cin, words[i]);
		s[words[i].size()].pb(i);
	}
	gen_mask();
	printf("Case #%d:", it);
	forn(it, m) {
		getline(cin, ab);
		res = 0, mav = 0;
		for1(len, 10) {
			if(s[len].size() < 2)
				continue;
			queue<pt> q; // id, points
			forn(i, s[len].size())
				q.push(pt(s[len][i], 0));
			rec(0, q);
		}
		printf(" %s", words[res].c_str());
	}
	printf("\n");
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int test;
	scanf("%d\n", &test);

	for1(it, test) {
		solve(it);
	}

	return 0;
}
