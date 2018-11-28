#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>

struct triple {
	int l, r, w, key;
};

bool operator <(const triple& a, const triple& b) {
	return a.key > b.key;
}

void solve2() {
	int X, S, R, t, N;
	scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
	std::vector< std::pair<int, int> > p;
	int pos = 0;
	for (int i = 0; i < N; ++i) {
		int l, r, w;
		scanf("%d%d%d", &l, &r, &w);
		if (pos < l) p.push_back(std::make_pair(0, l - pos));
		p.push_back(std::make_pair(w, r - l));
		pos = r;
	}
	if (pos < X)
		p.push_back(std::make_pair(0, X - pos));
	sort(p.begin(), p.end());
	double T = t, time = 0;
	for (int i = 0; i < p.size(); ++i) {
		double nw = p[i].first + R;
		double nt = p[i].second / nw;
		if (T < nt) {
			time += T + (p[i].second - nw * T) / (p[i].first + S);
			T = 0;
		} else {
			time += nt;
			T -= nt;
		}
	}
	printf(" %.9lf\n", time);
}

void solve() {
	int X, S, R, t, N;
	scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
	std::priority_queue<triple> q, p;
	for (int i = 0; i < N; ++i) {
		triple a;
		scanf("%d%d%d", &a.l, &a.r, &a.w);
		a.key = a.l;
		q.push(a);
		a.key = a.r;
		q.push(a);
	}
	triple dop;
	dop.key = X;
	dop.w = 0;
	dop.l = 0;
	dop.r = X;
	q.push(dop);
	int pos = 0;
	double time = 0;
	std::multiset<int> vs;
	vs.insert(0);
	while (q.size()) {
		triple cur = q.top();
		q.pop();
		if (cur.key > pos) {
			triple t;
			t.l = cur.key - pos;
			t.w = *--vs.end();
			t.key = t.w;
			p.push(t);
			pos = cur.key;
		}
		if (cur.key == cur.l) {
			vs.insert(cur.w);
		} else {
			vs.erase(cur.w);
		}
	}
	double T = t;
	while (p.size()) {
		triple t = p.top();
		p.pop();
		int nw = t.w + R;
		double nt = 1. * t.l / nw;
		if (T < nt) {
			time += T;
			time += (t.l - nw * T) / (t.w + S);
			T = 0;
		} else {
			time += nt;
			T -= nt;
		}
	}
	printf(" %.9lf\n", time);
}

char s[1024];
int main(int argc, char* argv[]) {
    freopen(argv[1], "r", stdin);
    strcat(s, argv[1]);
    strcat(s, ".out");
    freopen(s, "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d:", i+1);
		solve2();
    }
        
}