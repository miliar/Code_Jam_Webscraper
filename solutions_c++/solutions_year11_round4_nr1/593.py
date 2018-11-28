// MS Visual C++ 2008 Express
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;

const long double EPS = 1e-10;
int sp[1000001];

int cmp(const void *a, const void *b)
{
	return *((int *) a) - *((int *) b);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int tk = 1; tk <= T; tk++) {
		int x, s, r, t, n;
		cin >> x >> s >> r >> t >> n;
		for (int i = 0; i < x; i++) sp[i] = 0;
		int b, e, w;
		for (int i = 0; i < n; i++) {
			cin >> b >> e >> w;
			for (int j = b; j < e; j++) sp[j] = w;
		}
		
		qsort(sp, x, sizeof(sp[0]), cmp);
		long double tm = 0, tr = t;
		for (int i = 0; i < x; i++) {
			long double tmp = 1 / (long double) (sp[i] + r);
			if (tr - tmp > -EPS) {
				tr -= tmp;
				tm += 1 / (long double) (sp[i] + r);
			}
			else if (tr < EPS) {
				tm += 1 / (long double) (sp[i] + s);
			}
			else {
				long double q = (sp[i] + r) * tr;
				tm += tr + (1 - q) / (long double) (sp[i] + s);
				tr = 0;
			}
		}
		printf("Case #%d: %.8llf\n", tk, tm);
	}

	return 0;
}