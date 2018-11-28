#include <iostream>
#include <cstdio>
#include <algorithm>
#include <deque>

using namespace std;

const int MAX_N = 1000;

struct area {
	bool w[4];
	int p[4];
};

deque<area> q;

int n;
pair<int, int> r[MAX_N];//r, nr
int w, l;

int pos[MAX_N][2];

int now;

void put(int nr, int x, int y) {
	pos[r[nr].second][0] = x;
	pos[r[nr].second][1] = y;
}

void make() {
	area a;
	a.w[0] = a.w[1] = a.w[2] = a.w[3] = false;
	a.p[0] = a.p[1] = 0;
	a.p[2] = w;
	a.p[3] = l;
	q.push_front(a);
	now = n-1;
	
	while (now >= 0 && !q.empty()) {
		a = q.front();
		q.pop_front();
		int size = r[now].first;
		int x = a.p[0] + (a.w[0] ? size : 0);
		int y = a.p[1] + (a.w[1] ? size : 0);
		put(now, x, y);
		now--;
		
		area b, c;
		//down - front
		b = a;
		b.w[1] = true;
		b.p[1] = y + size;
		
		//right - back
		c = a;
		c.w[0] = true;
		c.w[3] = true;
		c.p[0] = x + size;
		c.p[3] = y + size;
		
		int bottom = b.p[3] - b.p[1];
		if (!b.w[3])
			bottom *= 2;
		int right = c.p[2] - b.p[0];
		if (bottom < right) {
			area temp = b;
			b = c;
			c = temp;
		}
		q.push_front(b);
		q.push_back(c);
	}
	
	/*
	int x, y;
	x = w;
	y = l;
	while (x >= 0 && y >= 0) {
		int nx = x, ny = y;
		put(now--, nx, ny);
		while (nx - r[now].first >= 0) {
			put(now, nx - r[now].first, ny)
		
	}
	*/
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cin >> n >> w >> l;
		for (int i = 0; i < n; i++) {
			cin >> r[i].first;
			r[i].second = i;
		}
		sort(r, r+n);
		make();
		cout << "Case #" << test << ": ";
		for (int i = 0; i < n; i++)
			cout << pos[i][0] << ' ' << pos[i][1] << ' ';
		cout << endl;
	}
	return 0;
}
