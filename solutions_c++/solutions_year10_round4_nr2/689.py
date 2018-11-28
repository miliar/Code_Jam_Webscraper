#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

const int maxp = 10, maxn = 1 << maxp;

int a[maxn];
int m[maxn], l[maxn];
int p, n;
int sum[maxn*2];

long long calculate (int u, int level, int point) {
	if (sum[u] <= point) {
		return 0;
	}
	long long min_val = a[u] + calculate(u*2, level+1, point+1) + calculate(u*2+1, level+1, point+1);
	if (p - level > sum[u] - point) {
		min_val = min (min_val, calculate(u*2, level+1, point) + calculate(u*2+1, level+1, point));
	}
	return min_val;
}

void make () {
	scanf ("%d", &p);
	n = 1 << p;
	for (int i = 0; i < n; i++) {
		scanf ("%d", &m[i]);
		l[i] = p - m[i];
	}
	for (int i = p-1; i >= 0; i--) {
		for (int j = 0; j < 1 << i; j++) {
			scanf ("%d", &a[(1 << i) + j]);
		}
	}
	for (int i = n; i < n*2; i++) {
		sum[i] = l[i-n];
	}
	for (int i = n-1; i > 0; i--) {
		sum[i] = max (sum[i*2], sum[i*2+1]);
	}
/*	for (int i = 1; i < n; i++) {
		printf ("%d ", a[i]);
	}
	printf ("\n");
	for (int i = 1; i < n*2; i++) {
		printf ("%d ", sum[i]);
	}
	printf ("\n");
	cerr << p << " " << n;
	cout.flush();
*/	printf ("%I64d\n", calculate (1, 0, 0));
}

int main () {
	freopen ("b.in", "rt", stdin);
	freopen ("b.out", "wt", stdout);
	int T; scanf ("%d\n", &T);
	for (int t = 1; t <= T; t++) {
		printf ("Case #%d: ", t);
		make();
	}
	return 0;
}
