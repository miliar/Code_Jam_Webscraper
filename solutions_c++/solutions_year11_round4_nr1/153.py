#include <cstdio>
#include <algorithm>
using namespace std;

struct w {
	int l, s;
	bool operator<(const w &x) const {
		return s < x.s;
	}
} walkway[1005];

int T, x, s, r, t, n;
int main() {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A.out", "w");

	fscanf(fin, "%d", &T);
	for (int test = 0; test < T; test++) {
		fscanf(fin, "%d %d %d %d %d", &x, &s, &r, &t, &n);
		int len = 0;
		for (int i = 0; i < n; i++) {
			int a, b;
			fscanf(fin, "%d %d %d", &a, &b, &walkway[i].s);
			walkway[i].l = b-a;
			len += walkway[i].l;
		}
		walkway[n].l = x-len, walkway[n].s = 0;
		sort(walkway, walkway+n+1);

		double ans = 0, run = 0;
		for (int i = 0; i <= n; i++) {
			//printf("%d %d\n", walkway[i].l, walkway[i].s);
			double add = (walkway[i].l)/(double)(walkway[i].s+r);
			if (run >= t) {
				ans += (walkway[i].l)/(double)(walkway[i].s+s);
			}
			else if (run+add <= t) {
				run += add;
				ans += add;
			}
			else {
				double left = t-run;
				double dist = left*(walkway[i].s+r);
				double distleft = walkway[i].l-dist;
				//printf("left dist distleft %f %f %f\n", left, dist, distleft);
				ans += (distleft)/(walkway[i].s+s) + left;
				run = t;
			}
		}
		fprintf(fout, "Case #%d: %lf\n", test+1, ans);
	}


	return 0;
}
