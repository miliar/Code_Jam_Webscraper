#include <string>
#include <cstdio>
using namespace std;

inline int ABS(int x) {
	return (x < 0) ? (-x) : x;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t, T, n, i, pos;
	int tot, lasto, lastb, cost, delta, o, b;
	char* s = new char[20];
	for (t = 1, scanf("%d", &T); t <= T; t++) {
		scanf("%d", &n);
		o = 1, b = 1;
		lasto = 0, lastb = 0;
		tot = 0;
		for (i = 0; i < n; i++) {
			scanf("%s %d", s, &pos);
			if (s[0] == 'O') {
				delta = ABS(o - pos);
				if (lastb < delta) {// if didn't have time to move enough spaces
					cost = 1 + delta - lastb; //move then push
				} else {
					cost = 1; // just push
				}
				lasto += cost;
				lastb = 0;
				o = pos;
			} else {
				delta = ABS(b - pos);
				if (lasto < delta) {// if didn't have time to move enough spaces
					cost = 1 + delta - lasto; //move then push
				} else {
					cost = 1; // just push
				}
				lasto = 0;
				lastb += cost;
				b = pos;
			}
			//printf("delta: %d  ", delta);
			//printf("cost : %d\n", cost);
			tot += cost;
		}
		printf("Case #%d: %d\n", t, tot);
	}
	fclose(stdout);
	return 0;
}
