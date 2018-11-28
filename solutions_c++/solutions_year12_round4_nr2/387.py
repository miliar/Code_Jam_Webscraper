#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

#define maxn (1005)

int x[maxn], y[maxn], r[maxn], rep[maxn];
int ansx[maxn], ansy[maxn];
int n, w, l;

bool cmp(int a, int b) {
	return r[a] > r[b];
}

void work() {
	scanf("%d%d%d", &n, &w, &l);
	for (int i = 0; i < n; ++i) scanf("%d", &r[i]);
	for (int i = 0; i < n; ++i) rep[i] = i;
	sort(rep, rep + n, cmp);
	
	int now = 0, cur = 1, opt, tot; 
	x[rep[0]] = y[rep[0]] = 0, tot = opt = r[rep[0]];
	
	for (; cur < n && r[rep[cur]] + tot <= l; ++cur) {
		y[rep[cur]] = tot + r[rep[cur]], x[rep[cur]] = now;
		tot += r[rep[cur]] * 2;
	} 
	now += opt;
	
	while (cur < n) {
		y[rep[cur]] = 0, x[rep[cur]] = now + r[rep[cur]], tot = opt = r[rep[cur]];
		cur++;
		for (; cur < n && r[rep[cur]] + tot <= l; ++cur) {
			y[rep[cur]] = tot + r[rep[cur]], x[rep[cur]] = now + r[rep[cur]];
			tot += r[rep[cur]] * 2;
		}
		now += opt + opt;
	}
	
	for (int i = 0; i < n; ++i) if (x[i] > w) puts("Oops!!");
	for (int i = 0; i < n; ++i) printf(" %d %d", x[i], y[i]);
	puts("");
}

int main() {
	int T; scanf("%d", &T);
	
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d:", t);
		work();
	}
	
	return 0;
}
