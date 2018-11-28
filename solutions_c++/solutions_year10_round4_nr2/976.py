#include <iostream>
using namespace std;

struct Node {
	int l, r;
	int v;
	int lev;
}st[1<<12];

void init(int i, int l, int r) {
	if(i == 1) st[i].lev = 0;
	else st[i].lev = st[i / 2].lev + 1;
	st[i].l = l;
	st[i].r = r;
	st[i].v = 0;
	if(l == r) return;
	init(i * 2, l, (l + r) / 2);
	init(i * 2 + 1, (l + r) / 2 + 1, r);
}

int ans;

void update(int i) {
	if(st[i * 2].v || st[i * 2 + 1].v) {
		st[i].v = max(st[i * 2].v, st[i * 2 + 1].v);
		if(st[i].v > st[i].lev) {
			st[i].v--;
			ans++;
		}
	}
	

	if(i > 1 && i % 2 == 1) update(i / 2);
}

void insert(int i, int p, int x) {
	if(st[i].l == st[i].r) {
		st[i].v = x;
		if(i % 2 == 1) update(i / 2);
		return;
	}
	int m = (st[i].l + st[i].r) / 2;
	if(p <= m) insert(i * 2, p, x);
	else insert(i * 2 + 1, p, x);
}

int main() {
	freopen("E://B-small-attempt2.in", "r", stdin);
	freopen("E://out.txt", "w", stdout);
	int t, n, m;
	int tc = 0;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		m = 1 << n;
		ans = 0;
		init(1, 0, m - 1);
		for(int i = 0; i < m; i++) {
			int x; scanf("%d", &x);
			insert(1, i, n - x);
		}
		for(int i = 0; i < m - 1; i++) scanf("%*d");
		printf("Case #%d: %d\n", ++tc, ans);
	}
	return 0;
}