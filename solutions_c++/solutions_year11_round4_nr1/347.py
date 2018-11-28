#include <iostream>
using namespace std;

const int maxn = 1000 + 10;

int tcase, X, S, R, t, n, B[maxn], E[maxn], w[maxn], len[maxn], ord[maxn];
double ans, remain;

bool comp(const int &u, const int &v) {
	return B[u] < B[v];
}

bool comp2(const int &u, const int &v) {
	return w[u] < w[v];
}

void init() {
	scanf("%d%d%d%d%d", &X, &S, &R, &t, &n);
	for (int i = 1; i <= n; ++i) {
		scanf("%d%d%d", B+i, E+i, w+i);
		len[i] = E[i] - B[i];
	}
}

void work() {
	//prepare
	for (int i = 0; i <= n; ++i)
		ord[i] = i;
	sort(ord+1, ord+n+1, comp);
	w[0] = len[0] = E[0] = 0;
	for (int i = 1; i <= n; ++i)
		len[0] += B[ord[i]] - E[ord[i - 1]];
	len[0] += X - E[ord[n]];
	sort(ord+1, ord+n+1, comp2);

	//greedy algorithm
	ans = 0, remain = (double)t;
	for (int i = 0; i <= n; ++i) {
		double runtime = min(remain, len[ord[i]] / (double)(R + w[ord[i]]));
		ans += runtime + (len[ord[i]] - runtime * (R + w[ord[i]])) / (S + w[ord[i]]);
		remain -= runtime;
		//cout << "?"<< len[ord[i]] << " "<< w[ord[i]] << endl;
		//cout << ans << " "<< runtime << endl;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcase);
	for (int k = 1; k <= tcase; ++k) {
		init();
		work();
		printf("Case #%d: %.9lf\n", k, ans);
	}
	return 0;
}
