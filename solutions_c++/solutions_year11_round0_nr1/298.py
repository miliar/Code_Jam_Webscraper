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

int n, m;

void solve() {
	int i, j, k;
	scanf("%d", &n);
	int ans = 0;
	int cp[2] = {1, 1};
	int next_task[2] = {1, 1};
	vector<pair<int, int> > p;
	for (i = 0; i < n; ++ i) {
		char buf[2];
		int pos;
		scanf("%s %d", buf, &pos);
		int id = (buf[0] == 'O') ? 0 : 1;
		p.push_back(make_pair(id, pos));
	}
	for (i = 0; i < sz(p); ++ i) {
		for (k = 0; k < 2; ++ k) {
			for (j = i; j < sz(p); ++ j) {
				if (p[j].first == k) {
					next_task[k] = p[j].second;
					break;
				}
			}
			if (j == sz(p)) {
				next_task[k] = cp[k];
			}
		}
		while (cp[p[i].first] != p[i].second) {
			for (k = 0; k < 2; ++ k) {
				if (cp[k] > next_task[k]) {
					-- cp[k];
				} else if (cp[k] < next_task[k]) {
					++ cp[k];
				}
			}
			++ ans;
		}
		++ ans;
		k = 1 - p[i].first;
		if (cp[k] > next_task[k]) {
			-- cp[k];
		} else if (cp[k] < next_task[k]) {
			++ cp[k];
		}
	}
	printf("%d\n", ans);
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