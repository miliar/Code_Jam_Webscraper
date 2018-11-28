#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>

const int Max = 10000;

int cnt[Max+1];

int lowbit(int x) {
	return x&(x^(x-1));
}

void update(int x, int a) {
	if(x == 0) {
		cnt[x] += a;
		return ;
	}
	int p = x;
	while(p <= Max) {
		cnt[p] += a;
		p += lowbit(p);
	}
}

int sum(int x) {
	int p = x,tol = 0;
	while(p > 0) {
		tol += cnt[p];
		p -= lowbit(p);
	}
	return tol + cnt[0];
}

int n, a[Max], b[Max], c[Max];
int bid[Max], cid[Max], deleted[Max];

void input() {
	scanf("%d", &n);
	for(int i = 0;i < n;i ++) {
		scanf("%d%d%d", &a[i], &b[i], &c[i]);
	}
}

int cmpb(const void *lhs, const void *rhs) {
	return b[*(int *)rhs] - b[*(int *)lhs];
}

int cmpc(const void *lhs, const void *rhs) {
	return c[*(int *)rhs] - c[*(int *)lhs];
}

void solve_c(int &res, int mc) {
	memset(cnt, 0, sizeof(cnt));
	for(int i = 0;i < n;i ++) if(!deleted[i]) update(a[i], 1);

	int mb = 10000 - mc + 1;
	for(int i = 0;i < n;i ++) {
		int ti = bid[i];
		if(deleted[ti]) continue;
		if(b[ti] >= mb) {
			update(a[ti], -1);
			continue;
		}

		mb = b[ti];

		int tmp = sum(10000 - mc - mb);

		if(tmp > res) res = tmp;

		-- mb;
		update(a[ti], -1);
	}
}

void solve() {
	for(int i = 0;i < n;i ++) {
		bid[i] = cid[i] = i;
	}
	qsort(bid, n, sizeof(int), cmpb);
	qsort(cid, n, sizeof(int), cmpc);

	memset(deleted, 0, sizeof(deleted));

	int res = 0;
	
	int mc = 10001;
	for(int i = 0;i < n;i ++) {
		if(c[cid[i]] >= mc) {
			deleted[cid[i]] = 1;
			continue;
		}

		mc = c[cid[i]];

		solve_c(res, mc);

		-- mc;

		deleted[cid[i]] = 1;
	}

	printf("%d\n", res);
}

int main() {
	freopen("./input", "r", stdin);
	freopen("./output.txt", "w", stdout);

	int Cas;
	scanf("%d", &Cas);
	for(int i = 1;i <= Cas;i ++) {
		input();
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
