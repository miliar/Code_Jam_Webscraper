//#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#include <set>
#include <map>
using namespace std;

struct time {
	int h, m;
	time(int h, int m): h(h), m(m) {};
	int getm() {
		return h * 60 + m;
	}
};

bool operator < (const time& a, const time& b) {
	return a.h < b.h || (a.h == b.h && a.m < b.m);
}

int delay, na, nb;
int a[1501], b[1501];
vector<time> sta, stb;

inline void input() {
	scanf("%d%d%d", &delay, &na, &nb);
	fill(a, a + 1501, 0);
	fill(b, b + 1501, 0);
	sta.clear();
	stb.clear();
	int h, m;
	for (int i = 0; i < na; ++i) {
		scanf("%d:%d", &h, &m);
		sta.push_back(time(h, m));
		scanf("%d:%d", &h, &m);
		int d = h * 60 + m + delay;
		if (d < 1501)
			b[d]++;
	}
	for (int i = 0; i < nb; ++i) {
		scanf("%d:%d", &h, &m);
		stb.push_back(time(h, m));
		scanf("%d:%d", &h, &m);
		int d = h * 60 + m + delay;
		if (d < 1501)
			a[d]++;
	}
}

inline void solve(int test) {
	sort(sta.begin(), sta.end());
	sort(stb.begin(), stb.end());
	int ca = 0, cb = 0;
	for (vector<time>::iterator it = sta.begin(); it < sta.end(); ++it) {
		int t = it->getm();
		int i;
		for (i = 0; i <= t; ++i)
			if (a[i])
				break;
		if (i > t) {
			++ca;
		} else {
			a[i]--;
		}
	}
	for (vector<time>::iterator it = stb.begin(); it < stb.end(); ++it) {
		int t = it->getm();
		int i;
		for (i = 0; i <= t; ++i)
			if (b[i])
				break;
		if (i > t) {
			++cb;
		} else {
			b[i]--;
		}
	}
	printf("Case #%d: %d %d\n", test, ca, cb);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	sta.reserve(100);
	stb.reserve(100);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		input();
		solve(i);
	}
	return 0;
}
