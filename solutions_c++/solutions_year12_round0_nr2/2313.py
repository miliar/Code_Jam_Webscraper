#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cassert>
#include <string>
#include <cstring>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define forn(i, n) for(int i = 0;i < n;i++)

typedef long long ll;
typedef unsigned long long llu;

const int inf = 2e9;
const double eps = 1e-7;
const double pi = 3.1415926535;

class googler {
public:
	pair <int, int> score; 
	int good;
	googler() {}
};

bool oper(const googler& a, const googler& b) {
	if(a.good != b.good) {
		return a.good > b.good;
	}
	return a.score.first > b.score.first;
}

int n, s, p;
int a[111];
googler b[111];

int solve_one() {
	forn(i, n) {
		if(a[i] == 0) {
			b[i].score = mp(0, -1);
		} else if(a[i] == 1) {
			b[i].score = mp(1, -1);
		} else if(a[i] == 29) {
			b[i].score = mp(10, -1);
		} else if(a[i] == 30) {
			b[i].score = mp(10, -1);
		} else if(a[i] % 3 == 0) {
			b[i].score = mp(a[i] / 3, a[i] / 3 + 1);
		} else if(a[i] % 3 == 1) {
			b[i].score = mp(a[i] / 3 + 1, a[i] / 3 + 1);
		} else {
			b[i].score = mp(a[i] / 3 + 1, a[i] / 3 + 2);
		}
		if(b[i].score.second != -1 && b[i].score.second >= p && b[i].score.first < p) b[i].good = 1;
		else b[i].good = 0;
	}
	int res = 0, used = 0;
	sort(b, b + n, oper);
	forn(i, n) {
		if(b[i].score.second == -1) {
			if(b[i].score.first >= p) res++;
		} else {
			if(used < s) {
				if(b[i].score.second >= p) res++;
				used++;
			} else {
				if(b[i].score.first >= p) res++;
			}
		}
	}

	return res;
}

int main() {
	int tests;
	scanf("%d", &tests);
	forn(t, tests) {
		scanf("%d%d%d", &n, &s, &p);
		forn(i, n) {
			scanf("%d", &a[i]);
		}
		int res = solve_one();
		cout << "Case #" << t + 1 << ": " << res << endl;
	}
	return 0;
}
