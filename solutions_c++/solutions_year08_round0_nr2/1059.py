#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, a) for (int i = 0; i < int(a.size()); i++)
#define fors(i, a) for (int i = 0; i < int(a.length()); i++)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>

#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

int n, m, tar;
int ans;

struct event {
	int t;
	int side, add;
};

vector<event> ev;
int d[2], res[2];

bool operator < (const event& a, const event& b) {
	return (a.t < b.t) || (a.t == b.t && a.add > b.add);
}

void outdata() {
	cout << res[0] << " " << res[1] << endl;
}

void solve() {
	res[0] = res[1] = 0;
	sort(all(ev));
	d[0] = d[1] = 0;
	forv(i, ev) {
		d[ev[i].side] += ev[i].add;
		if (d[ev[i].side] < 0) {
			d[ev[i].side] = 0;
			res[ev[i].side]++;
		}
	}
}

void readdata() {
	cin >> tar >> n >> m;
	ev.clear();
	ans = 0;
	forn(i, n) {
		int hr, mn, t1, t2;
		scanf("%d:%d", &hr, &mn);
        t1 = hr * 60 + mn;		
		scanf("%d:%d", &hr, &mn);
        t2 = hr * 60 + mn + tar;
        event c;
        c.t = t1;
        c.side = 0;
        c.add = -1;
        ev.pb(c);
        c.t = t2;
        c.side = 1;
        c.add = 1;
        ev.pb(c);
	}
	forn(i, m) {
		int hr, mn, t1, t2;
		scanf("%d:%d", &hr, &mn);
        t1 = hr * 60 + mn;
		scanf("%d:%d", &hr, &mn);
        t2 = hr * 60 + mn + tar;
        event c;
        c.t = t1;
        c.side = 1;
        c.add = -1;
        ev.pb(c);
        c.t = t2;
        c.side = 0;
        c.add = 1;
        ev.pb(c);
	}
}

int main() {
	int tst;
	cin >> tst;
	forn(i, tst) {
		readdata();
		solve();
		cout << "Case #" << i + 1 << ": "; 
		outdata();
	}
	return 0;
}
