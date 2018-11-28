#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <set>
#include <utility>
#include <algorithm>

using namespace std;

#define sqr(x) ((x)*(x))

double eps = 1e-9;

int n, w, l;
int r[1000];
int x[1000], y[1000];

bool check(int i, int j) {
	double xx = sqr((double) x[i] - (double) x[j]), yy = sqr((double) y[i] - (double) y[j]);
	if (sqrt(xx + yy) > (double) r[i] + (double) r[j] - eps)
		return true;
	else
		return false;
}

int rando() {
	return rand() * 32768 + rand();
}

int main() {
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		printf("Case #%d: ", tt);
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 0; i < n; i++) {
			scanf("%d", &r[i]);
		}
		while (1) {
			bool finish = true;
			for (int i = 0; i < n; i++) {
				bool ff = false;
				for (int j = 0; j < 1000; j++) {
					x[i] = rando() % (w + 1);
					y[i] = rando() % (l + 1);
					bool flag = true;
					for (int k = 0; k < i; k++) {
						if (!check(i, k)) {
							flag = false;
							break;
						}
					}
					if (flag) {
						ff = true;
						break;
					}
				}
				if (!ff) {
					finish = false;
					break;
				}
			}
			if (finish)
				break;
		}
		for (int i = 0; i < n; i++)
			printf("%d %d ", x[i], y[i]);
		printf("\n");
	}
}