#include <iostream>

using namespace std;

const int N = 1010;

const int M = 1000010;

const double eps = 1e-10;

typedef struct node {
	int b, e, w;
}Walk;

Walk ways[N];

bool cmp(Walk a, Walk b) {
	if (a.w < b.w) {
		return true;
	}
	return false;
}

bool mark[M];

int main() {

	int Tc;
/*	
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("a.smal.out", "w", stdout);
*/
	freopen("A-large.in", "r", stdin);
	freopen("a.large.out", "w", stdout);

	scanf("%d", &Tc);

	for (int tc = 1; tc <= Tc; ++tc) {
		
		int x, s, r, t, n;

		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);

		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d", &(ways[i].b), &(ways[i].e), &(ways[i].w));
		}

		sort(ways, ways + n, cmp);
		
		double ans = 0.0;
		
		for (int i = 0; i < x; ++i) {
			mark[i] = false;
		}
		
		double rest = t;

		for (int i = 0; i < n; ++i) {
			for (int j = ways[i].b; j < ways[i].e; ++j) {
				mark[j] = true;
			}
		}

		for (int i = 0; i < x; ++i) {
			if (mark[i] == false) {
				double len = 1.0;
				double rt = len / r;
				double st = len / s;
				
				if (rt < rest + eps) {
					ans += rt;
					rest -= rt;
				} else {
					ans += rest;
					len -= rest * r;
					ans += len / s;
					rest = 0.0;
				}
			}
		}
		
		for (int i = 0; i < n; ++i) {
		
			double len = ways[i].e - ways[i].b;
			double rt = 1.0 * len / (ways[i].w + r);
			double st = 1.0 * len / (ways[i].w + s);

			if (rt < rest + eps) {
				ans += rt;
				rest -= rt;
			} else {
				ans += rest;
				len -= rest * (ways[i].w + r);
				ans += len / (ways[i].w + s);
				rest = 0.0;
			}
		}

		printf("Case #%d: %lf\n", tc, ans);
	}

	return 0;
}

		
			




	
