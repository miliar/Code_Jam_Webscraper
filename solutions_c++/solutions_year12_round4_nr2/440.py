//============================================================================
// Author       : LAM PHAN VIET - lamphanviet@gmail.com
// Problem Name : 
// Time Limit   : .000s
// Description  : 
//============================================================================
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define AND(a,b) ((a) & (b))
#define OR(a,b) ((a) | (b))
#define XOR(a,b) ((a) ^ (b))
#define sqr(x) ((x) * (x))

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define eps 1e-7
#define maxN 1011

struct Circle {
	int len, x, y, r, pos;
	Circle() {}
	Circle(int rr, int p) { len = rr * 2; r = rr; pos = p; }
	bool operator < (const Circle &c) const {
		return len > c.len;
	}
	void print() {
		printf("%d.0 %d.0", x, y);
	}
} c[maxN];
struct Segment {
	int hei, len, x;
	Segment() {}
	Segment(int a, int b, int c) {
		hei = a; len = b; x = c;
	}
};
int n, W, L;
deque<Segment> seg;

bool cmp(Circle a, Circle b) {
	return a.pos < b.pos;
}

void solve() {
	sort(c, c + n);
	c[0].x = c[0].y = 0;
	int i = 1;
	seg.clear();
	seg.pb(Segment(c[0].r, c[0].r, 0));
	while (i < n) {
		int xx = seg.back().x + seg.back().len;
		if (xx + c[i].r <= L) {
			c[i].x = xx + c[i].r;
			c[i].y = 0;
			seg.pb(Segment(c[i].r, c[i].len, xx));
			i++;
		}
		else break;
		
	}
	int tmp = seg.back().x + seg.back().len;
	seg.pb(Segment(0, L - tmp, tmp));
	//if (i < n) puts("here");
	//return;
	int j = 0;
	while (i < n) {
		fr(_, 1, 1000) {
			j %= seg.size();
			if (j == 0) {
				if (seg[0].hei + c[i].r > W) {
					j = (j + 1) % seg.size();
					continue;
				}
				Segment tmp = Segment(seg[0].hei + c[i].len, c[i].r, 0);
				c[i].x = 0;
				c[i].y = seg[0].hei + c[i].r;
				while (seg.size() > 1 && tmp.len > seg.front().x + seg.front().len) {
					seg.pop_front();
				}
				if (!seg.size()) {
					seg.push_front(tmp);
					j = 0;
					break;
				}
				if (tmp.len > seg.front().x) {
					seg[0].x = tmp.len;
					seg.push_front(tmp);
				}
				j = (j + 1) % seg.size();
				break;
			}
			else {
				int h = seg[j].hei, xx = seg[j].x, len = seg[j].len;
				if (xx + c[i].r > L || h + c[i].r > W) {
					j = (j + 1) % seg.size();
					continue;
				}
				c[i].x = xx + c[i].r;
				c[i].y = h + c[i].r;
				Segment tmp = Segment(h + c[i].len, c[i].len, xx);
				while (seg.size() > 1 && tmp.x + tmp.len > seg[j].x + seg[j].len) {
					for (int k = j; k < seg.size() - 1; k++)
						seg[k] = seg[k + 1];
					seg.pop_back();
				}
				if (seg.size() && j < seg.size()) {
					seg[j].len = (seg[j].x + seg[j].len) - xx;
					seg[j].x = xx;
					seg[j].hei = h + c[i].len;
				}
				break;
			}
		}
		i++;
	}
}

int main() {
	#ifndef ONLINE_JUDGE
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	#endif
	int cases, caseNo = 0, r;
	for (scanf("%d", &cases); cases--; ) {
		scanf("%d %d %d", &n, &L, &W);
		rep(i, n) {
			scanf("%d", &r);
			c[i] = Circle(r, i);
		}
		solve();
		printf("Case #%d:", ++caseNo);
		sort(c, c + n, cmp);
		rep(i, n) {
			putchar(' ');
			c[i].print();
		}
		puts("");
	}
	return 0;
}

// Copyright (C) 2012, LamPhanViet